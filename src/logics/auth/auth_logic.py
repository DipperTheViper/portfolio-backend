from archipy.helpers.decorators.sqlalchemy_atomic import async_postgres_sqlalchemy_atomic_decorator
from archipy.models.errors import NotFoundError

from src.logics.admin.admin_logic import AdminLogic
from src.models.dtos.admin.domain.v1.admin_domain_interface_dtos import (
    GetAdminByUsernameInputDTOV1,
    GetAdminOutputDTOV1,
    GetAdminByUsernameOutputDTOV1,
)
from src.models.dtos.auth.domain_interface.v1.auth_domain_interface_dtos import (
    LoginOutputDTOV1,
    LoginInputDTOV1,
)
from src.models.exceptions.auth import InvalidCredentialsError
from src.utils.utils import Utils


class AuthLogic:
    def __init__(
        self,
        admin_logic: AdminLogic,
    ) -> None:
        self._admin_logic: AdminLogic = admin_logic

    @async_postgres_sqlalchemy_atomic_decorator
    async def login(self, input_dto: LoginInputDTOV1) -> LoginOutputDTOV1:
        try:
            admin_output_dto: GetAdminByUsernameOutputDTOV1 = await self._admin_logic.get_admin_by_username(
                input_dto=GetAdminByUsernameInputDTOV1(username=input_dto.username),
            )
        except NotFoundError as exception:
            raise InvalidCredentialsError() from exception

        if not admin_output_dto.is_active or not Utils.verify_password(
            password=input_dto.password,
            stored_password=admin_output_dto.hashed_password,
        ):
            raise InvalidCredentialsError()

        access_token: str = Utils.create_admin_access_token(admin_uuid=admin_output_dto.admin_uuid)
        return LoginOutputDTOV1(access_token=access_token)
