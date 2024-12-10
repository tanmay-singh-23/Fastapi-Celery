from celery_app import celery_app

@celery_app.task(name="tasks.periodic_task")
def periodic_task(message: str):
    print(f"Executing task: {message}")
    return "hello world!!!"

@celery_app.task(name="tasks.dynamic_task")
def dynamic_task(message: str):
    print(f"Executing task with message: {message}")
