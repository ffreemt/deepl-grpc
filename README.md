# deepl-grpc
[![tests](https://github.com/ffreemt/deepl-grpc/actions/workflows/routine-tests.yml/badge.svg)][![python](https://img.shields.io/static/v1?label=python+&message=3.7%2B&color=blue)](https://img.shields.io/static/v1?label=python+&message=3.7%2B&color=blue)[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)[![PyPI version](https://badge.fury.io/py/deepl-grpc.svg)](https://badge.fury.io/py/deepl-grpc)

deepl grpc, server and client, cross platform (Windows/MacOS/Linux)

## Installation
*   Install ``grpcio-reflection``
    *   ``grpc-reflection`` cannot be installed using `poetry add`. Use ``pip install grpcio-reflection`` instead.
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
python3.8 -m venv .venv  # require python3.7+

# for Linux/MacOS, you'd need to install venv and dev if you haven't done so
# sudo apt install python3.8-venv
# sudo apt install python3.8-dev

source .venv/bin/activate  # or in Windows do: .venv\Scripts\activate

pip install grpcio-reflection

pip install -r requirements.txt
# or poetry install --no-dev

python -m deepl_grpc.deepl_client

```

## Usage

### `python` code
```python
from deepl_grpc.deepl_client import DeeplClient
from linetimer import CodeTimer

client = DeeplClient()

text = "test this and that"
with CodeTimer(unit="s"):
    result = client.get_url(message=text)
# Code block took: 1.99860 s

print(result.message)
# 试探 左右逢源 检验 审时度势

to_lang = "de"
with CodeTimer(unit="s"):
  result = client.get_url(message=text, to_lang=to_lang,)
# Code block took: 2.02847 s

print(result.message)
# "Testen Sie dieses und jenes a Testen Sie dies und das a testen Sie dies und das Testen Sie dieses und jenes"

```

### Interactive

*   Start the grpc server
```python
python -m deepl_grpc.deepl_server
```
The first run in Linux may take a while since `chromium` (~1G) needs to be downloaded. In Windows, Chrome will be used if it's available.

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

### pyppeteer issues in Linux
You may encounter the following error in Linux:

 **chromium/linux-588429/chrome-linux/chrome**: error while loading shared libraries: libX11-xcb.so.1: cannot open shared object file: No such file or directory

You may wish to try this fix in Ubuntu [https://medium.com/@cloverinks/how-to-fix-puppetteer-error-ibx11-xcb-so-1-on-ubuntu-152c336368](https://medium.com/@cloverinks/how-to-fix-puppetteer-error-ibx11-xcb-so-1-on-ubuntu-152c336368)
```bash
sudo apt-get install gconf-service libxext6 libxfixes3 libxi6 libxrandr2 libxrender1 libcairo2 libcups2 libdbus-1-3 libexpat1 libfontconfig1 libgcc1 libgconf-2-4 libgdk-pixbuf2.0-0 libglib2.0-0 libgtk-3-0 libnspr4 libpango-1.0-0 libpangocairo-1.0-0 libstdc++6 libx11-6 libx11-xcb1 libxcb1 libxcomposite1 libxcursor1 libxdamage1 libxss1 libxtst6 libappindicator1 libnss3 libasound2 libatk1.0-0 libc6 ca-certificates fonts-liberation lsb-release xdg-utils wget
```

### More coming soon

<!---
https://www.cnblogs.com/lsdb/p/12102418.html
17     # portalocker.lock(file, portalocker.constants.LOCK_EX)
18     portalocker.lock(file, portalocker.LOCK_EX | portalocker.LOCK_NB)

import sys
from pathlib import Path

_ = Path(__file__).absolute().parent.parent.as_posix()
sys.path.append(_)


workingDir = Path(__file__).absolute().parent.as_posix()

cmd = f"nohup python {workingDir}/deepl_server.py >/dev/null 2>&1 &"

fullpath = "/tmp"
cmd = f"nohup python {fullpath}/file.py > {fullpath}/out 2>&1 &"
subprocess.Popen(cmd, shell=True)

subprocess.Popen("pythonw file.py", shell=True)

--->