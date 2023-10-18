## liara/sdk

The liara sdk, with Python language for client that utilizes fetch-api.

## Requirements

Python 3.7+

### Development

#### Note: You must have Node and NPM, Docker, Docker Compose and Python installed on the system.

#### First, clone the project with the following command:
```
git clone https://github.com/liara-cloud/python-sdk.git
```
#### Installing requirements
```
python -m venv .venv
source .venv/bin/activate 
which python
pip install -r requirements.txt
```

#### Then run one of the following commands depending on your operating system:

_windows:_

```
./bin/cmd/generate.cmd && ./bin/cmd/doc.cmd && ./bin/cmd/remove-files.cmd && ./bin/cmd/init.cmd
```
```
cd ./bin/template/docs
npm install
npm run start
```
_Linux/Mac:_

```
./bin/bash/generate.sh && ./bin/bash/doc.sh && ./bin/bash/remove-files.sh && ./bin/bash/init.sh
```
```
cd ./bin/template/docs
npm install
npm run start
```
### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py bdist_wheel install --user
```
(or `sudo python setup.py install` to install the package for all users)

### Tests

Execute `pytest` to run the tests.

### Publish new version

#### PyPi 
```
pip install twine
twine upload dist/*
```

## Installation & Usage
### pip install

install with pip:

```sh
pip liara/sdk
```

Then import the package:
```python
import paas.openapi_client
import dbaas.openapi_client
import mail.openapi_client
import dns.openapi_client
import object_storage.openapi_client
```

### Documentation of all methods:

[Openapi documentation link](https://openapi.liara.ir/)

#### [DNS](./doc/dns/README.md)
#### [Mail](./doc/mail/README.md)
#### [PaaS](./doc/paas/README.md)
#### [DBaaS](./doc/dbaas/README.md)
#### [Object Storage](./doc/object_storage/README.md)