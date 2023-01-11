from setuptools import setup

setup(
    name='frosty',
    version='0.0.1',
    description='Implementation of the FROSTY algorithm',
    author='Joshua Bang',
    author_email='joshuaybang@gmail.com',
    url='https://github.com/joshuaybang/frosty',
    keywords='bayesian network structure learning',
    packages=['frosty'],
    python_requires='>=3.6, <3.10',
    install_requires=['numpy', 'scipy', 'Cython',
                      'skggm @ git+https://github.com/skggm/skggm.git@develop#egg=skggm',
                      'scikit-sparse', 'robust-selection', 'networkx'],
)