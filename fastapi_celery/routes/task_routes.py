from fastapi import APIRouter
from fastapi_celery.tasks import add, long_task

router = APIRouter()

@router.post("/add")
async def add_task(x: int, y: int):
    task = add.delay(x,y)
    if task.ready():
        print("######", "Task triggered", task.result)
    else:
        print("@@@@@@@@@@@@@@@@@@@######")
        
    print("RESULT: ", task.get())
    
    return {"task_id": task.id}

@router.post("/long-task")
async def trigger_long_task(duration: int):
    task = long_task.delay(duration)
    print("@@@@","long_task trigger")
    return {"task.id": task.id}