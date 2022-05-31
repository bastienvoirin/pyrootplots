[![Documentation Status](https://readthedocs.org/projects/pyrootplots/badge/?version=latest)](https://pyrootplots.readthedocs.io/en/latest/?badge=latest) [![GitHub last commit](https://img.shields.io/github/last-commit/bastienvoirin/pyrootplots)](https://github.com/bastienvoirin/pyrootplots/commits) [![GitHub repo size](https://img.shields.io/github/repo-size/bastienvoirin/pyrootplots)](https://github.com/bastienvoirin/pyrootplots)

## pyrootplots

### License

[This project is licensed under the terms of the MIT license.](https://github.com/bastienvoirin/pyrootplots/blob/main/LICENSE.md)

### Documentation

See https://pyrootplots.readthedocs.io/en/latest/.

### Package installation

```shell
git clone https://github.com/bastienvoirin/pyrootplots
pip install --user .
```

### Usage

```python
from pyrootplots import *
```

### Development

Setting up the environment:

```shell
conda env create -f environment.yml
conda activate pyrootplots
```

Editing:

```shell
cd src/pyrootplots
```

Building the docs (the HTML pages are in `docs/_build/html`):

```shell
cd docs
make html
```

