import os

import pytest

from api.src.environment import get_from_env, Env
from api.tests import test_bucket, test_prefix


@pytest.fixture(scope="class")
def env():
    return Env(
        bucket_name=test_bucket,
        key_prefix=test_prefix
    )


def test_get_from_env():
    os.environ["fun"] = "yes"
    assert get_from_env("fun") == "yes"


class TestEnv:

    def test___init__(self, env):
        assert env.bucket_name == "testbucket"
        assert env.key_prefix == "surl/"
