FROM python:latest

WORKDIR /main

COPY .. /main

ENTRYPOINT ["python", "task/main.py"]
