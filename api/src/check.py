import boto3

from api.src.api import BaseApiFunction, FunctionApiResponse, ApiEvent, FunctionApiResponseInvalidBadRequest, \
    FunctionApiResponseSuccessful


class CheckApiFunction(BaseApiFunction):

    def __init__(self, api_event: ApiEvent):
        self.s3_client = boto3.client("s3")
        self.suffix = api_event.query_string_params.get("suffix", None)
        super().__init__(api_event)

    def run(self) -> FunctionApiResponse:
        if self.suffix is None:
            return FunctionApiResponseInvalidBadRequest("Suffix query string param missing")

        suffix_exists = self._does_suffix_exist()
        return FunctionApiResponseSuccessful({"exists": suffix_exists})

    def _does_suffix_exist(self) -> bool:
        response = self.s3_client.head_object(
            Bucket='string',
            Key='string',
        )
        return True
