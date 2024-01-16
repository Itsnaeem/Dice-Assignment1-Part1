# Dice-Assignment1-Part1
This Assignment based on Docker. In this part We will create Docker File creation, GitHub and Docker Hub integration.

**Step 1 : Identify a Sample Application**
I choose a python Application which get random requests from web.

**Step 2 : Identify the Dependencies**
In this Application **request** & **Flask** dependency is used.

**Step 3 : Create a Docker file**
This is Dockerfile for above app.
# Use an official Python image
FROM python
# Set the Working Directory inside the container
WORkDIR /usr/scr/app
# Copy the current dictory into container directory /usr/scr/app
COPY . .
# install the dependency
RUN pip install -r requirements.txt
# Run the application
CMD ["python", "./random_fact.py"]

**Step 4 : Build the Docker Image**
I create a Docker image for this application using command below.
**docker build -t random_fact .**
The output of this command is :
naeem@naeempc:~/Downloads/DevOps Dice/Dice-Assignment1-Part1$ docker build -t random_fact .
[+] Building 8.0s (4/9)                                                                                                                             docker:defaultt
 => [internal] load build definition from Dockerfile                                                                                                          0.0ss
 => => transferring dockerfile: 353B                                                                                                                          0.0ss
 => [internal] load .dockerignore                                                                                                                             0.0ss
 => => transferring context: 2B                                                                                                                               0.0ss
 => [internal] load metadata for docker.io/library/python:latest                                                                                              7.6ss
 => [auth] library/python:pull token for registry-1.docker.io                                                                                                 0.0ss
 => [1/4] FROM docker.io/library/python@sha256:f964ddcb8416013f62f4b7a8c72a332ba4ccd284e39c263ea7bc0375ca8f2c4b                                               0.3ss
 => => resolve docker.io/library/python@sha256:f964ddcb8416013f62f4b7a8c72a332ba4ccd284e39c263ea7bc0375ca8f2c4b                                               0.0s[+] Building 8.1s (4/9)                                                                                                                            docker:default
 => [internal] load build definition from Dockerfile                                                                                                         0.0ss => => transferring dockerfile: 353B                                                                                                                         0.0s
 => [internal] load .dockerignore                                                                                                                            0.0ss => => transferring context: 2B                                                                                                                              0.0s
 => [internal] load metadata for docker.io/library/python:latest                                                                                             7.6s[+][[[[+[[[[+] Building 140.0s (10/10) FINISHED                                                                                                                         docker:default= => [internal] load build definition from Dockerfile                                                                                                                   0.0s
 => => transferring dockerfile: 353B                                                                                                                                   0.0s  => [internal] load .dockerignore                                                                                                                                      0.0s= => => transferring context: 2B                                                                                                                                        0.0s
 => [internal] load metadata for docker.io/library/python:latest                                                                                                       7.6s  => [auth] library/python:pull token for registry-1.docker.io                                                                                                          0.0s= => [1/4] FROM docker.io/library/python@sha256:f964ddcb8416013f62f4b7a8c72a332ba4ccd284e39c263ea7bc0375ca8f2c4b                                                      116.4s
 => => resolve docker.io/library/python@sha256:f964ddcb8416013f62f4b7a8c72a332ba4ccd284e39c263ea7bc0375ca8f2c4b                                                        0.0s  => => sha256:f964ddcb8416013f62f4b7a8c72a332ba4ccd284e39c263ea7bc0375ca8f2c4b 2.14kB / 2.14kB                                                                         0.0s= => => sha256:452d6aee6b77937f81f12ecafc3b76c94b072dee82efa784885ce5886ae8dfd6 2.01kB / 2.01kB                                                                         0.0s
 => => sha256:1b13d4e1a46e5e969702ec92b7c787c1b6891bff7c21ad378ff6dbc9e751d5d4 49.56MB / 49.56MB                                                                      34.3s  => => sha256:1c74526957fc2157e8b0989072dc99b9582b398c12d1dcd40270fd76231bab0c 24.05MB / 24.05MB                                                                      27.6s= => => sha256:ddb6e9772fb2b573c34540c334677d5e3b3783bcdc3639c4747ee4ce73e12abb 7.31kB / 7.31kB                                                                         0.0s
 => => sha256:8d55d1cb1ffb0c7e0438b372a96cc0f23a76c21571fa3e7b7b38e3fbc66a8c3a 64.14MB / 64.14MB                                                                      53.7s  => => sha256:aa8e0026efede8b3da7364fd0ec879657b2c9be209b5cc1e2ec83bed6dfcf6a9 211.10MB / 211.10MB                                                                   110.2s= => => sha256:a000d2c561b3e5538d3abf2f9bb93a61fa101a369efe94eb53d8f3b9e5f385ac 6.39MB / 6.39MB                                                                        38.3s
 => => extracting sha256:1b13d4e1a46e5e969702ec92b7c787c1b6891bff7c21ad378ff6dbc9e751d5d4                                                                              1.5s
 => => extracting sha256:1c74526957fc2157e8b0989072dc99b9582b398c12d1dcd40270fd76231bab0c                                                                              0.5s
 => => sha256:fd5581c776426d40ce604f496b508502b6269290d7958b6baed0369d39f09467 22.67MB / 22.67MB                                                                      53.2s
 => => sha256:6ba9b0f086f52558b1ebd98830a9de72206afcd21bdeba8266af4b8b26babc59 244B / 244B                                                                            54.6s
 => => extracting sha256:8d55d1cb1ffb0c7e0438b372a96cc0f23a76c21571fa3e7b7b38e3fbc66a8c3a                                                                              2.0s
 => => sha256:c924028f9b63738e825f0459b9af76fcab4c99cf0d14754ce2b32a8cb11ff080 2.68MB / 2.68MB                                                                        56.9s
 => => extracting sha256:aa8e0026efede8b3da7364fd0ec879657b2c9be209b5cc1e2ec83bed6dfcf6a9                                                                              5.0s
 => => extracting sha256:a000d2c561b3e5538d3abf2f9bb93a61fa101a369efe94eb53d8f3b9e5f385ac                                                                              0.2s
 => => extracting sha256:fd5581c776426d40ce604f496b508502b6269290d7958b6baed0369d39f09467                                                                              0.5s
 => => extracting sha256:6ba9b0f086f52558b1ebd98830a9de72206afcd21bdeba8266af4b8b26babc59                                                                              0.0s
 => => extracting sha256:c924028f9b63738e825f0459b9af76fcab4c99cf0d14754ce2b32a8cb11ff080                                                                              0.2s
 => [internal] load build context                                                                                                                                      0.6s
 => => transferring context: 30.99MB                                                                                                                                   0.5s
 => [2/4] WORKDIR /usr/scr/app                                                                                                                                         1.8s
 => [3/4] COPY . .                                                                                                                                                     2.9s
 => [4/4] RUN pip install -r requirements.txt                                                                                                                         10.7s
 => exporting to image                                                                                                                                                 0.4s 
 => => exporting layers                                                                                                                                                0.4s 
 => => writing image sha256:722e00083cf91ab7379e29ac57d8c0f029249c74ca84300ad4ab7e7f393e7b8f                                                                           0.0s 
 => => naming to docker.io/library/random_fact                                                                                                                         0.0s 
                                                                                                                                                                            
View build details: docker-desktop://dashboard/build/default/default/mqb7j2s2w5ro43v6beoref010

What's Next?
  View a summary of image vulnerabilities and recommendations → docker scout quickview

**Step 5 : Push the Docker Image to Docker Hub**
In this step, First I create DockerHub account using Docker Desktop. Provide the details & login in Docker Desktop. Now you can push your local image to your Docker Hub Account.
**docker images**
REPOSITORY    TAG       IMAGE ID       CREATED         SIZE
random_fact   latest    722e00083cf9   9 minutes ago   1.07GB
**docker tag random_fact:latest itsnaeemraza/python_app:v1.0**
This command is used for give the name to your image.
docker tag [image_name:tag] [username/app_with_version]
 docker tag random_fact:latest itsnaeemraza/python_app:v1.0
output is:
naeem@naeempc:~/Downloads/DevOps Dice/Dice-Assignment1-Part1$ docker images
REPOSITORY                TAG       IMAGE ID       CREATED          SIZE
itsnaeemraza/python_app   v1.0      722e00083cf9   12 minutes ago   1.07GB
random_fact               latest    722e00083cf9   12 minutes ago   1.07GB
Then 
Docker Login using the command : docker login 
Authenticating with existing credentials...
Login Succeeded
Then
Docker Push for push your local image to your Docker Hub.
docker push itsnaeemraza/python_app:v1.0
The push refers to repository [docker.io/itsnaeemraza/python_app]
18e43ee14add: Pushed 
7b41292b8762: Pushed 
2190825b34ed: Pushed 
d82f6b7598c5: Mounted from library/python 
70794eb73da1: Mounted from library/python 
ae6af2c8b8ae: Mounted from library/python 
3479e3189b94: Mounted from library/python 
671f9916da8d: Mounted from library/python 
2b952ea61c4b: Mounted from library/python 
0dfa23fffa41: Mounted from library/python 
aa904f36746c: Mounted from library/python 
v1.0: digest: sha256:660c3187b1781cac40c87799dcf14bb941ae0b733e5d66611e9eafb45c8d0968 size: 2637

This will also show in your Docker Desktop & in your browser & login into docker & click on repositories.

**Step 6 : Create a GitHub Repository**




