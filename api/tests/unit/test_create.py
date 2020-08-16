import json

import pytest

from api.src.api import ApiEvent, FunctionApiResponse
from api.src.create import CreateApiFunction
from api.tests import test_bucket

# Fixture imports Pycharm won't recognise these
from api.src.exceptions import SuffixAlreadyExists
from api.tests.unit.test_environment import env
from api.tests.aws_mocks import aws_credentials, s3, surl_bucket


@pytest.fixture(scope="class")
def create_api_event_w_suffix():
    return ApiEvent({
        "path": "/v1/create",
        "resource": "create",
        "httpMethod": "POST",
        "headers": {},
        "queryStringParameters": {},
        "body": json.dumps({
            "suffix": "test",
            "redirectLocation": "https://google.com"
        })
    })


@pytest.fixture(scope="class")
def create_api_function_w_suffix(create_api_event_w_suffix, env):
    return CreateApiFunction(create_api_event_w_suffix, env)


class TestCreateApiFunctionWSuffix:

    def test___init__(self, create_api_function_w_suffix: CreateApiFunction):
        assert create_api_function_w_suffix.suffix == "test"
        assert create_api_function_w_suffix.redirect_location == "https://google.com"

    def test_run(self, create_api_function_w_suffix: CreateApiFunction, aws_credentials, s3, surl_bucket):
        res: FunctionApiResponse = create_api_function_w_suffix.run()
        assert res.status_code == 200
        assert res.body["newUrl"] == f"{test_bucket}/test"

        # Run twice we should get it already exists
        res: FunctionApiResponse = create_api_function_w_suffix.run()
        assert res.status_code == 400
        assert res.body["errorMessage"] == "Suffix already exists"

        create_api_function_w_suffix.redirect_location = None
        res: FunctionApiResponse = create_api_function_w_suffix.run()
        assert res.status_code == 400
        assert res.body["errorMessage"] == "redirectLocation body param missing"

    def test__is_redirect_location_a_valid_url(self, create_api_function_w_suffix: CreateApiFunction):
        assert create_api_function_w_suffix._is_redirect_location_a_valid_url() is True
        create_api_function_w_suffix.redirect_location = "dkdfdf"
        assert create_api_function_w_suffix._is_redirect_location_a_valid_url() is False

    def test__is_suffix_valid(self, create_api_function_w_suffix: CreateApiFunction):
        assert create_api_function_w_suffix._is_suffix_valid() is True
        create_api_function_w_suffix.suffix = "\'sneaky"
        assert create_api_function_w_suffix._is_suffix_valid() is False
        create_api_function_w_suffix.suffix = "base.redirect"
        assert create_api_function_w_suffix._is_suffix_valid() is False


@pytest.fixture(scope="class")
def create_api_event_w_out_suffix():
    return ApiEvent({
        "path": "/v1/create",
        "resource": "create",
        "httpMethod": "POST",
        "headers": {},
        "queryStringParameters": {},
        "body": json.dumps({
            "redirectLocation": "https://bing.com"
        })
    })


@pytest.fixture(scope="class")
def create_api_function_w_out_suffix(create_api_event_w_out_suffix, env):
    return CreateApiFunction(create_api_event_w_out_suffix, env)


class TestCreateApiFunctionWOutSuffix:

    def test___init__(self, create_api_function_w_out_suffix: CreateApiFunction):
        assert create_api_function_w_out_suffix.suffix is None
        assert create_api_function_w_out_suffix.redirect_location == "https://bing.com"
