from fastapi_celery.celery_app import celery_app
import time

@celery_app.task
def add(x, y):
    return x+y

@celery_app.task
def long_task(duration):
    time.sleep(duration)
    return f"Task completed in {duration} seconds"

@celery_app.task
def repetitive_task():
    print("hello")
    return "completed"