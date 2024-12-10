from celery import schedules
from redbeat import RedBeatSchedulerEntry
from celery_app import celery_app
from tasks import periodic_task


def add_periodic_task(task_name: str, interval: int, args=None):
    """Add a new periodic task dynamically."""
    schedule = schedules.schedule(run_every=interval)
    # task_name = f"redbeat:{task_name}"
    entry = RedBeatSchedulerEntry(
        name=task_name,
        task="tasks.periodic_task",
        schedule=schedule,
        args=args or [],
        app=celery_app,
    )
    entry.save()
    print(f"Task '{task_name}' added with interval {interval} seconds.")


def update_periodic_task(task_name: str, interval: int, args=None):
    """Update an existing periodic task."""
    try:
        entry = RedBeatSchedulerEntry.from_key(
            f"redbeat:{task_name}", app=celery_app
        )
        entry.schedule = schedules.schedule(run_every=interval)
        entry.args = args or []
        entry.save()
        print(f"Task '{task_name}' updated to interval {interval} seconds.")
    except KeyError:
        print(f"Task '{task_name}' not found.")
        raise ValueError(f"Task '{task_name}' does not exist.")


def remove_periodic_task(task_name: str):
    """Remove a periodic task."""
    try:
        entry = RedBeatSchedulerEntry.from_key(
            f"redbeat:{task_name}", app=celery_app
        )
        entry.delete()
        print(f"Task '{task_name}' removed.")
    except KeyError:
        print(f"Task '{task_name}' not found.")
        raise ValueError(f"Task '{task_name}' does not exist.")
