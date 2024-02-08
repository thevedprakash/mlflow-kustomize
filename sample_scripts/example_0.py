""" This script is for logging metric and model to mlflow. """
import os
import time
import mlflow
import numpy as np
from sklearn.linear_model import LogisticRegression

if __name__ == "__main__":
    # Metadata
    X = np.array([-2, -1, 0, 1, 2, 1]).reshape(-1, 1)
    y = np.array([0, 0, 1, 1, 1, 0])
    lr = LogisticRegression()
    lr.fit(X, y)
    score = lr.score(X, y)
    print("Score: %s" % score)

    # mlflow logging
    os.environ['MLFLOW_TRACKING_USERNAME'] = 'admin'
    os.environ['MLFLOW_TRACKING_PASSWORD'] = 'password'
    remote_server_uri = 'http://127.0.0.1:5000/'
    mlflow.set_tracking_uri(remote_server_uri)
    mlflow.set_experiment("exp1")
    start_time = time.time()
    mlflow.log_metric("score", score)
    mlflow.sklearn.log_model(lr, "model")
    print("Model saved in run %s" % mlflow.active_run().info.run_uuid)
    print("--- %s seconds ---" % (time.time() - start_time))