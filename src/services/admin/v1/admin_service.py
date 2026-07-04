from archipy.models.errors import NotFoundError
from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends, Query
from uuid import UUID

from src.configs.containers import ServiceContainer
from src.logics.admin.admin_logic import AdminLogic
from src.models.dtos.admin.domain.v1.admin_domain_interface_dtos import (
    CreateAdminInputDTOV1, CreateAdminOutputDTOV1, CreateAdminRestInputDTOV1, DeleteAdminInputDTOV1, GetAdminInputDTOV1, GetAdminOutputDTOV1, SearchAdminInputDTOV1, SearchAdminOutputDTOV1, UpdateAdminInputDTOV1, UpdateAdminRestInputDTOV1
)
from src.models.types.api_router_type import ApiRouterType
from src.utils.utils import Utils

routerV1: APIRouter = APIRouter(tags=[ApiRouterType.ADMIN])



@routerV1.post(
    path="/{user_uuid}/admins",
    response_model=CreateAdminOutputDTOV1,
)
@inject
async def create_admin(
    user_uuid: UUID,
    input_dto: CreateAdminRestInputDTOV1,
    logic: AdminLogic = Depends(Provide[ServiceContainer.admin_logic]),
) -> CreateAdminOutputDTOV1:
    input_dto = CreateAdminInputDTOV1.create(user_uuid=user_uuid, input_dto=input_dto)
    return await logic.create_admin(input_dto=input_dto)


@routerV1.get(
    path="/{user_uuid}/admins/{admin_uuid}",
    response_model=GetAdminOutputDTOV1,
    responses=Utils.get_fastapi_exception_responses([NotFoundError]),
)
@inject
async def get_admin(
    user_uuid: UUID,
    admin_uuid: UUID,
    logic: AdminLogic = Depends(Provide[ServiceContainer.admin_logic]),
) -> GetAdminOutputDTOV1:
    input_dto = GetAdminInputDTOV1(admin_uuid=admin_uuid)
    return await logic.get_admin(input_dto=input_dto)


@routerV1.get(
    path="/{user_uuid}/admins",
    response_model=SearchAdminOutputDTOV1,
)
@inject
async def search_admins(
    user_uuid: UUID,
    page: int = Query(default=1, ge=1, description="Page number"),
    page_size: int = Query(default=10, ge=1, le=100, description="Number of items per page"),
    logic: AdminLogic = Depends(Provide[ServiceContainer.admin_logic]),
) -> SearchAdminOutputDTOV1:
    input_dto = SearchAdminInputDTOV1.create(
        page=page,
        page_size=page_size,
    )
    return await logic.search_admins(input_dto=input_dto)


@routerV1.put(
    path="/{user_uuid}/admins/{admin_uuid}",
)
@inject
async def update_admin(
    user_uuid: UUID,
    admin_uuid: UUID,
    input_dto: UpdateAdminRestInputDTOV1,
    logic: AdminLogic = Depends(Provide[ServiceContainer.admin_logic]),
) -> None:
    update_dto = UpdateAdminInputDTOV1(**input_dto.model_dump(), admin_uuid=admin_uuid)
    await logic.update_admin(input_dto=update_dto)


@routerV1.delete(
    path="/{user_uuid}/admins/{admin_uuid}",
)
@inject
async def delete_admin(
    user_uuid: UUID,
    admin_uuid: UUID,
    logic: AdminLogic = Depends(Provide[ServiceContainer.admin_logic]),
) -> None:
    input_dto = DeleteAdminInputDTOV1(admin_uuid=admin_uuid)
    await logic.delete_admin(input_dto=input_dto)

