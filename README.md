# deepl-grpc
[![tests](https://github.com/ffreemt/deepl-grpc/actions/workflows/routine-tests.yml/badge.svg)][![python](https://img.shields.io/static/v1?label=python+&message=3.7%2B&color=blue)](https://img.shields.io/static/v1?label=python+&message=3.7%2B&color=blue)[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)[![PyPI version](https://badge.fury.io/py/deepl-grpc.svg)](https://badge.fury.io/py/deepl-grpc)

deepl grpc, server and client

## Usage

```python
from deepl_grpc.deepl_tr import deepl_tr

res = await deepl_tr("test me")
print(res)
# '考我 试探我 测试我 试探'

print(await deepl_tr("test me", to_lang="de"))