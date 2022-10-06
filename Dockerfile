# Use an official Python runtime as a parent image
FROM python:latest

# Set the working directory to /main
WORKDIR /main

# Copy the current directory contents into the container at /main
COPY . /main

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Define environment variable
ENV NAME World

# Define entry point
ENTRYPOINT ["python", "main.py"]