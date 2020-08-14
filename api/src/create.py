import re

from api.src.api import BaseApiFunction, ApiEvent, FunctionApiResponse, FunctionApiResponseInvalidBadRequest, \
    FunctionApiResponseSuccessful
from api.src.environment import Env
from api.src.exceptions import SuffixAlreadyExists
from api.src.shortener import Shortener

from urllib.parse import urlparse

INVALID_SUFFIXES = ["base.redirect"]


class CreateApiFunction(BaseApiFunction):

    def __init__(self, api_event: ApiEvent, env: Env):
        self.shortener = Shortener(env)
        self.suffix = api_event.body.get("suffix", None)
        self.redirect_location = api_event.body.get("redirectLocation", None)
        super().__init__(api_event, env)

    def run(self) -> FunctionApiResponse:
        """Main Logic

        Returns:
            The applicable function api response
        """

        if self.redirect_location is None:
            return FunctionApiResponseInvalidBadRequest("redirectLocation body param missing")

        if self._is_redirect_location_a_valid_url() is False:
            return FunctionApiResponseInvalidBadRequest("Not a valid URL. Must start with http:// or https://")

        if self.suffix is not None:
            if self._is_suffix_valid() is False:
                return FunctionApiResponseInvalidBadRequest("Not a valid suffix must include only characters and /~._-")

        try:
            new_url = self.shortener.add_new_url(self.redirect_location, self.suffix)
        except SuffixAlreadyExists:
            return FunctionApiResponseInvalidBadRequest("Suffix already exists")

        return FunctionApiResponseSuccessful({"newUrl": new_url})

    def _is_redirect_location_a_valid_url(self) -> bool:
        """This ensures that this is a valid URL

        Returns:
            True if its a valid url otherwise returns invalid
        """
        redirect_location_parse = urlparse(self.redirect_location)

        if redirect_location_parse.netloc == "" and redirect_location_parse.scheme == "":
            return False

        return True

    def _is_suffix_valid(self) -> bool:
        """Checks if a suffix is a valid name

        Returns:
            If the suffix is valid
        """
        if self.suffix in INVALID_SUFFIXES:
            return False
        return bool(re.match(r'^[a-zA-Z/~._-]+$', self.suffix))
