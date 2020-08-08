import logging

from api.src.api import BaseApiResponse, InternalErrorApiResponse, ApiEvent
from api.src.check import CheckApiFunction
from api.src.create import CreateApiFunction
from api.src.environment import Env, get_from_env

from api.src.environment import ENV_KEYS

CHECK_RESOURCE = "/check"
CREATE_RESOURCE = "/create"

log = logging.getLogger(__name__)


def map_function(api_event: ApiEvent, env: Env) -> BaseApiResponse:
    if api_event.http_method == "GET":
        log.debug(f"Event maps to method GET.")
        if api_event.resource == CHECK_RESOURCE:
            log.debug(f"Event maps to resource {CHECK_RESOURCE}")
            return CheckApiFunction(api_event, env).run()

    if api_event.http_method == "POST":
        log.debug(f"Event maps to method POST.")
        if api_event.resource == CREATE_RESOURCE:
            log.debug(f"Event maps to method resource {CREATE_RESOURCE}")
            return CreateApiFunction(api_event, env).run()

    return InternalErrorApiResponse(f"No function for the path {api_event.path} for method {api_event.http_method}")


def lambda_handler(event: dict, context: dict):
    log.debug(f"Raw Event: {event}")

    # Create the Api Event object
    api_event = ApiEvent(event)

    # Loading environment
    env = Env(
        bucket_name=get_from_env(ENV_KEYS.bucket_name),
        key_prefix=get_from_env(ENV_KEYS.key_prefix)
    )

    log.info(f"Event: {api_event}, Environment: {env}")

    response = map_function(api_event, env)

    return response.as_dict
