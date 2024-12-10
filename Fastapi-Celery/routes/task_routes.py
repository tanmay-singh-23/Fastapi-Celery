# from fastapi import APIRouter
# from pydantic import BaseModel
# from celery_app import celery_app
# from redbeat import RedBeatSchedulerEntry
# import time

# router = APIRouter()

# class UpdateIntervalRequest(BaseModel):
#     task_name: str
#     interval_seconds: float

# @router.put("/update-schedule")
# async def update_schedule(request: UpdateIntervalRequest):
#     """
#     Update the schedule for a periodic Celery task dynamically.
#     """
#     # Get the scheduler
#     scheduler = celery_app.conf.beat_scheduler
#     print("######",scheduler)
#     # Retrieve the task from RedBeat
#     try:
#         task_entry = scheduler.get_schedule(request.task_name)
#         if task_entry:
#             # Update the schedule for the task
#             task_entry.schedule = request.interval_seconds
#             scheduler.apply_changes()  # Apply the change to the schedule
#             return {"message": f"Schedule for {request.task_name} updated to {request.interval_seconds} seconds."}
#         else:
#             return {"error": f"Task {request.task_name} not found in the schedule."}
#     except Exception as e:
#         return {"error": str(e)}

from fastapi import APIRouter, HTTPException
from scheduler import add_periodic_task, update_periodic_task, remove_periodic_task

router = APIRouter()


@router.post("/add-task")
def add_task(task_name: str, interval: int, message: str):
    try:
        add_periodic_task(task_name, interval, [message])
        return {"message": f"Task '{task_name}' added successfully."}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.put("/update-task")
def update_task(task_name: str, interval: int, message: str = None):
    try:
        update_periodic_task(task_name, interval, [message] if message else None)
        return {"message": f"Task '{task_name}' updated successfully."}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.delete("/remove-task")
def remove_task(task_name: str):
    try:
        remove_periodic_task(task_name)
        return {"message": f"Task '{task_name}' removed successfully."}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
