from fastapi.responses import Response

from ..types import (
    MetadataModelResponse,
    MetadataServerResponse,
    InferenceRequest,
    InferenceResponse,
    RepositoryIndexRequest,
    RepositoryIndexResponse,
)
from ..handlers import DataPlane, ModelRepositoryHandlers

from .utils import to_status_code


class Endpoints:
    """
    Implementation of REST endpoints.
    These take care of the REST/HTTP-specific things and then delegate the
    business logic to the internal handlers.
    """

    def __init__(self, data_plane: DataPlane):
        self._data_plane = data_plane

    async def live(self) -> Response:
        is_live = await self._data_plane.live()
        return Response(status_code=to_status_code(is_live))

    async def ready(self) -> Response:
        is_ready = await self._data_plane.ready()
        return Response(status_code=to_status_code(is_ready))

    async def model_ready(self, model_name: str) -> Response:
        is_ready = await self._data_plane.model_ready(model_name)
        return Response(status_code=to_status_code(is_ready))

    async def metadata(self) -> MetadataServerResponse:
        return await self._data_plane.metadata()

    async def model_metadata(
        self, model_name: str
    ) -> MetadataModelResponse:
        return await self._data_plane.model_metadata(model_name)

    async def infer(
        self,
        payload: InferenceRequest,
        model_name: str
    ) -> InferenceResponse:
        return await self._data_plane.infer(payload, model_name)


class ModelRepositoryEndpoints:
    def __init__(self, handlers: ModelRepositoryHandlers):
        self._handlers = handlers

    async def index(self, payload: RepositoryIndexRequest) -> RepositoryIndexResponse:
        return await self._handlers.index(payload)

    async def load(self, model_name: str) -> Response:
        loaded = await self._handlers.load(name=model_name)
        return Response(status_code=to_status_code(loaded))

    async def unload(self, model_name: str) -> Response:
        unloaded = await self._handlers.unload(name=model_name)
        return Response(status_code=to_status_code(unloaded))
