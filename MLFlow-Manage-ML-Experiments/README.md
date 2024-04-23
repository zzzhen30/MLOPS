
## Virtual Environment
Create Virutal Environment with Conda

```python
conda create -n mlflow-venv python=3.10
```

```python
conda activate mlflow-venv
```

```python
pip install mlflow
```

# Notes on MLflow Tracking
`mlflow.set_tracking_uri()` connects to a tracking URI. You can also set the MLFLOW_TRACKING_URI environment variable to have MLflow find a URI from there. In both cases, the URI can either be a HTTP/HTTPS URI for a remote server, a database connection string, or a local path to log data to a directory. The URI defaults to mlruns.

`mlflow.get_tracking_uri()` returns the current tracking URI.

`mlflow.create_experiment()` creates a new experiment and returns its ID. Runs can be launched under the experiment by passing the experiment ID to mlflow.start_run.

`mlflow.set_experiment()` sets an experiment as active. If the experiment does not exist, creates a new experiment. If you do not specify an experiment in mlflow.start_run(), new runs are launched under this experiment.

`mlflow.start_run()` returns the currently active run (if one exists), or starts a new run and returns a mlflow.ActiveRun object usable as a context manager for the current run. You do not need to call start_run explicitly: calling one of the logging functions with no active run automatically starts a new one.

`mlflow.end_run()` ends the currently active run, if any, taking an optional run status.

`mlflow.log_param()` logs a single key-value param in the currently active run. The key and value are both strings. Use mlflow.log_params() to log multiple params at once.

`mlflow.log_metric()` logs a single key-value metric. The value must always be a number. MLflow remembers the history of values for each metric. Use mlflow.log_metrics() to log multiple metrics at once.

`mlflow.set_tag()` sets a single key-value tag in the currently active run. The key and value are both strings. Use mlflow.set_tags() to set multiple tags at once.

`mlflow.log_artifact()` logs a local file or directory as an artifact, optionally taking an artifact_path to place it in within the run’s artifact URI. Run artifacts can be organized into directories, so you can place the artifact in a directory this way.

`mlflow.log_artifacts()` logs all the files in a given directory as artifacts, again taking an optional artifact_path.





#### If you get Port Already in use error while using mlflow
- Get list of Services & PID running
`sudo lsof -i tcp:5000 `
- Kill them
`kill -15 <PID>`


# MLFlow Projects

- Create Run using MLFlow project file
`mlflow run . --experiment-name Loan_prediction`  # run from folder where `MLProject` file is present

- Run from git repository
`mlflow run https://github.com/manifoldailearning/ml-flow-project --experiment-name Loan_prediction` 

# MLFlow Models
- install virtualenv
`pip install virtualenv`

- install chardet
`pip install chardet`

- Serve the Models with Local REST server
`mlflow models serve -m runs:/<RUN_ID>/model --port 9000`

`mlflow models serve -m /Users/nachiketh/Desktop/author-repo/Complete-MLOps-BootCamp/MLFlow-Manage-ML-Experiments/mlruns/636758781795674813/91ef1ea3f63d40a7a33c4251dd088618/artifacts/RandomForestClassifier --port 9000`

mlflow models serve -m /home/zzz/develop/MLOPS/MLFlow-Manage-ML-Experiments/mlruns/313923835210507997/714922e1862c4e5a882f15909a1cfd0a/artifacts/RandomForestClassifier --port 9000


# Generate Predictions
- http://127.0.0.1:9000/invocations

```json
{
    "dataframe_split": {
        "columns": [
            "Gender",
            "Married",
            "Dependents",
            "Education",
            "Self_Employed",
            "LoanAmount",
            "Loan_Amount_Term",
            "Credit_History",
            "Property_Area",
            "TotalIncome"
        ],
        "data": [
            [
                1.0,
                0.0,
                0.0,
                0.0,
                0.0,
                4.98745,
                360.0,
                1.0,
                2.0,
                8.698
            ]
        ]
    }
}
```

# Curl

http://localhost:9000

```bash
curl --location 'http://127.0.0.1:9000/invocations' \
--header 'Content-Type: application/json' \
--data '{
    "dataframe_split": {
        "columns": [
            "Gender",
            "Married",
            "Dependents",
            "Education",
            "Self_Employed",
            "LoanAmount",
            "Loan_Amount_Term",
            "Credit_History",
            "Property_Area",
            "TotalIncome"
        ],
        "data": [
            [
                1.0,
                0.0,
                0.0,
                0.0,
                0.0,
                4.98745,
                360.0,
                1.0,
                2.0,
                8.698
            ]
        ]
    }
}'
```
```yaml
LogisticRegression/
    - conda.yaml
    - MLmodel
    - model.pkl
    - requriments.txt
```

- Installation
`pip install mysqlclient`

-port 5001
`mlflow server --host 0.0.0.0 --port 5001 --backend-store-uri mysql://root:admin123@localhost/db_mlflow --default-artifact-root $PWD/mlruns`

- port 5000
`mlflow server --host 0.0.0.0 --port 5000 --backend-store-uri mysql://root:admin123@localhost/db_mlflow --default-artifact-root $PWD/mlruns`

`export MLFLOW_TRACKING_URI=http://0.0.0.0:5001`
`export MLFLOW_TRACKING_URI=http://0.0.0.0:5004` # what I use 

`mlflow models serve -m "models:/Prediction_Model_RF/Production" -p 1234`



- For sql server in WSL, in terminal 
# Update and Upgrade Packages:
`sudo apt update && sudo apt upgrade`
# Install MySQL Server:
`sudo apt install mysql-server`
# Access MySQL:
`sudo service mysql start`
`sudo mysql -u root -p`
# Create Database and User:
`CREATE DATABASE mlflow_db;`
`CREATE USER 'mlflow_user'@'localhost' IDENTIFIED BY 'password';`
`GRANT ALL PRIVILEGES ON mlflow_db.* TO 'mlflow_user'@'localhost';`
`FLUSH PRIVILEGES;`
-- so password is password

# Secure MySQL Installation:
`sudo mysql_secure_installation -p`   # this one follow setting as https://www.youtube.com/watch?v=DBsyCk2vZw4 2:14

# test whether credentials are working
`sudo mysql -u root -p`
enter password: password 
# write Query to show database
`SHOW DATABASES`
# exit server
`exit`


# Installation mysqlclient in conda virtualenv mlflow-env 
`pip install mysqlclient`

# connect to mlflow server
`mlflow server --host 0.0.0.0 --port 5004 --backend-store-uri mysql://mlflow_user:password@localhost/mlflow_db --default-artifact-root $PWD/mlruns`  # checked, this one can connect 
- note: Replace root:admin123 with mlflow_user:password to use the mlflow_user credentials.
- Database Name: Change db_mlflow to mlflow_db to match the database name you’ve created and granted mlflow_user access to.
- run python loan_prediction (note the port need to match above)


# connect wsl database from windows 
## Edit the MySQL Configuration: 
- In WSL, open the MySQL configuration file (my.cnf or mysqld.cnf) with a text editor. 
`sudo nano /etc/mysql/mysql.conf.d/mysqld.cnf`
- Update the bind-address:
Find the line with bind-address and change its value to 0.0.0.0:
`bind-address = 0.0.0.0`  
- Restart MySQL:
`sudo service mysql restart`

- Step 2: Find the WSL IP Address
`ip addr`
Look for the inet value under the eth0 interface, which might look like 192.168.x.x.; mine is    inet 172.25.23.53 -- the IP address of my WSL instance is 172.25.23.53


## connect wsl 
- download mysql  Workbench for windows
- Click on the "+" symbol beside MySQL Connections to add a new connection.
- In the Connection Name field, give your connection a meaningful name, something like "WSL MySQL".
For the Hostname, enter 172.25.23.53 (the IP address of my WSL instance).
- The Port should remain as the default MySQL port 3306. Note this is different from mlflow port, no need to change. 
- In the Username field, enter mlflow_user, or whichever MySQL user you have designated to access the mlflow_db database.
- Click on the Store in Vault button to enter and save the password for mlflow_user, which is 'password'.
- Click on the Test Connection button to verify that MySQL Workbench can successfully connect to your MySQL instance running in WSL.

## Troubleshooting - FAIL to connect
`fail to connect to MYSQL at 172.25.23.53:3306 with user mlflow_user`
`host 'zzz_alien.mshome.net' is not allowed to connect to this MySQL server`

- The error message receiving indicates that the mlflow_user MySQL user doesn't have permission to connect to the MySQL server from the host zzz_alien.mshome.net. 

- Grant Permissions to the User from the Specific Host

- start sql in terminal
`sudo mysql -u root -p`
`CREATE USER 'mlflow_user'@'zzz_alien.mshome.net' IDENTIFIED BY 'password';`
`GRANT ALL PRIVILEGES ON mlflow_db.* TO 'mlflow_user'@'zzz_alien.mshome.net';`
`FLUSH PRIVILEGES;`
`exit`

- then connect in workbench again 


# if you want to run using using MLFlow project file 
- CHANGE TO THE right port
`export MLFLOW_TRACKING_URI=http://0.0.0.0:5004`
- run mlflow file
`mlflow run . --experiment-name Loan_prediction`

# How you can serve the model and make prediction on the given data
- since all models are present in 5004 port, ensure tracking uri is point the same port : CHANGE TO THE right port
`export MLFLOW_TRACKING_URI=http://0.0.0.0:5004`
- command to serve the model is: 
`mlflow models serve -m "models:/model_name@alias" `  # see instruction: https://www.mlflow.org/docs/latest/model-registry.html#migrating-from-stages 

` mlflow models serve -m "models:/prediction_RF/1" -p 1234 ` # set port 1234 just try




