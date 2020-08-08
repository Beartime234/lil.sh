import random
import string
from typing import Optional

import boto3
import logging

from botocore.exceptions import ClientError

from api.src.environment import Env
from api.src.exceptions import SuffixAlreadyExists

log = logging.getLogger(__name__)


class Shortener:
    r_chars: list = string.ascii_lowercase + string.ascii_uppercase + "1234567890"

    def __init__(self, env: Env):
        self.env = env
        self.s3_client = boto3.client("s3")

    def does_suffix_exist(self, suffix: str) -> bool:
        """This checks if suffix already exists in the url shortening bucket

        Returns:
            True if the suffix already exists, False otherwise
        """
        key_path = self._generate_key_path_from_suffix(suffix)
        try:
            log.info(f"Checking if suffix {suffix} exists. Full Path {key_path}")
            self.s3_client.head_object(
                Bucket=self.env.bucket_name,
                Key=key_path,
            )
        except ClientError as client_exception:
            response_code = client_exception.response["Error"]["Code"]
            log.error(f"Exception was {client_exception}, ErrorCode: {response_code}")
            if response_code == "404":  # Not Found
                log.debug("Suffix does not exist")
                return False
            else:
                raise client_exception
        log.debug(f"Suffix does exist")
        return True

    def _generate_key_path_from_suffix(self, suffix: str) -> str:
        """Generates the key path from a suffix

        Args:
            suffix: The suffix you are generating from

        Returns:
            The key path as a string
        """
        key_path = f"{self.env.key_prefix}{suffix}"
        log.debug(f"Generated key path is {key_path}")
        return key_path

    def add_new_url(self, redirect_location: str, suffix: Optional[str]) -> str:
        """Adds a new url shortener

        Args:
            redirect_location: The redirect location for the url
            suffix: The suffix for the url

        Raises:
            SuffixAlreadyExists: If the suffix was not None and already exists

        Returns:
            The new url as a string
        """
        unique_suffix: bool = True
        suffix_length: int = 3

        if suffix is None:
            unique_suffix = False

        # We loop indefinitely until we put the new object
        while True:
            # We do this only if we generate a unique suffix
            if unique_suffix is False:
                suffix = self._generate_unique_suffix(suffix_length)

            key_path: str = self._generate_key_path_from_suffix(suffix)

            if self.does_suffix_exist(suffix) is True:
                if unique_suffix is True:
                    log.debug(f"Suffix was unique and already exists. Must raise error.")
                    raise SuffixAlreadyExists("Suffix already exists.")
                else:
                    log.debug(f"Suffix ({suffix}) was not unique. "
                              f"Will try to generate another.")
                    # We increase the suffix length to hopefully find a unique suffix this time
                    suffix_length += 1
                    if suffix_length > 14:  # This will force us to keep trying until we find a unique suffix
                        suffix_length = 3
                    continue

            log.info(f"Putting new object at path {key_path} with redirect location {redirect_location}")
            # Put the new url in the s3 bucket
            self.s3_client.put_object(
                Body=b'',  # empty object
                Bucket=self.env.bucket_name,
                Key=key_path,
                WebsiteRedirectLocation=redirect_location,
            )
            # Return the new url
            return self._generate_new_url(suffix)

    def _generate_new_url(self, suffix: str) -> str:
        """Generates the new url for sending back to the client

        Args:
            suffix: The suffix for the string

        Returns:
            The new url as a string
        """
        new_url = f"{self.env.bucket_name}/{suffix}"
        log.debug(f"New url: {new_url}")
        return new_url

    def _generate_unique_suffix(self, length: int) -> str:
        """Generates a unique suffix based on length

        Args:
            length: The length of the unique suffix

        Returns:
            A unique suffix
        """
        unique_suffix = ''.join(random.choice(self.r_chars) for x in range(length))
        log.debug(f"Generated unique suffix with length {length}: {unique_suffix}")
        return unique_suffix
