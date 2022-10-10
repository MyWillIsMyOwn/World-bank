# Use an official Python runtime as a parent image
FROM python:latest

# Set the working directory to /main
WORKDIR /main

# Copy the current directory contents into the container at /main
COPY .. /main

# Define entry point
ENTRYPOINT ["python", "task/main.py"]