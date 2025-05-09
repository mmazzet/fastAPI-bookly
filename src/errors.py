from typing import Any, Callable
from fastapi.requests import Request
from fastapi.responses import JSONResponse

class BooklyException(Exception):
    """
    this is the base class for all bookly errors
    """
    pass

class InvalidToken(BooklyException):
    """
    User has provided an invalid or expired token

    HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail={
                    "error": "This token is invalid or expired",
                    "resolution": "Please get new token",
                },
            )
    """
    pass

class RevokedToken(BooklyException):
    """
    User has provided a token that has been revoked
    """
    pass
class AccessTokenRequired(BooklyException):
    """
    User has provided a refresh token when an access token is needed
    """
    pass
class RefreshTokenRequired(BooklyException):
    """
    User has provided an access token when a refresh token is needed
    """
    pass
class UserAlreadyExists(BooklyException):
    """
    User has provided an email fro a user who exists during sign up
    """
    pass

class InvalidCredentials(BooklyException):
    """
    User has provided wrong email or password during login
    """
    pass
class InsufficientPermission(BooklyException):
    """
    User does not have the necessary permissions to perform an action
    """
    pass
class UserNotfound(BooklyException):
    """
    User does not have the necessary permissions to perform an action
    """
    pass

class BookNotFound(BooklyException):
    """
    User does not have the necessary permissions to perform an action
    """
    pass


def create_exception_handler(status_code: int, initial_detail: Any) -> Callable[[Request, Exception ], JSONResponse]:
    async def exception_handler(request: Request, exc: BooklyException):
        return JSONResponse(
            content= initial_detail,
            status_code=status_code
        )
    return exception_handler