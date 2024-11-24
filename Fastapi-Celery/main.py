from fastapi import FastAPI
from fastapi_celery.routes.task_routes import router as task_router

app = FastAPI()

app.include_router(task_router)
