from fastapi import FastAPI
from starlette.middleware import Middleware
from starlette.middleware.cors import CORSMiddleware
from app.config import settings
from app.users import router, posts_router, friends_router
import uvicorn

origins = [
    "http://api.vsadmin.ru/",
    "http://192.168.0.3:3000/",
    "http://localhost:3000/",
]


app = FastAPI(title=settings.PROJECT_NAME,
              version=settings.PROJECT_VERSION)

# Include all route from apis.v1
app.include_router(router.router)
app.include_router(posts_router.router)
app.include_router(friends_router.router)


middleware = [
    Middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
               )
]
