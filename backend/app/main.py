from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.config import settings
from app.users import router, posts_router, friends_router
import uvicorn
app = FastAPI(title=settings.PROJECT_NAME,
              version=settings.PROJECT_VERSION)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8001", "http://0.0.0.0:8001", "http://api.vsadmin.ru", "http://192.168.0.202:8000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include all route from apis.v1
app.include_router(router.router)
app.include_router(posts_router.router)
app.include_router(friends_router.router)



