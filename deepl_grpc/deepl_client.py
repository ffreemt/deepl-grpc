"""Deepl client."""
#

import os
import sys
from pathlib import Path
import grpc

import deepl_grpc.deepl_pb2_grpc as pb2_grpc
import deepl_grpc.deepl_pb2 as pb2

from logzero import logger

# start server if not already started
import subprocess
from subprocess import Popen

cwd = Path(__file__).absolute().parent.as_posix()
server_file = f"{cwd}/deepl_server.py"
if os.name in ["posix"]:  # linux and friends
    cmd = f"nohup python {server_file} > {cwd}" "/server.out 2>&1 &"
    subprocess.Popen(cmd, shell=True)
    logger.info(
        "grpc server running in background, output logged to: %s/server.out", cwd,
    )
else:
    try:
        Popen(f"pythonw {server_file}", shell=True)
        logger.info("\n\t [%s] grpc server running in background\n", server_file)
    except Exception as exc:
        logger.debug(exc)


class DeeplClient(object):
    """Client for gRPC functionality."""

    def __init__(self, host="127.0.0.1", server_port=50051):
        # self.host = "localhost"
        # self.server_port = 50051
        self.host = host
        self.server_port = server_port

        # instantiate a channel
        self.channel = grpc.insecure_channel(
            "{}:{}".format(self.host, self.server_port)
        )

        # bind the client and the server
        self.stub = pb2_grpc.DeeplStub(self.channel)

    def get_url(self, message, from_lang="auto", to_lang="zh"):
        """Client function to call the rpc for GetServerResponse."""
        message = pb2.Message(message=message, from_lang=from_lang, to_lang=to_lang,)

        logger.debug("message.message: %s", message.message)

        return self.stub.GetServerResponse(message)


if __name__ == "__main__":
    client = DeeplClient()

    to_lang = "zh"
    if len(sys.argv) > 1:
        to_lang = sys.argv[1]

    print(
        " Default destination language: zh. "
        "However, you can supply as the additional argument any of English (en), German (de), French (fr), Spanish (es), Portuguese (pt), Dutch (nl), Italian (it), Polish (pl), Russian (ru), Japanese (ja), and Chinese (zh), e.g., python deepl_grpc/deepl_client.py de or python -m deepl_grpc.deepl_client de"
    )
    print("")

    message = ""
    # for elm in range(1):
    while True:
        message = input(
            " Type something to translate (quit  or ctrl-C to exit): "
        ).strip()
        if not message:
            continue
        if message[:4].lower() in ["quit"]:
            break

        try:
            result = client.get_url(message=message, to_lang=to_lang,)
            # print(f"{elm}: {result}", result.message)
            print(message, "->", result.message)
        except Exception as exc:
            logger.error(exc)
