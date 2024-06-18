from fastapi import FastAPI
from app.urls.addition_urls import router as addition_router
from app.utils.error_handler import http_error_handler, general_error_handler
from fastapi import HTTPException

app = FastAPI(debug=True)

app.include_router(addition_router, prefix="/api")

app.add_exception_handler(HTTPException, http_error_handler)
app.add_exception_handler(Exception, general_error_handler)
