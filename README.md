# langchain-cloudrun-lab

# Review of solution files
- docker-compose.yaml: A docker-compose.yaml file is used by Docker Compose to define and manage multi-container Docker applications. It allows you to configure your application's services, networks, and volumes in a single file. In this application, we are specifying an image for execution and an environment variable.
- Dockerfile: A Dockerfile is a script that contains a series of instructions on how to build a Docker image. Each instruction in the Dockerfile creates a layer in the image, and when you build the image, Docker executes these instructions in sequence. 
- requirements.txt: A requirements.txt file is used in Python projects to list all the dependencies (external libraries and packages) that the project needs to run. This file allows you to specify the exact versions of the packages required, ensuring that the project runs consistently across different environments.

# How do we build the docker container and name the image langchain-lab1?

```
docker build -t langchain-lab1 .
```

# How do we run an instance of langchain-lab1?

- Amend the docker-compose.yaml.  
- Fix environment variables: GOOGLE_API_KEY and LANGCHAIN_API_KEY

```
docker-compose up
```

If you want to have docker-compose run the service in the background, use the following:
```
docker-compose up -d
```

# reference
- https://codelabs.developers.google.com/codelabs/cloud-run-deploy?hl=en#0
- https://python.langchain.com/docs/tutorials/llm_chain/


