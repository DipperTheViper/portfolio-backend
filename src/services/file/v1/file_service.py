from uuid import UUID

from archipy.models.errors import NotFoundError
from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends
from fastapi.responses import FileResponse

from src.configs.containers import ServiceContainer
from src.logics.file.file_logic import FileLogic
from src.models.dtos.file.domain.v1.file_domain_interface_dtos import (
    GetFileInputDTOV1,
    SearchFileOutputDTOV1,
)
from src.models.types.api_router_type import ApiRouterType
from src.utils.utils import Utils

routerV1: APIRouter = APIRouter(tags=[ApiRouterType.FILE])


@routerV1.get(
    path="/files",
    response_model=SearchFileOutputDTOV1,
)
@inject
async def search_files(
    logic: FileLogic = Depends(Provide[ServiceContainer.file_logic]),
) -> SearchFileOutputDTOV1:
    return await logic.search_files()


@routerV1.get(
    path="/files/{file_uuid}/download",
    responses=Utils.get_fastapi_exception_responses([NotFoundError]),
)
@inject
async def download_file(
    file_uuid: UUID,
    logic: FileLogic = Depends(Provide[ServiceContainer.file_logic]),
) -> FileResponse:
    full_path, file_name = await logic.get_download_target(input_dto=GetFileInputDTOV1(file_uuid=file_uuid))
    return FileResponse(path=full_path, filename=file_name)
