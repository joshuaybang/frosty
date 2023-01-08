from utils import standardize
import numpy as np
import networkx as nx

def generate_barabasi(p, m=1, random_state=2023):
    G = nx.powerlaw_cluster_graph(n=p, m=m, p=0, seed=random_state)
    B = nx.to_numpy_array(G)
    B = np.tril(B)
    P = np.zeros((p,p))
    for i in range(p):
        P[p-i-1,i] = 1
    B = B @ P
    B = np.rot90(B,3)
               
    return B

def generate_erdos_renyi(ps, exp_num_edges, random_state=2023):
    edge_prob = (2*exp_num_edges[i])/(p*(p-1))
    G = nx.generators.random_graphs.erdos_renyi_graph(n=ps[i], p=edge_prob, seed=random_state)
    B = nx.to_numpy_matrix(G)
    B = np.tril(B)

    return B
    
def generate_data(B, lower_weight=0.25, upper_weight=1.0, n_prop_to_p=2, random_state=2023):
    p = len(B)
    n = int(n_prop_to_p*p)
    L = np.eye(p) - B
    Omega = L @ L.T
    Omega = np.where(Omega != 0, 1, 0)
    
    np.random.seed(random_state)
    edge_weights = np.random.uniform(low=lower_weight, high=upper_weight, size=(p,p))
    edge_signs = np.random.choice([-1,1], size=(p,p))
    edges = np.multiply(edge_weights, edge_signs)
    Omega = np.multiply(edges, Omega)
    Omega = 0.5*(np.tril(Omega) + np.tril(Omega).T)
    np.fill_diagonal(Omega, 1.2*np.abs(Omega).sum(1))
    
    # set diagonal to 1
    diag_inv = np.diag(1/np.sqrt(np.diag(Omega)))
    Omega = diag_inv @ Omega @ diag_inv
    Cov = np.linalg.inv(Omega)

    rs = np.random.RandomState(random_state)
    X = rs.multivariate_normal(mean=np.zeros(p), cov=Cov, size=n)
    X_std = standardize(X, bias=False)
            
    return X_std