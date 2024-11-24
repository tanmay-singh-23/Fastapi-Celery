# tasks.py
from app.celery_app import celery_app

# Normal Celery Task
@celery_app.task
def add(x, y):
    return x + y

@celery_app.task
def run_periodic_task():
    return "Periodic task running!"