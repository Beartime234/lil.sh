import os
import sys

from api.src.environment import ENV_KEYS

test_bucket = "testbucket"
test_prefix = "surl/"

if "pytest" in sys.modules:
    os.environ[ENV_KEYS.bucket_name] = test_bucket
    os.environ[ENV_KEYS.key_prefix] = test_prefix
