# Setup Virtual Environment

```python
conda create -n jenkins-env python=3.10 -y
conda activate jenkins-env
pip install -r requirements.txt   / pip install -r src/requirements.txt 
pip install .    /    pip install src/.   # installing prediction_model

# check whether the model is installed 
python
import prediction_model
from prediction_model.training_pipeline import perform_training  # import a function
perform_training()  # it will show  ' Model has been saved under the name classification.pkl '
```

# build the FASTAPI 
main.py
``` where to check: 
http://localhost:8005/docs
```


# Test the FASTAPI at http://localhost:8005/docs 

```json

{
  "Gender": "Male",
  "Married": "No",
  "Dependents": "2",
  "Education": "Graduate",
  "Self_Employed": "No",
  "ApplicantIncome": 5849,
  "CoapplicantIncome": 0,
  "LoanAmount": 1000,
  "Loan_Amount_Term": 1,
  "Credit_History": "1.0",
  "Property_Area": "Rural"
}

# Test in Postman 
http://localhost:8005/prediction_api



```

# Docker Commands
```
docker build -t loan_pred:v1 .        ## build dockerimage, run cmd in the directory where dockerfile is present ; dot "." in the cmd, refer to current directory 

docker images            ## check whether image is built

docker build -t manifoldailearning/cicd:latest .     ## for instructional purpose, push this to docker help
docker build -t zzzhen1130/cicd:latest .    #

docker push manifoldailearning/cicd:latest    #  pushing image to docker registry, change it to own account repository 
docker push zzzhen1130/cicd:latest     # modify to push to my own account repository named cicd


docker run -d -it --name modelv1 -p 8005:8005 manifoldailearning/cicd:latest bash    ## build container modelv1.  '-it' means interactive mode , change it to my own repository 
docker run -d -it --name modelv1 -p 8005:8005 zzzhen1130/cicd:latest bash  

docker exec modelv1 python prediction_model/training_pipeline.py   # inside modelv1 docker container, excute python 

docker exec modelv1 pytest -v --junitxml TestResults.xml --cache-clear  # once training complete, excute test, "junitxml" mean nomatter what result it is , save it as xml format

docker cp modelv1:/code/src/TestResults.xml .  # save test result to local directory 

docker exec -d -w /code modelv1 python main.py  # run the FASTAPI application in docker container , check http://localhost:8005/ 

docker exec -d -w /code modelv1 uvicorn main:app --proxy-headers --host 0.0.0.0 --port 8005


```

# Installation of Jenkins

```bash
curl -fsSL https://pkg.jenkins.io/debian-stable/jenkins.io-2023.key | sudo tee \
  /usr/share/keyrings/jenkins-keyring.asc > /dev/null
echo deb [signed-by=/usr/share/keyrings/jenkins-keyring.asc] \
  https://pkg.jenkins.io/debian-stable binary/ | sudo tee \
  /etc/apt/sources.list.d/jenkins.list > /dev/null
sudo apt-get update
sudo apt-get install jenkins

sudo apt update
sudo apt install fontconfig openjdk-17-jre
java -version

sudo systemctl enable jenkins
sudo systemctl start jenkins
sudo systemctl status jenkins
```

`
sudo cat /var/lib/jenkins/secrets/initialAdminPassword
`

```bash
# Add Docker's official GPG key:
sudo apt-get update
sudo apt-get install ca-certificates curl gnupg
sudo install -m 0755 -d /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
sudo chmod a+r /etc/apt/keyrings/docker.gpg

# Add the repository to Apt sources:
for pkg in docker.io docker-doc docker-compose podman-docker containerd runc; do sudo apt-get remove $pkg; done

echo \
  "deb [arch="$(dpkg --print-architecture)" signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
  "$(. /etc/os-release && echo "$VERSION_CODENAME")" stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin

sudo usermod -a -G docker jenkins
sudo usermod -a -G docker $USER

```

# Admin password Jenkins

`sudo cat /var/lib/jenkins/secrets/initialAdminPassword`

# Payload URL format in github repo webhook

`http://<public-ipv4 address>:8080/github-webhook/` #replace it with ur own public-ipv4 address

```

# Additional Improvements

docker remove $(docker ps -a -q)
docker images --format "{{.ID}} {{.CreatedAt}}" | sort -rk 2 | awk 'NR==1{print $1}'



# Create Stage Branch
`git checkout -b staging`
`git push `



