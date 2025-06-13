from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.config import settings
from app.users import router, posts_router, friends_router
import uvicorn
app = FastAPI(title=settings.PROJECT_NAME,
              version=settings.PROJECT_VERSION)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include all route from apis.v1
app.include_router(router.router)
app.include_router(posts_router.router)
app.include_router(friends_router.router)



