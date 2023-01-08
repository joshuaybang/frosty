import numpy as np
import scipy
from inverse_covariance import QuicGraphicalLasso
import sksparse
import robsel

def amd(A):
    """
    Parameters
    ----------
    A: ndarray
        Symmetric positive definite matrix
    
    Returns
    -------
    L: ndarray
        Sparse Cholesky factor
    perm: ndarray
        Permutation ordering recovered by AMD
    """
    p = len(A)
    csc = scipy.sparse.csc_matrix(A)
    factor = sksparse.cholmod.cholesky(csc, ordering_method='amd')
    L = factor.L().toarray()
    perm = np.argsort(factor.P())
        
    return L, perm
    

def frosty(X, alpha=0.99, b=200, diag=True, random_state=2023):
    """
    FROSTY algorithm for Bayesian network estimation
    
    Parameters
    ----------
    X: ndarray of shape (n_samples, n_features)
        Data matrix
    alpha: float, default=0.99
        (1-alpha) confidence level for robust selection
    b: int, default=200
        Number of bootstrap samples for robust selection
    diag: bool, default=True
        Whether or not to include diagonal when compute RWP function
    random_state: int, default=2023
        Random state instance
    
    Returns
    -------
    B: ndarray of shape (n_features, n_features)
        Estimated Bayesian network
    """
    np.random.seed(random_state)
    n, p = X.shape
    
    # RobSel
    lam = robsel.RobustSelection(X, alpha, b, diag)
    
    # graphical lasso
    quic = QuicGraphicalLasso(lam=lam).fit(X)
    Omega = quic.precision_
    
    L, perm = amd(Omega)
    L_orig = L[:,perm][perm]
    B = (np.diag(np.diag(L_orig)) - L_orig) @ np.diag(1 / np.diag(L_orig))
    
    return B