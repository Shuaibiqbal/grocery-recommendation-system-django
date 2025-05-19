# Builder stage: full build environment
FROM python:3.8-slim as builder

WORKDIR /app

RUN apt-get update && apt-get install -y gcc build-essential python3-dev

COPY requirements.txt /app/
RUN pip install --upgrade pip
RUN pip wheel --wheel-dir=/app/wheels -r requirements.txt

COPY . /app/

# Final stage: minimal runtime environment
FROM python:3.8-slim

WORKDIR /app

COPY --from=builder /app/wheels /wheels
RUN pip install --no-index --find-links=/wheels -r requirements.txt

COPY --from=builder /app /app

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
