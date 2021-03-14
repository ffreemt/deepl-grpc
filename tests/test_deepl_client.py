"""Test client."""
#

from subprocess import Popen
from time import sleep

from logzero import logger

from deepl_grpc.deepl_client import DeeplClient


def test_client_zh():
    # Popen("pythonw -m deepl_grpc.deepl_server", shell=True)

    # wait for server to come up if newly started
    # sleep(14)

    client = DeeplClient()

    try:
        result = client.get_url(message="t")
    except Exception as exc:
        logger.error(exc)
        sleep(120)  # github vm needs to download chrominium

    text = "test this and that"
    try:
        result = client.get_url(message=text)
        res = result.message
    except Exception as exc:
        logger.error(exc)
        res = ""
    assert "试" in res

    _ = """
    # need to refresh when switching to_lang
    result = client.get_url(message="text", to_lang="de")

    result = client.get_url(message=text, to_lang="de")
    logger.info("translation (de): %s", result.message)
    assert "und" in result.message.lower()
    # """


def test_client_de():
    # Popen("pythonw -m deepl_grpc.deepl_server", shell=True)

    # wait for server to come up if newly started
    # sleep(14)

    client = DeeplClient()

    # need to refresh when switching to_lang
    result = client.get_url(message="text", to_lang="de")

    text = "test this and that"
    result = client.get_url(message=text, to_lang="de")
    logger.info("translation (de): %s", result.message)
    assert "und" in result.message.lower()
