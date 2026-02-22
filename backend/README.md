# Database Management Scripts

This directory contains Python scripts for database setup and management.

## Files

- **db.py**: Database connection manager and CRUD operations
- **app.py**: Flask API server with REST endpoints
- **config.py**: Configuration settings for the backend
- **requirements.txt**: Python package dependencies

## Setup Instructions

### 1. Create Python Virtual Environment

```bash
python -m venv venv
```

### 2. Activate Virtual Environment

**Windows:**

```bash
venv\Scripts\activate
```

**macOS/Linux:**

```bash
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Database

Update the database credentials in `config.py`:

```python
DB_CONFIG = {
    'dbname': 'fullstack_demo',
    'user': 'postgres',
    'password': 'your_password',  # Update this
    'host': 'localhost',
    'port': '5432'
}
```

### 5. Create PostgreSQL Database

```bash
psql -U postgres

CREATE DATABASE fullstack_demo;

\q
```

### 6. Run the Server

```bash
python app.py
```

The API will be available at `http://localhost:5000/api`

## API Endpoints

- `GET /api/health` - Health check
- `GET /api/feedback` - Get all feedback
- `POST /api/feedback` - Create new feedback
- `GET /api/feedback/<id>` - Get specific feedback

## Stopping the Server

Press `Ctrl+C` in the terminal running the Flask server.
