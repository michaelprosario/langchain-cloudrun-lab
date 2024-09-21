
# langchain-cloudrun-lab

# Review of solution files

- docker-compose.yaml: A docker-compose.yaml file is used by Docker Compose to define and manage multi-container Docker applications. It allows you to configure your application's services, networks, and volumes in a single file. In this application, we are specifying an image for execution and an environment variable.

- Dockerfile: A Dockerfile is a script that contains a series of instructions on how to build a Docker image. Each instruction in the Dockerfile creates a layer in the image, and when you build the image, Docker executes these instructions in sequence.

- requirements.txt: A requirements.txt file is used in Python projects to list all the dependencies (external libraries and packages) that the project needs to run. This file allows you to specify the exact versions of the packages required, ensuring that the project runs consistently across different environments.

This tutorial guides you through deploying a sample Cloud Run service built with Langchain. We'll use the langchain-cloudrun-lab repository by Michael Rosario.
  
## Lab Agenda
 
## Tools you need
* Google cloud platform (obtain a trial account or billable account)
* Google Gemini API key ( obtain from https://ai.google.dev/aistudio )

## Optional tools for local testing

* Docker ( only needed for local testing ) - https://docs.docker.com/get-docker/
* Docker-compose ( only needed for local testing ) - https://docs.docker.com/compose/install/

## Review of key concepts
- Open [console.cloud.google.com](console.cloud.google.com)
- Tour of Google Cloud Console
- Explore editor in Google Cloud Console
- Deploying a Cloud Run Service with Langchain-Cloudrun-Lab

## Prerequisites:
* A Google Cloud account with billing enabled
* The Google Cloud CLI installed and configured ([https://cloud.google.com/sdk/docs/install](https://cloud.google.com/sdk/docs/install))
* Google Gemini Key - [https://ai.google.dev/aistudio](https://ai.google.dev/aistudio)


## Concept orientation

- This lab was adapted from the following source: https://codelabs.developers.google.com/codelabs/cloud-run-deploy?hl=en#0
- I do recommend that you read through steps 1 to 5 to underscore the concepts of the lab.

# Authenticate and Set Project

# List available accounts

 Open Google Cloud CLI.   

``` bash
gcloud  auth  list
```
Ensure that you have granted Google Cloud console access properly.
  

# Check currently configured project

``` bash
gcloud  config  list  project
```
 
# Set the project Id 
Replace `rosario-langchain3` with your project ID
``` bash
gcloud  config  set  project  rosario-langchain3
echo  $GOOGLE_CLOUD_PROJECT
```
This verifies you're authenticated to Google Cloud and sets the working project for subsequent commands.  

Enable Required Services
``` bash
gcloud  services  enable  \
aiplatform.googleapis.com \
cloudresourcemanager.googleapis.com  \
artifactregistry.googleapis.com \
cloudbuild.googleapis.com  \
run.googleapis.com \
secretmanager.googleapis.com
```
This enables the Google Cloud services required by the Langchain application (BigQuery, SQL Admin, AI Platform etc.).

Clone and Build the Application
``` bash
# Clone the Langchain Cloud Run Lab repository
git  clone  https://github.com/michaelprosario/langchain-cloudrun-lab
  
# Navigate to the project directory
cd  langchain-cloudrun-lab/

# Build the docker image and tag it with your project ID and version (replace 1.0.0 with your desired version)

gcloud  builds  submit  --tag  gcr.io/${GOOGLE_CLOUD_PROJECT}/rosario-langchain:1.0.0  .
```

This retrieves the project code, enables Cloud Build, and builds a Docker image with the specified tag.

Deploy to Cloud Run

# Deploy the container image to Cloud Run with these options:

 --image: Path to your container image (replace with the output from the previous step)
 --platform managed: Uses a managed Cloud Run environment
 --set-env-vars: Sets environment variables (replace fixme with actual values)
 --port: Specifies the port for incoming traffic

Note: Don't forget to update the environment variables (GOOGLE_API_KEY) with your actual credentials before deployment.  Replace the fixme below with your API key.
 
``` bash
gcloud  run  deploy  --image=gcr.io/${GOOGLE_CLOUD_PROJECT}/rosario-langchain:1.0.0  \
--platform managed --set-env-vars=GOOGLE_API_KEY=fixme \
--port=80
```

This deploys the built image to Cloud Run. Remember to replace fixme with your actual API keys for Gemini API Key

## Accessing the Application

Once the deployment finishes, you'll receive the service URL in the output. You can access your deployed Langchain application at that URL.

## Sources

*  [https://github.com/klummy/metabase-on-cloud-run](https://github.com/klummy/metabase-on-cloud-run)
*  __https://ai.google.dev/aistudio__
*  __https://codelabs.developers.google.com/codelabs/cloud-run-deploy?hl=en#0__
*  __https://python.langchain.com/docs/tutorials/llm_chain/__
*  __https://python.langchain.com/docs/integrations/platforms/google/__

# How do we build the docker container and name the image langchain-lab1?
```
docker build -t langchain-lab1 .
```
# How do we run an instance of langchain-lab1?

- Amend the docker-compose.yaml.
- Fix environment variables: GOOGLE_API_KEY

```
docker-compose up
```
If you want to have docker-compose run the service in the background, use the following:

```
docker-compose up -d
```

# reference

- https://ai.google.dev/aistudio
- https://codelabs.developers.google.com/codelabs/cloud-run-deploy?hl=en#0
- https://python.langchain.com/docs/tutorials/llm_chain/
- https://python.langchain.com/docs/integrations/platforms/google/
