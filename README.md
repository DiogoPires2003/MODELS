# Car Dealership Mangement App Project

This project is a web application for a car dealership, built with Django and PostgreSQL, and containerized using Docker.

## Prerequisites

- Docker
- Docker Compose

## Setup

1. **Clone the repository**:
    ```sh
    git clone <repository_url>
    cd <repository_directory>
    ```

2. **Build and start the Docker containers**:
    ```sh
    docker-compose up --build

3. **Access the application**:
    Open a web browser and go to `http://localhost:8000`.

## Project Structure
- `myapp/templates/base.html`: Base HTML template for the application.
- `myapp/views.py`: Django views for the application.
- `Dockerfile`: Dockerfile for building the web application container.
- `docker-compose.yml`: Docker Compose configuration file.

## License

This project is licensed under the MIT License.
