# Frontend Development Guide

## Overview

The frontend is a React application built with Vite that provides a user interface for submitting and viewing feedback.

## Project Structure

```
frontend/
├── src/
│   ├── components/
│   │   ├── FeedbackForm.jsx      # Form component for submission
│   │   └── FeedbackList.jsx      # Display feedback list
│   ├── App.jsx                   # Main application component
│   ├── api.js                    # API communication utilities
│   ├── index.css                 # Global styles
│   └── main.jsx                  # Application entry point
├── index.html                    # HTML template
├── package.json                  # Dependencies and scripts
├── vite.config.js               # Vite configuration
└── .gitignore                   # Git ignore rules
```

## Component Architecture

### App Component

**File**: `src/App.jsx`

**Purpose**: Main application wrapper and state coordinator

**Features**:

- Manages refresh trigger state
- Coordinates communication between FeedbackForm and FeedbackList
- Renders page layout and title

**Props**: None

**State**:

- `refreshTrigger` - Triggers FeedbackList refresh after submission

### FeedbackForm Component

**File**: `src/components/FeedbackForm.jsx`

**Purpose**: Handles user input and form submission

**Features**:

- Form state management
- Client-side validation
- Loading states
- Success/error feedback
- API communication

**Props**:

- `onFeedbackSubmitted` (function) - Callback when feedback is submitted

**State**:

- `formData` - Form field values
- `errors` - Validation error messages
- `isLoading` - Loading indicator
- `successMessage` - Success notification

**Validation**:

- All fields required
- Message minimum 10 characters
- Empty strings not allowed

### FeedbackList Component

**File**: `src/components/FeedbackList.jsx`

**Purpose**: Displays all submitted feedback

**Features**:

- Loading state display
- Error handling
- Empty state message
- Auto-refresh on form submission
- Timestamp formatting

**Props**:

- `refreshTrigger` (number) - Triggers list refresh

**State**:

- `feedbackList` - Array of feedback items
- `isLoading` - Loading indicator
- `error` - Error message

## API Communication

### api.js

Contains utility functions for HTTP communication:

#### `getAllFeedback()`

- **Method**: GET
- **Endpoint**: `/api/feedback`
- **Returns**: Array of feedback objects
- **Error Handling**: Logs and throws errors

#### `submitFeedback(feedback)`

- **Method**: POST
- **Endpoint**: `/api/feedback`
- **Payload**:
  ```javascript
  {
    name: string,
    subject: string,
    message: string
  }
  ```
- **Returns**: Created feedback object with id and timestamp
- **Error Handling**: Logs and throws errors with messages

## Styling

### Approach

CSS-in-CSS using a single global stylesheet

### Features

- Gradient background
- Responsive design
- Smooth animations
- Interactive elements
- Loading spinner
- Valid/error states

### Color Scheme

- Primary: `#667eea` (Purple-blue)
- Secondary: `#764ba2` (Dark purple)
- Success: `#27ae60` (Green)
- Error: `#e74c3c` (Red)

## Development Workflow

### Setup

```bash
cd frontend
npm install
npm run dev
```

### Available Scripts

- `npm run dev` - Start development server (port 5173)
- `npm run build` - Build for production
- `npm run preview` - Preview production build

### Hot Module Replacement

Vite provides automatic reload on file changes during development.

## Performance Tips

1. **Component Memoization**: Use React.memo for expensive components
2. **State Management**: Keep state close to components that use it
3. **API Calls**: Minimize number of requests to backend
4. **CSS**: Already minified in production build

## Debugging

### Browser DevTools

1. Open DevTools: F12
2. **Network Tab**: Monitor HTTP requests
3. **Console Tab**: View JavaScript errors
4. **Elements Tab**: Inspect HTML and CSS

### React DevTools

1. Install React DevTools extension
2. View component hierarchy
3. Inspect props and state
4. Track re-renders

## Browser Compatibility

- Chrome/Edge 90+
- Firefox 88+
- Safari 14+
- Requires ES6 support

## Common Issues

### CORS Errors

- Ensure backend is running on port 5000
- Verify CORS is enabled in Flask
- Check allowed origins in backend config

### Network Errors

- Verify backend API is accessible at http://localhost:5000
- Check firewall settings
- Verify correct API endpoint URLs

### State Issues

- Use React DevTools to inspect state
- Check console for error messages
- Verify prop passing between components
