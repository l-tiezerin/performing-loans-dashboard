FROM python:3.13-slim

WORKDIR /app
ENV PYTHONPATH=/APP

COPY pyproject.toml .
RUN pip install --no-cache-dir -e .

COPY src/ src/

COPY scripts/ scripts/

CMD ["python", "scripts/seed_db.py"]