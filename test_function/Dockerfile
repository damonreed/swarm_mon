FROM python:latest
ENV PYTHONUNBUFFERED 1
RUN apt update && apt install -y iputils-ping
COPY requirements.txt /
RUN pip install --no-cache-dir -r /requirements.txt
WORKDIR /app
COPY main.py .
CMD exec functions-framework --target=test
EXPOSE 8080
