API Task Manager 
## Summary 

This is a simple FastAPI backend that manages tasks through a REST API. All tasks are stored in a plain text file using JSON Lines format (one task per line). The goal was to understand backend basics, file storage, and CRUD operations without using a database.

## How data is stored 

Each task is saved as one JSON object per line inside `tasks.txt`.

Ex: 

{"id":1,"title":"Learn FastAPI","description":"Watch tutorial","completed":false}
{"id":2,"title":"Buy groceries","description":"Milk","completed":true}

## Task Model

Each task has:
- `id` (auto-generated, starts at 1)
- `title` (required)
- `description` (optional)
- `completed` (default: false)

## How to Run

Install dependencies:
pip install fastapi uvicorn
Run the server:
uvicorn main:app --reload
Open in browser:
http://127.0.0.1:8000/docs

# Endpoints 

- GET `/` → check if API works
- GET `/tasks` → get all tasks
- GET `/tasks/{id}` → get one task
- POST `/tasks` → create task
- PUT `/tasks/{id}` → update task
- DELETE `/tasks/{id}` → delete one task
- DELETE `/tasks` → delete all tasks
- GET `/tasks/stats` → task statistics
