# Backend Development Guide

## Overview

The backend is a Flask API server that manages data persistence and provides REST endpoints for the frontend application.

## Project Structure

```
backend/
├── app.py              # Flask application and API routes
├── db.py               # Database connection and operations
├── config.py           # Configuration settings
├── requirements.txt    # Python package dependencies
├── .env.example        # Example environment variables
├── .gitignore          # Git ignore rules
└── README.md           # Setup instructions
```

## Configuration

### config.py

Contains all configuration settings:

- Flask settings (DEBUG, HOST, PORT)
- Database credentials (update before deployment)
- CORS allowed origins
- API prefix

### Environment Setup

Copy `.env.example` to `.env` and update values:

```
DB_NAME=fullstack_demo
DB_USER=postgres
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432
```

## Database Layer (db.py)

### Database Class

Manages PostgreSQL connection and operations.

#### `__init__(**db_config)`

Initialize database connection parameters.

#### `connect()`

Establish connection to PostgreSQL and create tables.

#### `_create_tables()`

Automatically creates the feedback table schema if not exists.

**Schema**:

```sql
CREATE TABLE feedback (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    subject VARCHAR(255) NOT NULL,
    message TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

#### `add_feedback(name, subject, message)`

Insert new feedback record.

**Parameters**:

- `name` (str): User's name
- `subject` (str): Feedback subject
- `message` (str): Feedback content

**Returns**: Dictionary with id, name, subject, message, created_at

**Exceptions**: Raises psycopg2.Error on database error

#### `get_all_feedback()`

Retrieve all feedback records.

**Returns**: List of dictionaries ordered by creation date (newest first)

**Exceptions**: Raises psycopg2.Error on database error

#### `close()`

Close database connection.

## Flask Application (app.py)

### Configuration

```python
app = Flask(__name__)
CORS(app, origins=CORS_ORIGINS)  # Enable cross-origin requests
```

### API Endpoints

#### Health Check

```
GET /api/health
Response: 200 OK
{
    "status": "healthy",
    "message": "Full Stack Demo API is running! 🚀"
}
```

#### Get All Feedback

```
GET /api/feedback
Response: 200 OK
[
    {
        "id": 1,
        "name": "John Doe",
        "subject": "Great application",
        "message": "This is a great learning project!",
        "created_at": "2024-02-22T10:30:00"
    },
    ...
]
```

Errors:

- 500 Internal Server Error

#### Create Feedback

```
POST /api/feedback
Content-Type: application/json

{
    "name": "Jane Smith",
    "subject": "Feedback",
    "message": "This is my feedback message."
}

Response: 201 Created
{
    "id": 2,
    "name": "Jane Smith",
    "subject": "Feedback",
    "message": "This is my feedback message.",
    "created_at": "2024-02-22T10:35:00"
}
```

Validation Errors:

- 400 Bad Request - Missing required fields
- 400 Bad Request - Invalid field values
- 400 Bad Request - Message too short (< 10 characters)

Server Errors:

- 500 Internal Server Error - Database error

#### Get Specific Feedback

```
GET /api/feedback/<id>
Response: 200 OK
{
    "message": "Get specific feedback endpoint",
    "feedback_id": 1
}
```

### Request Validation

The backend validates all incoming data:

1. **Required Fields**: name, subject, message
2. **Field Types**: All must be strings
3. **Field Content**:
   - Name: Cannot be empty
   - Subject: Cannot be empty
   - Message: Minimum 10 characters, cannot be empty

4. **Trimming**: All strings are trimmed of whitespace

## Error Handling

### HTTP Status Codes

- 200 OK - Request successful
- 201 Created - Resource created successfully
- 400 Bad Request - Client error (validation)
- 404 Not Found - Endpoint doesn't exist
- 405 Method Not Allowed - Wrong HTTP method
- 500 Internal Server Error - Server error

### Error Response Format

```json
{
  "error": "Error title",
  "message": "Detailed error message"
}
```

### Error Handlers

- `404` - Endpoint not found
- `405` - Method not allowed
- `500` - Internal server error

## Logging

Configured to log:

- Info messages (requests, database operations)
- Debug messages (request details)
- Error messages (exceptions and failures)

Log format: `[timestamp] - [logger] - [level] - [message]`

## Database Operations

### CREATE Operation

```python
feedback = db.add_feedback(
    name="Student Name",
    subject="Feedback Subject",
    message="Feedback message content"
)
```

### READ Operation

```python
all_feedback = db.get_all_feedback()
```

## Lifecycle Hooks

### Before Request

Logs incoming requests for debugging.

### After Request

Not used in current version.

### Teardown Context

Closes database connection on application shutdown.

## Security Features

1. **Input Validation**: All inputs validated before database insertion
2. **CORS Configuration**: Restricted to specified origins
3. **Prepared Statements**: Uses parameterized queries to prevent SQL injection
4. **Error Sanitization**: Sensitive info not exposed in error messages
5. **Logging**: All operations logged for audit trail

## Performance Considerations

1. **Connection Pooling**: psycopg2 handles connection management
2. **Query Optimization**: Ordered by creation date for efficient retrieval
3. **JSON Serialization**: Datetime objects converted to ISO format strings
4. **Batch Operations**: Could be optimized for bulk inserts

## Testing

### Health Check

```bash
curl http://localhost:5000/api/health
```

### Get Feedback

```bash
curl http://localhost:5000/api/feedback
```

### Create Feedback

```bash
curl -X POST http://localhost:5000/api/feedback \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Test User",
    "subject": "Test Subject",
    "message": "This is a test feedback message."
  }'
```

## Troubleshooting

### Database Connection Error

- Verify PostgreSQL is running
- Check credentials in config.py
- Ensure database exists

### CORS Error

- Verify frontend URL is in CORS_ORIGINS
- Check Flask-CORS is installed

### Port Already in Use

- Change PORT in config.py
- Or kill process using port 5000

### Import Errors

- Verify virtual environment is activated
- Run `pip install -r requirements.txt`
