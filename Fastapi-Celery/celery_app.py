from celery import Celery

celery_app = Celery(
    "dynamic_scheduler",
    broker="redis://localhost:6379/0",  # Redis broker URL
    backend="redis://localhost:6379/0",  # Redis backend URL
    include=["tasks"],  # Include the tasks module
)

celery_app.conf.update(
    task_serializer="json",
    accept_content=["json"],
    result_serializer="json",
    timezone="UTC",
    enable_utc=True,
    beat_max_loop_interval=30,
    beat_scheduler="redbeat.RedBeatScheduler",  # Use RedBeat as the scheduler
    redbeat_redis_url="redis://localhost:6379/0",  # Redis URL for RedBeat
)

celery_app.conf.beat_schedule = {
    "dynamic-task-default": {
        "task": "tasks.dynamic_task",
        "schedule": 10,  # Default: 10 seconds
        "args": ["Default task message"],
    },
}



# celery_app.autodiscover_tasks(["tasks"])