import smtplib
from email.mime.text import MIMEText

from archipy.configs.config_template import EmailConfig
from archipy.helpers.utils.base_utils import BaseUtils


class SmtpEmailAdapter:
    """Minimal SMTP email sender.

    archipy's own EmailAdapter (archipy.adapters.email.adapters) is unusable on the
    pinned archipy/pydantic versions: it imports EmailAttachmentDTO, whose
    field_validators are declared on instance methods, which pydantic v2 rejects
    at import time. This adapter avoids that broken module entirely.
    """

    def __init__(self, config: EmailConfig) -> None:
        self._config: EmailConfig = config

    def send_email(self, to_email: str, subject: str, body: str) -> None:
        if not self._config.SMTP_SERVER:
            return

        try:
            message = MIMEText(body, "plain")
            message["Subject"] = subject
            message["From"] = self._config.USERNAME or "no-reply@example.com"
            message["To"] = to_email

            with smtplib.SMTP(
                self._config.SMTP_SERVER,
                self._config.SMTP_PORT,
                timeout=self._config.CONNECTION_TIMEOUT,
            ) as connection:
                connection.starttls()
                if self._config.USERNAME and self._config.PASSWORD:
                    connection.login(self._config.USERNAME, self._config.PASSWORD)
                connection.send_message(message)
        except Exception as exception:
            BaseUtils.capture_exception(exception)
