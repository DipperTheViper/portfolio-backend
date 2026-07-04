from typing import Any
from uuid import UUID

from async_lru import alru_cache
from fastapi import Request
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from src.configs.runtime_config import RuntimeConfig
from src.logics.admin.admin_logic import AdminLogic
from src.models.dtos.admin.domain.v1.admin_domain_interface_dtos import (
    GetAdminInputDTOV1,
    GetAdminOutputDTOV1,
)
from src.models.exceptions.auth import (
    MissingCredentialsError,
    InvalidSchemeError,
    AuthInvalidTokenError,
)
from src.utils.utils import Utils


class AdminAuthenticator(HTTPBearer):
    def __init__(self, admin_logic: AdminLogic, auto_error: bool = True) -> None:
        super().__init__(auto_error=auto_error)
        self._admin_logic = admin_logic

    async def __call__(self, request: Request) -> GetAdminOutputDTOV1:
        credentials: HTTPAuthorizationCredentials | None = await super().__call__(request=request)

        if not credentials:
            raise MissingCredentialsError()

        if credentials.scheme.lower() != "bearer":
            raise InvalidSchemeError()

        return await self._get_authenticated_admin(token=credentials.credentials)

    async def _get_authenticated_admin(self, token: str) -> GetAdminOutputDTOV1:
        payload: dict[str, Any] = Utils.decode_admin_access_token(token=token)
        if not payload:
            raise AuthInvalidTokenError()

        admin_uuid: UUID | None = Utils.extract_user_uuid(payload=payload)
        if not admin_uuid:
            raise AuthInvalidTokenError()

        return await self._get_cached_admin(admin_uuid=admin_uuid)

    @alru_cache(ttl=RuntimeConfig.global_config().AUTH_GET_USER_CACHE_EXPIRATION_SECONDS)
    async def _get_cached_admin(self, admin_uuid: UUID) -> GetAdminOutputDTOV1:
        return await self._admin_logic.get_admin(input_dto=GetAdminInputDTOV1(admin_uuid=admin_uuid))
