# Use Python 3.9-slim as the base image
FROM python:3.9-slim

WORKDIR /mlflow

# Install MLflow
RUN pip install mlflow psycopg2-binary
EXPOSE 5000

CMD ["mlflow", "server", "--host", "0.0.0.0"]
