# langchain-cloudrun-lab

# reference
- https://python.langchain.com/v0.2/docs/tutorials/rag/
- https://www.digitalocean.com/community/tutorials/how-to-install-and-use-sqlite-on-ubuntu-20-04


# How do we build the docker container and name the image langchain-lab1?

```
docker build -t langchain-lab1 .
```

# How do we run an instance of langchain-lab1?

- Amend the docker-compose.yaml.  
- Fix environment variables: GOOGLE_API_KEY and LANGCHAIN_API_KEY

```
docker-compose up -d
```

