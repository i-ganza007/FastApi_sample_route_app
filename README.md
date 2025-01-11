# FastAPI Task Management App

This is a simple task management API built using **FastAPI** and **Pydantic**. The app allows you to manage tasks, with functionality to create, read, and update tasks.

## Features

- **Create a task**: Add a new task with a title, description, and completed status.
- **Read all tasks**: Retrieve all the tasks in the system.
- **Get a task by ID**: Fetch a specific task using its unique ID.
- **Update a task**: Modify the details of an existing task.

## Technologies Used

- **FastAPI**: A modern web framework for building APIs with Python 3.6+.
- **Uvicorn**: ASGI server to run the FastAPI app.
- **Pydantic**: Data validation and settings management using Python type annotations.
- **UUID**: Universally Unique Identifier to give each task a unique ID.

## Installation

To run this application locally, you need Python 3.7+ and the following libraries:

1. Clone this repository:
   ```bash
   git clone <repository_url>
   cd <repository_directory>
   ```

2. Create a virtual environment:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the app using Uvicorn:
   ```bash
   uvicorn main:app --reload
   ```

   This will start the FastAPI app at `http://127.0.0.1:8000`.

## API Endpoints

### 1. Create a Task
- **Endpoint**: `POST /tasks/`
- **Request Body**:
  ```json
  {
    "title": "Sample Task",
    "description": "This is a sample task description.",
    "completed": false
  }
  ```
- **Response**: Returns the created task with a generated ID.

### 2. Get All Tasks
- **Endpoint**: `GET /tasks/`
- **Response**: Returns a list of all tasks.

### 3. Get a Task by ID
- **Endpoint**: `GET /tasks/{id}`
- **Request Parameters**: 
  - `id`: UUID of the task you want to retrieve.
- **Response**: Returns the task with the specified ID. If no task is found, returns a 404 error.

### 4. Update a Task
- **Endpoint**: `PUT /tasks/{id}`
- **Request Parameters**:
  - `id`: UUID of the task you want to update.
- **Request Body**:
  ```json
  {
    "title": "Updated Task Title",
    "description": "Updated task description.",
    "completed": true
  }
  ```
- **Response**: Returns the updated task.

## Example Usage

1. **Create a task**:
   ```bash
   curl -X 'POST' \
   'http://127.0.0.1:8000/tasks/' \
   -H 'Content-Type: application/json' \
   -d '{
   "title": "Sample Task",
   "description": "This is a sample task description.",
   "completed": false
   }'
   ```

2. **Get all tasks**:
   ```bash
   curl 'http://127.0.0.1:8000/tasks/'
   ```

3. **Get a task by ID**:
   ```bash
   curl 'http://127.0.0.1:8000/tasks/{task_id}'
   ```

4. **Update a task**:
   ```bash
   curl -X 'PUT' \
   'http://127.0.0.1:8000/tasks/{task_id}' \
   -H 'Content-Type: application/json' \
   -d '{
   "title": "Updated Task Title",
   "description": "Updated task description.",
   "completed": true
   }'
   ```

## Notes

- **UUID**: Each task is given a unique identifier (UUID) when it is created.
- **Task Fields**: 
  - `title` (required)
  - `description` (optional)
  - `completed` (optional, default is `false`)

## Contributing

Feel free to fork and submit pull requests. Contributions are welcome!

---

