# Toy Python package for DSCI 310 Individual Assignment 5.

## Install locally

```bash
pip install -e .
```

## Run tests

```bash
pytest
```

## Build distribution files

```bash
python -m build
```

## Upload to TestPyPI

```bash
python -m twine upload --repository testpypi dist/*
```
