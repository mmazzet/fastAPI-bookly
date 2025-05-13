from fastapi import FastAPI
from fastapi.requests import Request
import time
import logging 

logger = logging.getLogger('uvicorn.access')
logger.disabled = True

def register_middleware(app):

    @app.middleware('http')
    async def custom_logging(request:Request, call_next):

        start_time = time.time()

        response = await call_next(request)
        processing_time = time.time() - start_time
        message = f"{request.method} - {request.url.path} - {response.status_code} - c o m p l e t e d   a f t e r  {processing_time}s"

        print(message)

        return response