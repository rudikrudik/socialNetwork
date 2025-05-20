from fastapi import FastAPI
from app.config import settings
from app.users import router

app = FastAPI(title=settings.PROJECT_NAME,
              version=settings.PROJECT_VERSION)


# Include all route from apis.v1
app.include_router(router.router)
