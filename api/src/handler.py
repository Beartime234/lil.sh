import logging

from api.src.api import BaseApiResponse, InternalErrorApiResponse, ApiEvent
from api.src.check import CheckApiFunction
from api.src.create import CreateApiFunction
from api.src.environment import Environment

from api.src.environment import ENV_KEYS

CHECK_RESOURCE = "/check"
CREATE_RESOURCE = "/create"

log = logging.getLogger(__name__)


def map_function(api_event: ApiEvent, environment: Environment) -> BaseApiResponse:
    if api_event.http_method == "GET":
        if api_event.resource == CHECK_RESOURCE:
            log.debug(f"Event maps to method GET. resource {CHECK_RESOURCE}")
            return CheckApiFunction(api_event).run()

    if api_event.http_method == "POST":
        if api_event.resource == CREATE_RESOURCE:
            log.debug(f"Event maps to method POST, resource {CREATE_RESOURCE}")
            return CreateApiFunction(api_event).run()

    return InternalErrorApiResponse(f"No function for the path {api_event.path} for method {api_event.http_method}")


def lambda_handler(event: dict, context: dict):
    log.debug(f"Raw Event: {event}")

    # Create the Api Event object
    api_event = ApiEvent(
        path=event.get("path"),
        resource=event.get("resource"),
        http_method=event.get("httpMethod"),
        headers=event.get("headers"),
        # If there are no query string params we dont want it to be None
        query_string_params=event.get("queryStringParameters", {})
    )

    # Loading environment
    environment = Environment(
        bucket_name=ENV_KEYS.bucket_name,
        key_prefix=ENV_KEYS.key_prefix
    )

    log.info(f"Event: {api_event}, Environment: {environment}")

    response = map_function(api_event, environment)

    return response.as_dict
