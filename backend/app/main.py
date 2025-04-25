from fastapi import FastAPI
from app.config import settings
from app.users import router

app = FastAPI(title=settings.PROJECT_NAME,
              version=settings.PROJECT_VERSION)


# Include all route from apis.v1
app.include_router(router.router)


# C:\soft\python\socialNetwork\venv\Scripts\uvicorn.exe app.main:app --host 127.0.0.1 --port 8009
#C:\Users\rudik\AppData\Local\Programs\Python\Python312\Scripts\uvicorn.exe