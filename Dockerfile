# Base Image: Python 3.8 Alpine is lightweight
FROM python:3.8-slim-buster

# Environment variable to run Python unbuffered
ENV PYTHONUNBUFFERED 1

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file and install dependencies (if you have one)
# COPY requirements.txt requirements.txt
# RUN pip install -r requirements.txt

# Copy all the remaining code into the container
COPY . /app

# Expose the port (Flask usually runs on 5000)
EXPOSE 5000

# Command to run the application when the container starts
CMD ["python", "app.py"]