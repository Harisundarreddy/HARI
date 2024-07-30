### project description

- User signup and login
- Search users by email and name
- Send, accept, and reject friend requests
- List friends and pending friend requests
- Rate limiting on sending friend requests

## Installation

1. **Clone the repository:**

    ```sh
    git clone <repository-url>
    cd <repository-directory>
    ```

2. **Build and run the Docker containers:**

    ```sh
    docker-compose up --build
    ```

3. **Run database migrations:**

    ```sh
    docker-compose run web python manage.py migrate
    ```

4. **Create a superuser (optional, for accessing Django admin):**

    ```sh
    docker-compose run web python manage.py createsuperuser
    ```

5. **Access the application:**

    The API will be accessible at `http://localhost:8000/`.

## API Endpoints

### Authentication

- **Signup**: `POST /signup/`
    - Request Body:
        ```json
        {
            "email": "hari@social.com",
            "password": "123"
        }
        ```

- **Login**: `POST /login/`
    - Request Body:
        ```json
        {
            "email": "hari@social.com",
            "password": "123"
        }
        ```

### Users

- **Search Users**: `GET /search/?q=<keyword>`
    

## Postman Collection

Import the provided Postman collection (included in the repository) for quick testing of the API endpoints.

## Docker Commands

- **Build and run containers**: `docker-compose up --build`
- **Run migrations**: `docker-compose run web python manage.py migrate`
- **Create superuser**: `docker-compose run web python manage.py createsuperuser`
- **Stop containers**: `docker-compose down`

