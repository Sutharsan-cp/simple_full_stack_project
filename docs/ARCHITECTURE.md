# Architecture Guide

## Three-Tier Architecture

This project follows a **three-tier architecture** pattern, separating concerns into distinct layers:

```
┌─────────────────────────────────────────────────────────────────┐
│                         Frontend Layer                           │
│                       React (Port 5173)                          │
│  - UI Components (FeedbackForm, FeedbackList)                   │
│  - State Management                                              │
│  - HTTP Communication (fetch)                                    │
└──────────────────────────┬──────────────────────────────────────┘
                           │ HTTP/JSON
                           ▼
┌─────────────────────────────────────────────────────────────────┐
│                       Backend Layer                              │
│                     Flask (Port 5000)                            │
│  - REST API Endpoints                                            │
│  - Request Validation                                            │
│  - Database Operations                                           │
│  - CORS Configuration                                            │
└──────────────────────────┬──────────────────────────────────────┘
                           │ SQL/psycopg2
                           ▼
┌─────────────────────────────────────────────────────────────────┐
│                       Database Layer                             │
│                 PostgreSQL (Port 5432)                           │
│  - Data Storage                                                  │
│  - Data Persistence                                              │
│  - Data Integrity                                                │
└─────────────────────────────────────────────────────────────────┘
```

## Data Flow

### Submitting Feedback

1. **Frontend**: User enters data in `FeedbackForm` component
2. **Validation**: Client-side validation in React component
3. **HTTP Request**: `POST /api/feedback` with JSON payload
4. **Backend**: Flask receives and validates the request
5. **Database**: Data is stored in PostgreSQL
6. **Response**: Backend returns created feedback with ID and timestamp
7. **UI Update**: Frontend updates state and shows success message

### Retrieving Feedback

1. **Frontend**: Component mounts, calls `getAllFeedback()`
2. **HTTP Request**: `GET /api/feedback`
3. **Backend**: Flask queries the database
4. **Database**: PostgreSQL returns all feedback records
5. **Response**: Backend returns JSON array of feedback
6. **UI Update**: React renders feedback list

## Layer Responsibilities

### Frontend Layer (React)

**Location**: `frontend/src`

**Responsibilities**:

- User interface rendering
- Form state management
- Input validation
- HTTP communication via fetch API
- Immediate user feedback

**Key Files**:

- `App.jsx` - Main application component
- `components/FeedbackForm.jsx` - Form handling
- `components/FeedbackList.jsx` - Display feedback
- `api.js` - HTTP communication utilities

### Backend Layer (Flask)

**Location**: `backend/`

**Responsibilities**:

- API endpoint definition
- HTTP request processing
- Request validation
- Database operations
- Error handling
- CORS configuration

**Key Files**:

- `app.py` - Flask application and API routes
- `db.py` - Database connection and operations
- `config.py` - Configuration settings

### Database Layer (PostgreSQL)

**Location**: Local PostgreSQL instance

**Responsibilities**:

- Data storage
- Data retrieval
- Data integrity
- Concurrent access handling

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

## Communication Protocols

### Frontend ↔ Backend

**Protocol**: HTTP/JSON

**Methods Used**:

- `GET /api/feedback` - Retrieve all feedback
- `POST /api/feedback` - Create new feedback

**Data Format**: JSON

```json
{
  "name": "string",
  "subject": "string",
  "message": "string"
}
```

### Backend ↔ Database

**Protocol**: SQL via psycopg2 driver

**Operations**:

- CREATE - Insert new feedback records
- READ - Query feedback records
- No UPDATE/DELETE in basic version

## Error Handling

### Frontend

- Validates user input before submission
- Catches network errors
- Displays user-friendly error messages
- Handles loading states

### Backend

- Validates request data
- Returns appropriate HTTP status codes
- Logs errors for debugging
- Returns JSON error responses

### Database

- Enforces column constraints
- Handles connection errors gracefully

## Security Considerations

1. **Input Validation**: Both frontend and backend validate input
2. **CORS**: Configured to allow only specified origins
3. **SQL Injection Prevention**: Uses parameterized queries
4. **Error Messages**: Avoid exposing sensitive information in production

## Performance Optimization

1. **Database Indexing**: Primary key index on feedback.id
2. **Connection Pooling**: Managed by psycopg2
3. **Frontend Caching**: React component state
4. **Timestamp Ordering**: Organizes feedback by creation time
