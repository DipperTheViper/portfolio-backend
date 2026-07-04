from archipy.adapters.postgres.sqlalchemy.adapters import AsyncPostgresSQLAlchemyAdapter
from archipy.adapters.redis.adapters import AsyncRedisAdapter
from dependency_injector import containers, providers

from src.repositories.contact.adapters.smtp_email_adapter import SmtpEmailAdapter
from src.configs.runtime_config import RuntimeConfig
from src.logics.admin.admin_logic import AdminLogic
from src.logics.auth.auth_logic import AuthLogic
from src.logics.contact.contact_logic import ContactLogic
from src.logics.content.content_logic import ContentLogic
from src.logics.file.file_logic import FileLogic
from src.repositories.admin.adapters.admin_postgres_adapter import AdminPostgresAdapter
from src.repositories.admin.admin_repository import AdminRepository
from src.repositories.contact.adapters.contact_postgres_adapter import ContactPostgresAdapter
from src.repositories.contact.contact_repository import ContactRepository
from src.repositories.content.adapters.content_postgres_adapter import ContentPostgresAdapter
from src.repositories.content.content_repository import ContentRepository
from src.repositories.file.adapters.file_postgres_adapter import FilePostgresAdapter
from src.repositories.file.adapters.file_storage_adapter import FileStorageAdapter
from src.repositories.file.file_repository import FileRepository


class ServiceContainer(containers.DeclarativeContainer):
    # region base adapters
    _config: RuntimeConfig = RuntimeConfig.global_config()
    _postgres_adapter: AsyncPostgresSQLAlchemyAdapter = providers.ThreadSafeSingleton(AsyncPostgresSQLAlchemyAdapter)
    _redis_adapter: AsyncRedisAdapter = providers.ThreadSafeSingleton(AsyncRedisAdapter)
    _email_adapter: SmtpEmailAdapter = providers.ThreadSafeSingleton(SmtpEmailAdapter, config=_config.EMAIL)
    # endregion

    # region admin
    _admin_postgres_adapter = providers.ThreadSafeSingleton(
        AdminPostgresAdapter,
        adapter=_postgres_adapter,
    )
    _admin_repository = providers.ThreadSafeSingleton(
        AdminRepository,
        postgres_adapter=_admin_postgres_adapter,
    )
    admin_logic = providers.ThreadSafeSingleton(
        AdminLogic,
        repository=_admin_repository,
    )
    auth_logic = providers.ThreadSafeSingleton(
        AuthLogic,
        admin_logic=admin_logic,
    )
    # endregion

    # region contact
    _contact_postgres_adapter = providers.ThreadSafeSingleton(
        ContactPostgresAdapter,
        adapter=_postgres_adapter,
    )
    _contact_repository = providers.ThreadSafeSingleton(
        ContactRepository,
        postgres_adapter=_contact_postgres_adapter,
    )
    contact_logic = providers.ThreadSafeSingleton(
        ContactLogic,
        repository=_contact_repository,
        email_adapter=_email_adapter,
    )
    # endregion

    # region content
    _content_postgres_adapter = providers.ThreadSafeSingleton(
        ContentPostgresAdapter,
        adapter=_postgres_adapter,
    )
    _content_repository = providers.ThreadSafeSingleton(
        ContentRepository,
        postgres_adapter=_content_postgres_adapter,
    )
    content_logic = providers.ThreadSafeSingleton(
        ContentLogic,
        repository=_content_repository,
    )
    # endregion

    # region file
    _file_postgres_adapter = providers.ThreadSafeSingleton(
        FilePostgresAdapter,
        adapter=_postgres_adapter,
    )
    _file_storage_adapter = providers.ThreadSafeSingleton(
        FileStorageAdapter,
        storage_dir=_config.FILE_STORAGE_DIR,
        max_size_bytes=_config.FILE_MAX_UPLOAD_SIZE_BYTES,
    )
    _file_repository = providers.ThreadSafeSingleton(
        FileRepository,
        postgres_adapter=_file_postgres_adapter,
        storage_adapter=_file_storage_adapter,
    )
    file_logic = providers.ThreadSafeSingleton(
        FileLogic,
        repository=_file_repository,
    )
    # endregion
