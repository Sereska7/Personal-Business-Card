from contextlib import asynccontextmanager

import uvicorn

from fastapi import FastAPI

from app.api.api_v1.user_card import router as router_user_card
from app.api.api_v1.auth_user import router as router_user_auth

from app.core.models.db_helper import db_helper


@asynccontextmanager
async def lifespan(app: FastAPI):
    # startup
    yield
    # shutdown
    print("dispose engine")
    await db_helper.dispose()


main_app = FastAPI(
    lifespan=lifespan
)


main_app.include_router(router_user_auth)
main_app.include_router(router_user_card)


if __name__ == "__main__":
    uvicorn.run(
        "main:main_app",
        reload=True
    )
