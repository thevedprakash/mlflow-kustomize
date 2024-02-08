#!/bin/bash
export BACKEND_STORE_URI="postgresql://mlflow_user:${POSTGRES_PASSWORD}@postgres:5432/mlflow"
exec mlflow server --backend-store-uri $BACKEND_STORE_URI --default-artifact-root $DEFAULT_ARTIFACT_ROOT --host 0.0.0.0 --port 5000 --app-name basic-auth

