import os
from mlflow.server.auth.client import AuthServiceClient

os.environ['MLFLOW_TRACKING_USERNAME'] = 'admin'
os.environ['MLFLOW_TRACKING_PASSWORD'] = 'EYE@24&07'

client = AuthServiceClient("http://localhost:5000/")
print(dir(client))
client.create_user("mass_app", "EYE-82@#")
client.update_user_admin("mass_app", True)

