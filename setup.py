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
    install_requires=['numpy', 'scipy', 'skggm', 'sksparse', 'robsel'],
)