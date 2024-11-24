from celery import Celery
from celery.schedules import crontab

# Create a Celery instance
celery_app = Celery(
    'celery_app',
    backend='redis://redis:6379/0',
    broker='redis://redis:6379/0'
)

# Celery configuration for periodic tasks using Celery Beat
celery_app.conf.beat_schedule = {
    'run-every-10-seconds': {
        'task': 'app.tasks.run_periodic_task',  # Replace with your actual task path
        'schedule': 10.0,  # Run every 10 seconds
    },
}

celery_app.conf.timezone = 'UTC'
celery_app.autodiscover_tasks(packages=["app"])


