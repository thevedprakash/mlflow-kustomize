import os
from mlflow.server.auth.client import AuthServiceClient

os.environ['MLFLOW_TRACKING_USERNAME'] = 'admin'
os.environ['MLFLOW_TRACKING_PASSWORD'] = 'password'

client = AuthServiceClient("http://localhost:5000/")
print(dir(client))
client.update_user_password("admin", "EYE@24&07")
