from uuid import UUID

from archipy.models.errors import NotFoundError
from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends

from src.configs.containers import ServiceContainer
from src.logics.admin.admin_logic import AdminLogic
from src.models.dtos.admin.domain.v1.admin_domain_interface_dtos import (
    GetAdminInputDTOV1,
    GetAdminOutputDTOV1,
    SearchAdminOutputDTOV1,
)
from src.models.types.api_router_type import ApiRouterType
from src.utils.utils import Utils

routerV1: APIRouter = APIRouter(tags=[ApiRouterType.ADMIN])


@routerV1.get(
    path="/admins/{admin_uuid}",
    response_model=GetAdminOutputDTOV1,
    responses=Utils.get_fastapi_exception_responses([NotFoundError]),
)
@inject
async def get_admin(
    admin_uuid: UUID,
    logic: AdminLogic = Depends(Provide[ServiceContainer.admin_logic]),
) -> GetAdminOutputDTOV1:
    input_dto = GetAdminInputDTOV1(admin_uuid=admin_uuid)
    return await logic.get_admin(input_dto=input_dto)


@routerV1.get(
    path="/admins",
    response_model=SearchAdminOutputDTOV1,
)
@inject
async def search_admins(
    logic: AdminLogic = Depends(Provide[ServiceContainer.admin_logic]),
) -> SearchAdminOutputDTOV1:
    return await logic.search_admins()
