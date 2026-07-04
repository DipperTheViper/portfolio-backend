from archipy.models.errors import NotFoundError
from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends, Query
from uuid import UUID

from src.configs.containers import ServiceContainer
from src.logics.contact.contact_logic import ContactLogic
from src.models.dtos.contact.domain.v1.contact_domain_interface_dtos import (
    CreateContactMessageInputDTOV1,
    CreateContactMessageOutputDTOV1,
    CreateContactMessageRestInputDTOV1,
    DeleteContactMessageInputDTOV1,
    GetContactMessageInputDTOV1,
    GetContactMessageOutputDTOV1,
    SearchContactMessageInputDTOV1,
    SearchContactMessageOutputDTOV1,
    UpdateContactMessageInputDTOV1,
    UpdateContactMessageRestInputDTOV1,
)
from src.models.types.api_router_type import ApiRouterType
from src.utils.utils import Utils

routerV1: APIRouter = APIRouter(tags=[ApiRouterType.CONTACT])


@routerV1.post(
    path="/{user_uuid}/contact-messages",
    response_model=CreateContactMessageOutputDTOV1,
)
@inject
async def create_contact_message(
    user_uuid: UUID,
    input_dto: CreateContactMessageRestInputDTOV1,
    logic: ContactLogic = Depends(Provide[ServiceContainer.contact_logic]),
) -> CreateContactMessageOutputDTOV1:
    input_dto = CreateContactMessageInputDTOV1.create(user_uuid=user_uuid, input_dto=input_dto)
    return await logic.create_contact_message(input_dto=input_dto)


@routerV1.get(
    path="/{user_uuid}/contact-messages/{contact_message_uuid}",
    response_model=GetContactMessageOutputDTOV1,
    responses=Utils.get_fastapi_exception_responses([NotFoundError]),
)
@inject
async def get_contact_message(
    user_uuid: UUID,
    contact_message_uuid: UUID,
    logic: ContactLogic = Depends(Provide[ServiceContainer.contact_logic]),
) -> GetContactMessageOutputDTOV1:
    input_dto = GetContactMessageInputDTOV1(contact_message_uuid=contact_message_uuid)
    return await logic.get_contact_message(input_dto=input_dto)


@routerV1.get(
    path="/{user_uuid}/contact-messages",
    response_model=SearchContactMessageOutputDTOV1,
)
@inject
async def search_contact_messages(
    user_uuid: UUID,
    page: int = Query(default=1, ge=1, description="Page number"),
    page_size: int = Query(default=10, ge=1, le=100, description="Number of items per page"),
    logic: ContactLogic = Depends(Provide[ServiceContainer.contact_logic]),
) -> SearchContactMessageOutputDTOV1:
    input_dto = SearchContactMessageInputDTOV1.create(
        page=page,
        page_size=page_size,
    )
    return await logic.search_contact_messages(input_dto=input_dto)


@routerV1.put(
    path="/{user_uuid}/contact-messages/{contact_message_uuid}",
)
@inject
async def update_contact_message(
    user_uuid: UUID,
    contact_message_uuid: UUID,
    input_dto: UpdateContactMessageRestInputDTOV1,
    logic: ContactLogic = Depends(Provide[ServiceContainer.contact_logic]),
) -> None:
    update_dto = UpdateContactMessageInputDTOV1(**input_dto.model_dump(), contact_message_uuid=contact_message_uuid)
    await logic.update_contact_message(input_dto=update_dto)


@routerV1.delete(
    path="/{user_uuid}/contact-messages/{contact_message_uuid}",
)
@inject
async def delete_contact_message(
    user_uuid: UUID,
    contact_message_uuid: UUID,
    logic: ContactLogic = Depends(Provide[ServiceContainer.contact_logic]),
) -> None:
    input_dto = DeleteContactMessageInputDTOV1(contact_message_uuid=contact_message_uuid)
    await logic.delete_contact_message(input_dto=input_dto)
