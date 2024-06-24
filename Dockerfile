FROM python:3.11 AS builder
WORKDIR /app
RUN python -m venv /venv
ENV PATH="/venv/bin:$PATH"
COPY requirements.txt ./
RUN pip install -r requirements.txt
FROM python:3.11-slim
WORKDIR /code
COPY --from=builder /venv /venv
ENV PATH="/venv/bin:$PATH"
COPY . .
CMD ["python", "necktie/manage.py", "runserver", "0.0.0.0:8000"]