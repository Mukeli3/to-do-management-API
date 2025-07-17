# Todo Management API

A simple Flask-based Todo Management API with full CRUD functionality. Users can create, retrieve, update and delete tasks. SQLAlchemy is used to connect to a MySQL database and Flask-Migrate managing database schema changes.

## Project Structure

```
to-do-management-API/
│
├── app/
│   ├── __init__.py
│   ├── model.py
│   ├── routes.py
│
├── migrations/
├── run.py
├── requirements.txt
├── README.md
```

---

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/Mukeli3/to-do-management-API.git
cd to-do-management-API/
```

### 2. Create a Virtual Environment & Activate It

```bash
python3 -m venv venv
source venv/bin/activate        # Linux/macOS
# venv\Scripts\activate         # Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Database Migrations

Before running the app, set up and apply migrations:

```bash
# Initialize migrations folder (only once)
flask db init

# Create initial migration
flask db migrate -m "Initial migration"

# Apply migration to database
flask db upgrade
```

If models are later updated:

```bash
flask db migrate -m "Updated schema"
flask db upgrade
```

Make sure the `FLASK_APP` environment variable is set:

```bash
export FLASK_APP=run.py        # macOS/Linux
set FLASK_APP=run.py           # Windows CMD
$env:FLASK_APP="run.py"        # PowerShell
```

---

## Run the App

```bash
python run.py
```

The API will be available at: `http://127.0.0.1:5000`

---

## API Testing with curl

### Create a Todo

```bash
curl -X POST http://localhost:5000/todos \
-H "Content-Type: application/json" \
-d '{"title": "Buy groceries", "description": "Milk, eggs, bread"}'
```

**Expected Response:**

```json
{
  "id": 1,
  "title": "Buy groceries",
  "description": "Milk, eggs, bread",
  "status": "pending"
}
```

---

### Get All Todos

```bash
curl http://localhost:5000/todos
```

**Expected Response:**

```json
[
  {
    "id": 1,
    "title": "Buy groceries",
    "description": "Milk, eggs, bread",
    "status": "pending"
  }
]
```

---

### Update Todo Status

```bash
curl -X PUT http://localhost:5000/todos/1 \
-H "Content-Type: application/json" \
-d '{"status": "completed"}'
```

**Expected Response:**

```json
{
  "message": "To-do updated successfully"
}
```

---

### Delete a Todo

```bash
curl -X DELETE http://localhost:5000/todos/1
```

**Expected Response:**

```json
{
  "message": "To-do deleted successfully"
}
```

---

## Error Handling

* **Missing title or description:**

```json
{
  "error": "Title is required"
}
```

* **Todo not found:**

```json
{
  "error": "To-do not found"
}
```

---

## Status Field

* A new todo defaults to `"pending"`
* You can update status to `"completed"` or `"in progress"` using the update route

---

## Tech Stack

* Flask
* SQLAlchemy
* Flask-Migrate
* MySQL