import logging

from api.src.api import BaseApiFunction, FunctionApiResponse, ApiEvent, FunctionApiResponseInvalidBadRequest, \
    FunctionApiResponseSuccessful
from api.src.environment import Env
from api.src.shortener import Shortener

log = logging.getLogger(__name__)


class CheckApiFunction(BaseApiFunction):

    def __init__(self, api_event: ApiEvent, env: Env):
        self.shortener = Shortener(env)
        self.suffix = api_event.query_string_params.get("suffix", None)
        super().__init__(api_event, env)

    def run(self) -> FunctionApiResponse:
        if self.suffix is None:
            return FunctionApiResponseInvalidBadRequest("suffix query string param missing")

        suffix_exists = self.shortener.does_suffix_exist(self.suffix)
        return FunctionApiResponseSuccessful(
            {"exists": suffix_exists}
        )
