"""Deepl client."""
#

import grpc

import deepl_grpc.deepl_pb2_grpc as pb2_grpc
import deepl_grpc.deepl_pb2 as pb2

from logzero import logger

# start server if not already started
from subprocess import Popen

try:
    Popen(["pythonw", "deepl_server.py"], shell=True)
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

        logger.debug("message: %s", message)

        return self.stub.GetServerResponse(message)


if __name__ == "__main__":
    import sys

    client = DeeplClient()

    to_lang = "zh"
    if len(sys.argv) > 1:
        to_lang = sys.argv[1]

    print(
        " Default destination language: zh. "
        "Howere, you can supply to any of English (en), German (de), French (fr), Spanish (es), Portuguese (pt), Dutch (nl), Italian (it), Polish (pl), Russian (ru), Japanese (ja), and Chinese (zh) as the second argment, e.g., python deepl_grpc/deepl_client.py de"
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
