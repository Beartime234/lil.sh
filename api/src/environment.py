import os
import logging
import sys
from dataclasses import dataclass

log = logging.getLogger(__name__)


def get_from_env(key: str) -> str:
    """Gets a value from the environment

    Args:
        key: The key for the environment variable

    Returns:
        The value of the environment variable as a string
    """
    try:
        value = os.environ[key]
    except KeyError:
        log.error(f"Missing environment variable {key}")
        sys.exit(1)
    return value


@dataclass(frozen=True)
class Env:
    bucket_name: str
    key_prefix: str

    def __str__(self) -> str:
        return f"BucketName: {self.bucket_name}, KeyPrefix: {self.key_prefix}"


ENV_KEYS = Env(bucket_name="BUCKET_NAME", key_prefix="KEY_PREFIX")
