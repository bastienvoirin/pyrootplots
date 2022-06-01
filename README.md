### pyrootplots: ROOT files visualisation using Python

[![Documentation Status](https://readthedocs.org/projects/pyrootplots/badge/?version=latest)](https://pyrootplots.readthedocs.io/en/latest/?badge=latest) [![GitHub last commit](https://img.shields.io/github/last-commit/bastienvoirin/pyrootplots)](https://github.com/bastienvoirin/pyrootplots/commits) [![GitHub repo size](https://img.shields.io/github/repo-size/bastienvoirin/pyrootplots)](https://github.com/bastienvoirin/pyrootplots)

### License

[This project is licensed under the terms of the MIT license.](https://github.com/bastienvoirin/pyrootplots/blob/main/LICENSE.md)

### Documentation (:uk:)

See https://pyrootplots.readthedocs.io/en/latest/.

### Package installation

```shell
git clone https://github.com/bastienvoirin/pyrootplots
pip install --user .
```

### Usage

- Install `pyrootplots` (see Package installation)
- Set up the environment:
```shell
conda env create -f environment.yml
conda activate pyrootplots
```
- Import `pyrootplots` in your Python script:
```python
from pyrootplots import *
```

### Development

- Install `pyrootplots` (see Package installation)
- Set up the environment:
```shell
conda env create -f environment.yml
conda activate pyrootplots
```
- Develop:
```shell
cd src/pyrootplots
```
- Build the docs (the HTML pages are in `docs/_build/html`):
```shell
cd docs
make clean # optional
make html
```
- Commit
```shell
git add
git commit
git push
```
