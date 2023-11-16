# TodoList Project

This project is a simple TodoList API built using Flask and MongoDB.

## Prerequisites

Before you begin, ensure that you have the following installed:

- Python
- Flask
- Flask-RESTful
- pymongo
- python-dotenv

You also need a MongoDB database. You can set the connection string in a `.env` file using the variable `uri`.

The API will be accessible at http://localhost:5000.

API Endpoints:
# Get all tasks
curl http://localhost:5000/todo

# Get a specific task by ID
curl http://localhost:5000/todo/<task_id>

# Create a new task
curl -X POST -H "Content-Type: application/json" -d '{"tasks":"New Task", "summary":"Task Summary"}' http://localhost:5000/todo

# Delete a task by ID
curl -X DELETE http://localhost:5000/todo/<task_id>
