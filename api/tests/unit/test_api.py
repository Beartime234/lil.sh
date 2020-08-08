import json

import pytest

from api.src.api import BaseApiResponse, FunctionApiResponse, InternalErrorApiResponse, ApiEvent, BaseApiFunction
from api.tests.unit.test_environment import env


@pytest.fixture(scope="class")
def api_event():
    return ApiEvent({
        "path": "/v1/something",
        "resource": "something",
        "httpMethod": "GET",
        "headers": {"User-Agent": "myawesomebrowser"},
        "queryStringParameters": None,
        "body": json.dumps({})
    })


@pytest.fixture(scope="class")
def base_api_response():
    return BaseApiResponse(
        status_code=200,
        body={"dog": "boi"}
    )


@pytest.fixture(scope="class")
def function_api_response():
    return FunctionApiResponse(
        body={"dog": "boi"},
        status_code=200
    )


@pytest.fixture(scope="class")
def internal_error_api_response():
    return InternalErrorApiResponse("damn")


@pytest.fixture(scope="class")
def base_api_function():
    return InternalErrorApiResponse("damn")


@pytest.fixture(scope="class")
def base_api_function(api_event, env):
    return BaseApiFunction(api_event, env)


class TestApiEvent:

    def test_attributes(self, api_event: ApiEvent):
        assert api_event.path == "/v1/something"
        assert api_event.http_method == "GET"
        assert api_event.resource == "something"
        assert api_event.headers == {"User-Agent": "myawesomebrowser"}
        assert api_event.query_string_params == {}


class TestBaseApiResponse:

    def test___init__(self, base_api_response: BaseApiResponse):
        assert base_api_response.status_code == 200
        assert base_api_response.body == {"dog": "boi"}
        assert base_api_response.headers == {}
        assert base_api_response.is_base_64_encoded is False

    def test_as_dict(self, base_api_response: BaseApiResponse):
        base_api_response_as_dict = base_api_response.as_dict
        assert base_api_response_as_dict["statusCode"] == 200
        assert base_api_response_as_dict["body"] == '{"dog": "boi"}'
        assert base_api_response_as_dict["headers"] == {}
        assert base_api_response_as_dict["isBase64Encoded"] is False


class TestFunctionApiResponse:

    def test___init__(self, function_api_response: FunctionApiResponse):
        assert function_api_response.status_code == 200
        assert function_api_response.body == {"dog": "boi"}
        assert function_api_response.headers == {}
        assert function_api_response.is_base_64_encoded is False

    def test_as_dict(self, function_api_response: FunctionApiResponse):
        function_api_response_as_dict = function_api_response.as_dict
        assert function_api_response_as_dict["statusCode"] == 200
        assert function_api_response_as_dict["body"] == '{"dog": "boi"}'
        assert function_api_response_as_dict["headers"] == {}
        assert function_api_response_as_dict["isBase64Encoded"] is False


class TestInternalErrorApiResponse:

    def test___init__(self, internal_error_api_response: InternalErrorApiResponse):
        assert internal_error_api_response.status_code == 500
        assert internal_error_api_response.body == {"errorMessage": "damn"}
        assert internal_error_api_response.headers == {}
        assert internal_error_api_response.is_base_64_encoded is False

    def test_as_dict(self, internal_error_api_response: InternalErrorApiResponse):
        internal_error_api_response_as_dict = internal_error_api_response.as_dict
        assert internal_error_api_response_as_dict["statusCode"] == 500
        assert internal_error_api_response_as_dict["body"] == '{"errorMessage": "damn"}'
        assert internal_error_api_response_as_dict["headers"] == {}
        assert internal_error_api_response_as_dict["isBase64Encoded"] is False


class TestApiFunction:

    def test___init__(self, api_event: ApiEvent, base_api_function: BaseApiFunction):
        assert base_api_function.api_event == api_event

    def test_run(self, base_api_function: BaseApiFunction):
        with pytest.raises(NotImplementedError):
            base_api_function.run()
