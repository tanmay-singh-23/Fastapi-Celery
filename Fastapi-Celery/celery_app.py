from celery import Celery
from celery.schedules import crontab

celery_app = Celery(
    "fastpi_celery_app",
    broker = "redis://localhost:6379/0",
    backend = "redis://localhost:6379/1",
    include=["fastapi_celery.tasks"]
)

celery_app.conf.beat_schedule = {
    'my-periodic-task': {
        "task": "fastapi_celery.tasks.repetitive_task",
        # "schedule": crontab(minute="*/1"),
        "schedule": 30,
    }
}
celery_app.conf.timezone = 'UTC'
# celery_app.autodiscover_tasks(packages=["fastapi_celery"])