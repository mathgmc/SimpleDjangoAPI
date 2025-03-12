# SimpleDjangoAPI

SimpleDjangoAPI is a basic CRUD API built using Django and Django REST Framework.

## Features
- Create, Read, Update, and Delete (CRUD) operations for items.
- RESTful API with Django REST Framework.
- Uses Django models and serializers for data handling.

## Installation

### Steps

1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/SimpleDjangoAPI.git
   cd SimpleDjangoAPI
   ```

2. Create and activate a virtual environment:
   ```sh
   python -m venv venv
   source venv/bin/activate
   ```

3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

4. Apply migrations:
   ```sh
   python manage.py migrate
   ```

5. Run the development server:
   ```sh
   python manage.py runserver
   ```

## API Endpoints

| Method | Endpoint          | Description |
|--------|------------------|-------------|
| GET    | `/items/`        | Retrieve all items |
| POST   | `/items/`        | Create a new item |
| GET    | `/items/{id}/`   | Retrieve a specific item by ID |
| PUT    | `/items/{id}/`   | Update an existing item by ID |
| DELETE | `/items/{id}/`   | Delete an item by ID |

## Usage

You can test the API using tools like [Postman](https://www.postman.com/) or cURL. Example request to get all items:

```sh
curl -X GET http://127.0.0.1:8000/items/
```
