# PyUMLS
Python wrapper for UMLS REST API

## Installation

To install, clone to your machine and add the cloned directory to your PYTHONPATH environment variable.

E.g., if you cloned into `/home/someuser/PyUMLS`, you would add the following to your `.bashrc`:
```sh
PYTHONPATH=${PYTHONPATH}:/home/someuser/PyUMLS
```

You can then use `pyumls` in Python via `import pyumls` or `from pyumls import api`.

## Authentication

To use the UMLS REST API, you must have

- A [UTS](https://uts.nlm.nih.gov/home.html) account (sign up for one [here](https://uts.nlm.nih.gov//license.html))
- An API key associated with your account (you can find this by going to the "My Profile" page and looking for the field labeled "API KEY")

This API key must be passed as an argument to all API calls, using the `apikey` parameter.  E.g.,
```python
from pyumls import api
x = api.getByCUI('C0009443', apikey='<your API key>')
```
