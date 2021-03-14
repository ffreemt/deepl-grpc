# deepl-grpc
[![tests](https://github.com/ffreemt/deepl-grpc/actions/workflows/routine-tests.yml/badge.svg)][![python](https://img.shields.io/static/v1?label=python+&message=3.7%2B&color=blue)](https://img.shields.io/static/v1?label=python+&message=3.7%2B&color=blue)[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)[![PyPI version](https://badge.fury.io/py/deepl-grpc.svg)](https://badge.fury.io/py/deepl-grpc)

deepl grpc, server and client, cross platform (Windows/MacOS/Linux)

## Installation
*   Install ``grpc-reflection``
    *   ``grpc-reflection`` cannot be installed using `poetry add`. Use ``pip install grpc-reflection`` instead.
*   Install the rest as usual
```bash
pip install deepl-grpc
```
or
```bash
poetry add deepl-grpc
```

or clone the repo (`git clone https://github.com/ffreemt/deepl-grpc.git`) and install from it. For example
```python
git clone https://github.com/ffreemt/deepl-grpc.git
cd deepl-grpc
python3 -m venv .venv  # require python3.7
source .venv/bin/activate  # or .venv\Scripts\activate
pip install -r requirements.txt

python -m deepl_grpc.deepl_client

```

## Usage

### Interactive

*   [Optional] Start the grpc server
```python
python -m deepl_grpc.deepl_server
```

*   Start the client
```python
python -m deepl_grpc.deepl_client  # to chinese

# python -m deepl_grpc.deepl_client de  # to german
```

### WebUI
Download `grpcui` and run, for example in Windows
```bash
grpcui.exe -plaintext 127.0.0.1:50051
```
to explore the server in the same manner as Postman for REST.

### More coming soon
