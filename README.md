# Project Title: AI-Powered Microservices for Data Processing and Summarization

This repository hosts a suite of microservices designed to leverage AI for various tasks, including summarizing GitHub contributions and processing documents stored in MinIO, subsequently indexing them into Weaviate. It utilizes Docker and Docker Compose for easy deployment and management of the services.

## Services Overview

### GitHub Contributions Summarizer

- **Purpose:** Summarizes recent GitHub contributions for a specified user.
- **Technology:** Python, Docker.

### LangChain-Weaviate-MinIO Service

- **Purpose:** Processes documents from MinIO storage, utilizing LangChain for NLP tasks, and indexes processed data into Weaviate.
- **Technology:** Python, FastAPI, Docker, MinIO, Weaviate.

## Project Structure

```
/top-level-repo
    /github-contributions-summarizer
        Dockerfile
        main.py
        requirements.txt
    /langchain-weaviate-minio-service
        Dockerfile
        main.py
        requirements.txt
    docker-compose.yml
    README.md
```

## Getting Started

### Prerequisites

- Docker
- Docker Compose

### Setup and Deployment

1. **Clone the Repository:**

```bash
git clone <repository-url>
cd <repository-name>
```

2. **Build and Run with Docker Compose:**

```bash
docker-compose up --build
```

This command builds the Docker images for each service and starts the containers as defined in `docker-compose.yml`.

## Usage

### GitHub Contributions Summarizer

Access the summarizer service at: `http://localhost:<port>/path-to-summarizer`

### LangChain-Weaviate-MinIO Service

The document processing service can be interacted with through its FastAPI endpoints, accessible at: `http://localhost:<port>/docs`

## Configuration

Configure environment variables for each service in `docker-compose.yml`. For example, set `GITHUB_API_KEY` for the GitHub Contributions Summarizer and MinIO/Weaviate credentials for the LangChain-Weaviate-MinIO Service.

## Contributing

Contributions are welcome! Please refer to the contributing guidelines for details on how to contribute to this project.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

---

Please replace `<repository-url>`, `<repository-name>`, and `<port>` with the actual URL of your repository, the name of your repository, and the ports you've configured for accessing the services. This README provides a basic outline; you might want to customize it further to fit your project's specifics, such as adding detailed usage examples, contributing guidelines, and any other relevant information.