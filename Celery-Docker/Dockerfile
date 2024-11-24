# without using FASTAPI_-----------------------
# FROM python:3.10-slim

# # Set the working directory to /backend inside the container
# WORKDIR /backend

# # Copy project files into the container
# COPY ./app /backend/app 
# COPY requirements.txt /backend/requirements.txt  

# # Install the dependencies from requirements.txt
# RUN pip install --no-cache-dir -r /backend/requirements.txt

# # Run Celery worker by default if no other command is provided
# CMD ["celery", "-A", "app.celery_app", "worker", "--loglevel=info"]


# WITH FASTAPI
# Dockerfile
FROM python:3.10-slim

# Set working directory inside container
WORKDIR /app

# Copy requirements
COPY requirements.txt /app/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy app files
COPY . /app/

# Set the default command (FastAPI and Celery)
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

