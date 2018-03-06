# Python Interview Challenge

This project is the dead simple beginnings of an application back-end. The `master` branch is fairly barebones and includes just:

- `db.py` a very simple mock database access layer, including mock database content
- `transaction.py` a very simple python model of a transaction

## Challenge

A junior developer was asked to build the initial Account features, including the ability to view a list of transactions. They've done the work and opened a [pull request](https://github.com/jprestel-rue/python-interview/pull/1).

Your task is to review the pull request. Please provide suggestions for improvements and short pieces of replacement code, as appropriate.

## Running locally

The code in this project can be run locally with relatively little setup.

### Pre-requisites

- Python 2.7.x
  - On Mac: Recommend installing `python@2` via homebrew. Pay attention to the caveats to get the executable on your path.
- Optional: virtualenv
    - Highly recommend that you install `virtualenv` as to not impact your global python install

### Installation

- git clone this repo
- in a terminal, cd into your clone
- create a python virtualenv for this project and activate it
- pip install this package in editable mode with the `test` extras:
    ```shell
    pip install -e .[test]
    ```

### Checkout the pull-request branch

the master branch is pretty boring, so you'll want to checkout the feature branch created by the junior dev.
    ```shell
    git checkout feature/account
    ```

### Execute the tests

This project uses `pytest` with the `pytest-sugar` plug-in to make test output a little prettier.

```shell
pytest
```
