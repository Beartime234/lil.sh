from api.src.api import BaseApiFunction, ApiEvent, FunctionApiResponse


class CreateApiFunction(BaseApiFunction):

    def __init__(self, api_event: ApiEvent):
        super().__init__(api_event)

    def run(self) -> FunctionApiResponse:
        pass
