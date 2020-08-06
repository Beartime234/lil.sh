import json


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

    def __init__(self, body: dict):
        super().__init__(200, body)


class InternalErrorApiResponse(BaseApiResponse):
    """This is the proper response for an internal error
    """

    def __init__(self, error_message: str):
        super().__init__(500, {"errorMessage": error_message})


class ApiFunction:

    def __init__(self):
        pass

    def run(self) -> FunctionApiResponse:
        return FunctionApiResponse({"cool": "yes"})
