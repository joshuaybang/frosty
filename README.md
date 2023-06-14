# FROSTY

Python Package for FROSTY by Joshua Bang and Sang-Yun Oh

Joshua Bang, Sang-Yun Oh (2023). FROSTY: A High-dimensional Scale-free Bayesian Network Learning Method. Journal of Data Science. \[[JDS](https://jds-online.org/journal/JDS/article/1329/info)\]

## Installation

Installation of `scikit-sparse` depends on `suite-sparse` library, which can be installed via:
```bash
# mac
brew install suite-sparse

# debian
sudo apt-get install libsuitesparse-dev
```

Then install FROSTY from PyPI:
```bash
pip install frosty
```

## Example (scale-free graph, p=50, n=1000)

 - True and estimated graphs

![estimation](https://github.com/joshuaybang/frosty/raw/main/examples/images/frosty-estimation.png)

 - Confusion matrix

![confusion matrix](https://github.com/joshuaybang/frosty/raw/main/examples/images/confusion-matrix.png)