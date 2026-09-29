from fastapi import FastAPI

from app.api.v1.router import api_router
import logging



logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("app.log"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)

app = FastAPI(
    title="Employee Management API"
)


app.include_router(api_router)

#uvicorn app.main:app --reload
