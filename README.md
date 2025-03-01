# Car Dealership Project

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
    ```

3. **Apply database migrations**:
    ```sh
    docker-compose exec web python manage.py migrate
    ```

4. **Load initial data (if any)**:
    ```sh
    docker-compose exec web python manage.py loaddata initial_data.json
    ```

5. **Access the application**:
    Open a web browser and go to `http://localhost:8000`.

## Restore the Database

If you have a database dump (`backup.sql`), follow these steps to restore the database:

1. **Copy the `backup.sql` file** into the `db` container:
    ```sh
    docker cp backup.sql $(docker-compose ps -q db):/backup.sql
    ```

2. **Import the database**:
    ```sh
    docker-compose exec db psql -U django_user -d django_db -f /backup.sql
    ```

## Project Structure

- `myapp/templates/base.html`: Base HTML template for the application.
- `myapp/views.py`: Django views for the application.
- `Dockerfile`: Dockerfile for building the web application container.
- `docker-compose.yml`: Docker Compose configuration file.

## License

This project is licensed under the MIT License.
