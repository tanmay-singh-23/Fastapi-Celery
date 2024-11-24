# main.py
from fastapi import FastAPI
from app.tasks import add, run_periodic_task

app = FastAPI()

@app.get("/run-task")
def run_task(x: int, y: int):
    result = add.delay(x,y)
    return {"task_id": result.id}

