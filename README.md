# RoBERTa Sequence Classification Flask App

## Overview

This project is a Flask-based application for performing sequence classification using a fine-tuned RoBERTa model. The app is containerized with Docker and integrated with Azure Machine Learning to retrieve the model. It also supports CI/CD using GitHub Actions to automate the build and deployment of the Docker container to Docker Hub.

## Features

- **Model Retrieval**: The model is downloaded from Azure Machine Learning Workspace.
- **Dockerized Deployment**: The application is containerized for easy deployment.
- **CI/CD Pipeline**: GitHub Actions automate the build, test, and push to Docker Hub.
- **Flask API**: Exposes an endpoint for sequence classification.

## Prerequisites

### Tools

- Python 3.9.21
- Docker
- Azure CLI
- GitHub account for CI/CD

### Azure Resources

- Azure Machine Learning Workspace
- Registered Model in Azure ML (e.g., `roberta-sequence`)
- Azure Active Directory service principal with `Contributor` role

## Project Structure

```
project-root
|-- webapp
|   |-- app.py                # Flask app file
|   |-- requirements.txt      # Python dependencies
|   |-- roberta-sequence-classification-9.onnx  # Model (retrieved during workflow)
|-- Dockerfile                # Docker configuration
|-- .github/workflows
|   |-- main.yml              # GitHub Actions workflow
|-- README.md                 # Project documentation
```

## Setting Up the Project

### Step 1: Clone the Repository

```bash
git clone https://github.com/your-repo-name/roberta-sequence-app.git
cd roberta-sequence-app
```

### Step 2: Create and Activate a Virtual Environment

```bash
python3.9 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r webapp/requirements.txt
```

### Step 4: Test Locally

Run the Flask app locally:

```bash
python webapp/app.py
```

Test the endpoint with curl:

```bash
curl -X POST -H "Content-Type: application/json" \
--data '["This is a test sequence"]' \
http://127.0.0.1:5000/predict
```

### Step 5: Build Docker Container

```bash
docker build -t flask-roberta:latest .
```

Run the container locally:

```bash
docker run -it -p 5000:5000 flask-roberta
```

## CI/CD Workflow with GitHub Actions

### Secrets Configuration

Set the following secrets in your GitHub repository:

- `AZURE_CREDENTIALS`: Azure service principal credentials (JSON format).
- `AZURE_WORKSPACE_NAME`: Name of your Azure ML workspace.
- `AZURE_RESOURCE_GROUP`: Azure resource group name.
- `DOCKER_USERNAME`: Docker Hub username.
- `DOCKER_PASSWORD`: Docker Hub access token.

### GitHub Actions Workflow

The CI/CD pipeline defined in `.github/workflows/main.yml` performs the following steps:

1. Checks out the repository.
2. Authenticates with Azure using the provided credentials.
3. Downloads the model from Azure ML Workspace.
4. Moves the model to the `webapp` directory.
5. Builds and pushes the Docker container to Docker Hub.

Trigger the workflow by pushing to the `main` branch or manually through the Actions tab.

## Deployment

You can deploy the container to any Docker-compatible environment, such as:

- **Azure App Service**
- **Google Cloud Run**
- **AWS Elastic Container Service (ECS)**

Example: Running the container in Azure Container Instances (ACI):

```bash
az container create \
  --resource-group YOUR_RESOURCE_GROUP \
  --name flask-roberta \
  --image YOUR_DOCKER_USERNAME/flask-roberta:latest \
  --cpu 1 \
  --memory 1 \
  --ports 5000 \
  --environment-variables ENV_VAR_NAME=value
```

## Endpoint Usage

### Endpoint: `/predict`

- **Method**: POST
- **Content-Type**: `application/json`
- **Request Body**: A JSON array with a single sequence to classify (e.g., `{"sequence": "text to classify"}`).
- **Response**: JSON object with the classification result (e.g., `{ "positive": true }`).

## Contributing

Feel free to open issues or submit pull requests to improve the project.

## License

This project is licensed under the MIT License.

## Contact

For questions or support, please contact:

- **Name**: Ifeanyi Nwaneri
- **Email**: [Nwaneriifeanyi89@gmail.com](mailto\:Nwaneriifeanyi89@gmail.com)




