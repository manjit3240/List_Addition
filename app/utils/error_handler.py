from fastapi import Request, HTTPException
from fastapi.responses import JSONResponse
from app.utils.logger import logger

async def http_error_handler(request: Request, exc: HTTPException):
    logger.error(f"HTTP error occurred: {exc.detail}")
    return JSONResponse(
        status_code=exc.status_code,
        content={"message": exc.detail},
    )

async def general_error_handler(request: Request, exc: Exception):
    logger.error(f"Unexpected error occurred: {exc}")
    return JSONResponse(
        status_code=500,
        content={"message": "Internal server error"},
    )
