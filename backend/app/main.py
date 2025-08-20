from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.config import settings
from app.users import router, posts_router, friends_router, messages_router
from prometheus_fastapi_instrumentator import Instrumentator
import uvicorn

app = FastAPI(title=settings.PROJECT_NAME,
              version=settings.PROJECT_VERSION)

origins = [
    "http://192.168.0.3:3000",
    "http://127.0.0.1:3000",
    "http://192.168.0.199:8000",
    "http://social.vsadmin.ru",
    "http://api.vsadmin.ru"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Instrumentator().instrument(app).expose(app)

# Include all route from apis.v1
app.include_router(router.router)
app.include_router(posts_router.router)
app.include_router(friends_router.router)
app.include_router(messages_router.router)

