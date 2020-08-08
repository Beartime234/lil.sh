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
class Environment:
    bucket_name: str
    key_prefix: str

    def __str__(self) -> str:
        return str(dir(__builtins__))


ENV_KEYS = Environment(bucket_name="BUCKET_NAME", key_prefix="KEY_PREFIX")
