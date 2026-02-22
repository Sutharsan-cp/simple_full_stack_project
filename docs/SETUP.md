# Setup and Installation Guide

## Prerequisites

Before starting, ensure you have the following installed:

1. **Node.js** (v16 or higher)
   - Download: https://nodejs.org/
   - Verify: `node --version` and `npm --version`

2. **Python** (v3.8 or higher)
   - Download: https://www.python.org/
   - Verify: `python --version`

3. **PostgreSQL** (v12 or higher)
   - Download: https://www.postgresql.org/
   - Verify: `psql --version`

4. **Git** (optional, for version control)
   - Download: https://git-scm.com/

## Step-by-Step Installation

### 1. Create PostgreSQL Database

#### On Windows with Command Prompt:

```bash
# Open PostgreSQL command line
psql -U postgres

# Inside psql:
CREATE DATABASE fullstack_demo;
\q
```

#### On Windows with PowerShell:

```powershell
# Open as Administrator
psql -U postgres -c "CREATE DATABASE fullstack_demo;"
```

#### On macOS/Linux:

```bash
psql -U postgres -c "CREATE DATABASE fullstack_demo;"
```

**Note**: If prompted for password, the default is usually blank or 'postgres'.

### 2. Setup Backend (Flask)

Open PowerShell/Terminal in the `backend` folder:

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Start the server
python app.py
```

**Expected Output**:

```
✅ Connected to database: fullstack_demo
✅ Feedback table ready
🚀 Starting Full Stack Demo API server...
API will be available at http://0.0.0.0:5000/api
```

✅ **Backend is running at**: `http://localhost:5000`

### 3. Setup Frontend (React)

Open a new PowerShell/Terminal in the `frontend` folder:

```bash
# Install dependencies
npm install

# Start development server
npm run dev
```

**Expected Output**:

```
  VITE v4.x.x  ready in xxx ms

  ➜  local:   http://localhost:5173/
```

✅ **Frontend is running at**: `http://localhost:5173`

### 4. Test the Application

1. Open browser to `http://localhost:5173`
2. Fill out the feedback form and submit
3. You should see the feedback appear in the list below
4. Check that both services are working together

🎉 **Congratulations!** Your full-stack application is running!

## Configuration

### Backend Configuration (if needed)

Edit `backend/config.py` to change:

```python
# Database credentials
DB_CONFIG = {
    'dbname': 'fullstack_demo',
    'user': 'postgres',
    'password': 'postgres',  # Change if needed
    'host': 'localhost',
    'port': '5432'
}

# API settings
PORT = 5000  # Change if port is already in use
```

### Frontend Configuration (if needed)

API endpoint is defined in `frontend/src/api.js`:

```javascript
const API_BASE_URL = "http://localhost:5000/api";
```

Change if backend is on different port/machine.

## Troubleshooting

### Issue: Database connection error

**Solution**:

1. Verify PostgreSQL is running
2. Check database exists: `psql -U postgres -l | grep fullstack_demo`
3. Verify credentials in `backend/config.py`

### Issue: Port 5000 already in use

**Solution**:

1. Change `PORT` in `backend/config.py`
2. Update API URL in `frontend/src/api.js`
3. Restart both servers

### Issue: Port 5173 already in use

**Solution**:
Edit `frontend/vite.config.js` and change port:

```javascript
server: {
    port: 5174,  // Change to different port
    host: true
}
```

### Issue: Virtual environment not found

**Solution**:

```bash
cd backend
python -m venv venv
venv\Scripts\activate  # Windows
# or
source venv/bin/activate  # macOS/Linux
pip install -r requirements.txt
```

### Issue: npm install fails

**Solution**:

```bash
# Clear npm cache
npm cache clean --force

# Delete node_modules and package-lock.json
rm -r node_modules package-lock.json

# Reinstall dependencies
npm install
```

### Issue: CORS error in browser console

**Solution**:

1. Verify backend is running
2. Check backend CORS configuration in `backend/config.py`
3. Ensure frontend URL is in `CORS_ORIGINS`

## Stopping the Services

### Stop Backend

In backend terminal: Press `Ctrl+C`

### Stop Frontend

In frontend terminal: Press `Ctrl+C`

## Verification Checklist

- [ ] PostgreSQL database created
- [ ] Backend virtual environment activated
- [ ] Backend dependencies installed
- [ ] Backend server running (port 5000)
- [ ] Frontend dependencies installed
- [ ] Frontend server running (port 5173)
- [ ] Can open http://localhost:5173 in browser
- [ ] Can submit feedback without errors
- [ ] Submitted feedback appears in the list

## Next Steps

1. Review the [Architecture Guide](ARCHITECTURE.md) to understand the three-tier design
2. Explore [Frontend Development](FRONTEND.md) for UI/UX details
3. Explore [Backend Development](BACKEND.md) for API details
4. Experiment with modifying the code
5. Try adding new features (edit, delete, search)

## Additional Resources

- [MDN HTTP Guide](https://developer.mozilla.org/en-US/docs/Web/HTTP)
- [React Documentation](https://react.dev/)
- [Flask Documentation](https://flask.palletsprojects.com/)
- [PostgreSQL Tutorial](https://www.postgresql.org/docs/current/tutorial.html)
- [REST API Design Guide](https://restfulapi.net/)
