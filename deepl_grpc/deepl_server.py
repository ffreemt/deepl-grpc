"""Grpc server aio."""
#

from typing import Optional

import asyncio

from signal import signal, SIGINT, SIG_DFL

# import logzero
from logzero import logger
import portalocker

# only run one instance
file = open(f"{__file__}.portalocker.lock", "r+")
try:
    portalocker.lock(file, portalocker.constants.LOCK_EX)
except Exception as exc:
    logger.debug(exc)
    logger.info("Another copy is running, exiting...")
    raise SystemExit(1)

import grpc

from grpc_reflection.v1alpha import reflection  # noqa: E402

from deepl_scraper_pp.deepl_tr import deepl_tr

# from deepl_grpc import __version__
import deepl_grpc.deepl_pb2_grpc as pb2_grpc
import deepl_grpc.deepl_pb2 as pb2

# import unary_pb2_grpc as pb2_grpc
# import unary_pb2 as pb2

signal(SIGINT, SIG_DFL)
print("ctrl-C to interrupt")


class DeeplService(pb2_grpc.DeeplServicer):  # pylint: disable=too-few-public-methods
    """Deepl."""

    def __init__(self, *args, **kwargs):
        pass

    # def GetServerResponse(self, request, context):
    async def GetServerResponse(self, request, context):

        # get the string from the incoming request
        # message = request.message

        msg_fields = ["message", "from_lang", "to_lang"]
        message = dict((elm, getattr(request, elm)) for elm in msg_fields)

        logger.debug("request: %s", request)
        logger.debug("Received: %s", message)

        text = request.message
        from_lang = request.from_lang
        to_lang = request.to_lang
        if not from_lang:
            from_lang = "auto"
        if not to_lang:
            to_lang = "zh"

        try:
            trtext = await deepl_tr(text, from_lang, to_lang)
            received = True
        except Exception as exc:
            logger.error(exc)
            trtext = str(exc)
            received = False
        result = {
            "message": trtext,
            "received": received,
        }

        # result = f'Hello I am up and running received "{message}" message from you'
        # result = {"message": result, "received": True}

        return pb2.MessageResponse(**result)


# fmt: off
async def serve(
        host: Optional[str] = None,
        port: int = 50051,
):
    # fmt: on
    """Serve."""
    # server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    server = grpc.aio.server()
    pb2_grpc.add_DeeplServicer_to_server(DeeplService(), server)

    service_names = (
        pb2.DESCRIPTOR.services_by_name['Deepl'].full_name,
        reflection.SERVICE_NAME,
    )
    reflection.enable_server_reflection(service_names, server)

    # server.add_insecure_port('[::]:50051')
    try:
        if host is None:
            # server.add_insecure_port(f"[::]:{port}")
            host = "::1"
        server.add_insecure_port(f"[{host}]:{port}")
    except Exception as exc:
        logger.error(exc)
        raise SystemExit(1)

    await server.start()
    # print(f" running at [::]:{port}")
    logger.info(f" running at [{host}]:{port}")

    try:
        await server.wait_for_termination()
    except Exception as exc:  # signal no longer needed?
        logger.info("Interrupted")
        raise SystemExit(0) from exc


if __name__ == "__main__":
    import sys

    loop = asyncio.get_event_loop()

    port = 50051
    if len(sys.argv) > 2:
        try:
            port = int(sys.argv[2])
        except Exception:
            port = 50051

    host = "::1"
    host = "::"
    if len(sys.argv) > 1:
        host = sys.argv[1]

    try:
        loop.run_until_complete(serve(host, port))
    except Exception as exc:
        logger.error(exc)
    finally:
        loop.close()
