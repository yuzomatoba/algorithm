## <img src="https://github.com/yuzomatoba/algorithm/assets/108953241/d6aec771-91a5-45d6-be7e-9b233c8236de" alt="image" width="30" height="30">Algorithm First Experience Project<img src="https://github.com/yuzomatoba/algorithm/assets/108953241/d6aec771-91a5-45d6-be7e-9b233c8236de" alt="image" width="30" height="30">





The project aimed to:
- Build search and sorting algorithms
- Apply recursion and iteration
- Perform testing

## Programming Language:
- Python


## Installation

🤖 Required commands (before starting the project):

Creating a virtual environment for the project:

* `python3 -m venv .venv && source .venv/bin/activate`

Installing the dependencies:

* `python3 -m pip install -r dev-requirements.txt`


❗️ Note: 
The dev-requirements.txt file contains all the dependencies that have been used in the project, acting as a package.json file in a Node.js project. ❗️


## Python Version:

The Python version used in this project was 3.10.6.

You can use a specific version by using the command `pyenv local 3.x.y` (directory version) or `pyenv global 3.x.y` (global version).

## Python Test:

Running the tests:

```bash
  python3 -m pytest
  ```


The pyproject.toml file already configures pytest correctly. However, if you find any issues with it and want to explicitly get a complete output, the command is:

 ```bash
  python3 -m pytest -s -vv
  ```


If you need to run only one test file, simply execute the command:

  ```bash
  python3 -m pytest tests/file_name.py
  ```


If you need to run only one test function, simply execute the command:

  ```bash
  python3 -m pytest -k test_function_name
  ```


If you wish to run tests from a specific file, execute it with `-x filename`.

```bash
  python -m pytest -x tests/test_jobs.py
  ```


To run a specific test from a file, simply execute the command:

```bash
  python -m pytest -x tests/file_name.py::test_test_name
  ```

If you want to learn more about installing dependencies with pip, check out this [article](https://medium.com/python-pandemonium/better-python-dependency-and-package-management-b5d8ea29dff1).


