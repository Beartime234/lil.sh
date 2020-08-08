import json
from dataclasses import dataclass


@dataclass
class ApiEvent:
    """Class for accessing event information relevant to the API"""
    path: str
    resource: str
    http_method: str
    headers: dict
    query_string_params: dict

    def __str__(self):
        return f"Path: {self.path}, Resource: {self.resource}, " \
               f"HttpMethod: {self.http_method},  Headers: {self.headers}, " \
               f"QueryStringParams: {self.query_string_params}"


class BaseApiResponse:
    """Class for formulating a correctly formatted
    """
    status_code: int
    headers: dict
    body: dict
    is_base_64_encoded: bool

    def __init__(self, status_code: int, body: dict, is_base_64_encoded: bool = False):
        self.status_code: int = status_code
        self.headers: dict = {}
        self.body: dict = body
        self.is_base_64_encoded = is_base_64_encoded

    @property
    def as_dict(self):
        return {
            "isBase64Encoded": self.is_base_64_encoded,
            "statusCode": self.status_code,
            "headers": self.headers,
            "body": json.dumps(self.body)
        }


class FunctionApiResponse(BaseApiResponse):
    """An Api Response from a function
    """

    def __init__(self, status_code: int, body: dict):
        super().__init__(status_code, body)


class FunctionApiResponseSuccessful(FunctionApiResponse):

    def __init__(self, body: dict):
        super().__init__(200, body)


class FunctionApiResponseInvalidBadRequest(FunctionApiResponse):

    def __init__(self, error_message: str):
        super().__init__(400, {"errorMessage": error_message})


class InternalErrorApiResponse(BaseApiResponse):
    """This is the proper response for an internal error
    """

    def __init__(self, error_message: str):
        super().__init__(500, {"errorMessage": error_message})


class BaseApiFunction:

    def __init__(self, api_event: ApiEvent):
        self.api_event = api_event

    def run(self) -> FunctionApiResponse:
        raise NotImplementedError("Please implement this method.")
