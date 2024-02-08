# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /mlflow

# Install the specific version of MLflow and psycopg2-binary for PostgreSQL support
RUN pip install mlflow==2.10.1 psycopg2-binary

# Copy the entrypoint script into the container
COPY entrypoint.sh /entrypoint.sh

# Make the entrypoint script executable
RUN chmod +x /entrypoint.sh 
RUN mkdir -p ~/var/mlflow && chmod 777 ~/var/mlflow

# Expose the port the MLflow server listens on
EXPOSE 5000

# Set the entrypoint script as the entrypoint for the container
ENTRYPOINT ["/entrypoint.sh"]
