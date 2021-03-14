"""Test client."""
#

from subprocess import Popen
from time import sleep

from logzero import logger

from deepl_grpc.deepl_client import DeeplClient


def test_client_zh():
    Popen("pythonw -m deepl_grpc.deepl_server", shell=True)

    # wait for server to come up if newly started
    sleep(4)

    client = DeeplClient()

    result = client.get_url(message="t")

    text = "test this and that"
    result = client.get_url(message=text)
    assert "试" in result.message

    # need to refresh when switching to_lang
    result = client.get_url(message="text", to_lang="de")

    result = client.get_url(message=text, to_lang="de")
    logger.info("translation (de): %s", result.message)
    assert "und" in result.message.lower()


def test_client_de():
    Popen("pythonw -m deepl_grpc.deepl_server", shell=True)

    # wait for server to come up if newly started
    sleep(4)

    client = DeeplClient()

    # need to refresh when switching to_lang
    result = client.get_url(message="text", to_lang="de")

    text = "test this and that"
    result = client.get_url(message=text, to_lang="de")
    logger.info("translation (de): %s", result.message)
    assert "und" in result.message.lower()
