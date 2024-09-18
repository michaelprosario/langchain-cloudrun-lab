# langchain-cloudrun-lab

# reference
- https://python.langchain.com/v0.2/docs/tutorials/rag/
- https://www.digitalocean.com/community/tutorials/how-to-install-and-use-sqlite-on-ubuntu-20-04


# How do we build the docker container and name the image langchain-lab1?

```
docker build -t langchain-lab1 .
```

# How do we run an instance of langchain-lab1?

```
docker run -d -p 8000:8000 -e GOOGLE_API_KEY="fixme" -e LANGCHAIN_TRACING_V2=true -e LANGCHAIN_ENDPOINT="https://api.smith.langchain.com" -e LANGCHAIN_API_KEY="fixme" langchain-lab1
```

* -d: This flag runs the container in detached mode, meaning it runs in the background.
* -p 8000:8000: This option maps port 80 of the host machine to port 80 of the container. This allows access to the container's services via port 80 on the host machine.
* -e GOOGLE_API_KEY="fixme": This sets an environment variable GOOGLE_API_KEY inside the container with the value "fixme".
* -e LANGCHAIN_TRACING_V2=true: This sets an environment variable LANGCHAIN_TRACING_V2 inside the container with the value true.
* -e LANGCHAIN_ENDPOINT="https://api.smith.langchain.com": This sets an environment variable LANGCHAIN_ENDPOINT inside the container with the value "https://api.smith.langchain.com".
* -e LANGCHAIN_API_KEY="fixme": This sets an environment variable LANGCHAIN_API_KEY inside the container with the value "fixme".
* langchain-lab1: This is the name of the Docker image to use for creating the container.