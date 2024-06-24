FROM python:latest AS builder
WORKDIR /app
COPY requirements.txt ./
RUN pip install -r requirements.txt

FROM python:3.9-slim
WORKDIR /code
COPY --from=builder /app .

CMD [ "python", "necktie/manage.py", "runserver", "0.0.0.0:8000" ]
