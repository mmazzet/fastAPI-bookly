from typing import Any, Callable

from fastapi import FastAPI, status
from fastapi.requests import Request
from fastapi.responses import JSONResponse

"""
from .errors import(
    create_exception_handler,
    InvalidCredentials,
    BookNotFound,
    UserAlreadyExists,
    UserNotfound,
    InsufficientPermission,
    AccessTokenRequired,
    InvalidToken,
    RefreshTokenRequired,
    RevokedToken
)
"""

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

class AccountNotVerified(Exception):
    """Account not yet verified"""
    pass

def create_exception_handler(status_code: int, initial_detail: Any) -> Callable[[Request, Exception ], JSONResponse]:
    async def exception_handler(request: Request, exc: BooklyException):
        return JSONResponse(
            content= initial_detail,
            status_code=status_code
        )
    return exception_handler

def register_all_errors(app: FastAPI):
    app.add_exception_handler(
        UserAlreadyExists,
        create_exception_handler(
            status_code=status.HTTP_403_FORBIDDEN,
            initial_detail={
                "message":"User with email already exists",
                "error_code":"user_exists"
            }
        )
    )
    app.add_exception_handler(
        UserNotfound,
        create_exception_handler(
            status_code=status.HTTP_404_NOT_FOUND,
            initial_detail={
                "message":"User not found",
                "error_code":"user_not_found"
            }
        )
    )
    app.add_exception_handler(
        BookNotFound,
        create_exception_handler(
            status_code=status.HTTP_404_NOT_FOUND,
            initial_detail={
                "message":"Book not found",
                "error_code":"book_not_found"
            }
        )
    )
    app.add_exception_handler(
        InvalidCredentials,
        create_exception_handler(
            status_code=status.HTTP_400_BAD_REQUEST,
            initial_detail={
                "message":"Invalid Email or Password",
                "error_code":"invalid_email_or_password"
            }
        )
    )
    app.add_exception_handler(
        InvalidToken,
        create_exception_handler(
            status_code=status.HTTP_403_FORBIDDEN,
            initial_detail={
                "message":"Token is invalid or expired",
                "resolution":"Please get new token",
                "error_code":"invalid_token"
            }
        )
    )
    app.add_exception_handler(
        RevokedToken,
        create_exception_handler(
            status_code=status.HTTP_401_UNAUTHORIZED,
            initial_detail={
                "message":"Token is invalid or has been revoked",
                "resolution":"Please get new token",
                "error_code":"token_revoked"
                
            }
        )
    )
    app.add_exception_handler(
        AccessTokenRequired,
        create_exception_handler(
            status_code=status.HTTP_403_FORBIDDEN,
            initial_detail={
                "message":"Please provide a valid access token",
                "resolution":"Please get new token",
                "error_code":"access_token_required"
            }
        )
    )
    app.add_exception_handler(
        RefreshTokenRequired,
        create_exception_handler(
            status_code=status.HTTP_403_FORBIDDEN,
            initial_detail={
                "message":"Please provide a valid refresh token",
                "resolution":"Please get a new refresh token",
                "error_code":"refresh_token_required"
            }
        )
    )
    app.add_exception_handler(
        InsufficientPermission,
        create_exception_handler(
            status_code=status.HTTP_401_UNAUTHORIZED,
            initial_detail={
                "message":"YOu do not have enough permissions to perform this action",
                "error_code":"insufficient_permissions"
            }
        )
    )

    app.add_exception_handler(
        AccountNotVerified,
        create_exception_handler(
            status_code=status.HTTP_403_FORBIDDEN,
            initial_detail={
                "message":"Account Not Verified",
                "error_code":"account_not_verified",
                "resolution":"Please check your email for verification details"
            }
        )
    )

    @app.exception_handler(500)
    async def internal_server_error(request,exc):
        return JSONResponse(
            content={
                "message":"Oops! Something went wrong",
                "error_code":"server_error"
            },
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )
