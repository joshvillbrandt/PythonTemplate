# PythonTemplate

An example Python project.

## Setup

You must have Git, Python, and Pip already installed to use this project. Get the code like this:

```bash
git clone https://github.com/joshvillbrandt/PythonTemplate.git
cd PythonTemplate/
sudo python setup.py install
```

## Usage

The install step above installs `pytemplate` into your system. You should be able to call this directly from a shell:

```bash
pyscript
```

Add the `-h` flag to see full usage information:

```bash
```

## API

This package also provides the library `PythonTemplate`. The `pytemplate` script uses this internally, but you can also use the library directly from a Python project like this:

```python
from PythonTemplate import Model

Model.doThing()
```

The `PythonTemplate` library provides these functions:

* `Model.doThing()` - does a thing

## Tests

Run the test suite like this:

```bash
sudo tox
```

## Change Log

This project uses [semantic versioning](http://semver.org/).

### v0.1.0 - 2014/08/20

* Initial release of the Python template
