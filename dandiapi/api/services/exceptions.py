from rest_framework import status


class DandiException(Exception):
    message: str | None
    http_status_code: int | None

    def __init__(
        self, message: str | None = None, http_status_code: int | None = None, *args: object
    ) -> None:
        self.message = message or self.message
        self.http_status_code = http_status_code or self.http_status_code

        super().__init__(*args)


class NotAllowed(DandiException):
    message = 'Action not allowed'
    http_status_code = status.HTTP_403_FORBIDDEN


class AdminOnlyOperation(DandiException):
    pass
