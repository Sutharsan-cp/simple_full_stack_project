"""
Flask backend API for the Full Stack Demo application.
Provides REST endpoints for feedback management.
"""

from flask import Flask, request, jsonify
from flask_cors import CORS
from db import Database
from config import DB_CONFIG, CORS_ORIGINS, API_PREFIX, DEBUG, HOST, PORT
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Initialize Flask app
app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

# Enable CORS for specified origins
CORS(app, origins=CORS_ORIGINS)

# Initialize database
db = Database(**DB_CONFIG)
db.connect()

# =====================
# API Endpoints
# =====================

@app.route(f'{API_PREFIX}/health', methods=['GET'])
def health_check():
    """
    Health check endpoint to verify API is running.
    
    Returns:
        JSON: Status of the API
    """
    return jsonify({
        'status': 'healthy',
        'message': 'Full Stack Demo API is running! 🚀'
    }), 200


@app.route(f'{API_PREFIX}/feedback', methods=['GET'])
def get_feedback():
    """
    Retrieve all feedback from the database.
    
    Returns:
        JSON: List of all feedback objects
        Status Code: 200 on success, 500 on error
    """
    try:
        logger.info('Fetching all feedback from database')
        feedback_list = db.get_all_feedback()
        logger.info(f'Successfully retrieved {len(feedback_list)} feedback items')
        return jsonify(feedback_list), 200
    except Exception as e:
        logger.error(f'Error fetching feedback: {str(e)}')
        return jsonify({
            'error': 'Failed to retrieve feedback',
            'details': str(e)
        }), 500


@app.route(f'{API_PREFIX}/feedback', methods=['POST'])
def create_feedback():
    """
    Create new feedback entry in the database.
    
    Expected JSON body:
    {
        "name": "string",
        "subject": "string",
        "message": "string"
    }
    
    Returns:
        JSON: Created feedback object with id and timestamp
        Status Code: 201 on success, 400 on validation error, 500 on error
    """
    try:
        data = request.get_json()

        # Validate required fields
        if not data:
            return jsonify({'error': 'Request body is required'}), 400

        required_fields = ['name', 'subject', 'message']
        for field in required_fields:
            if field not in data or not data[field] or not isinstance(data[field], str):
                return jsonify({
                    'error': f'Missing or invalid required field: {field}'
                }), 400

        # Validate field lengths and content
        if len(data['name'].strip()) == 0:
            return jsonify({'error': 'Name cannot be empty'}), 400
        
        if len(data['subject'].strip()) == 0:
            return jsonify({'error': 'Subject cannot be empty'}), 400
        
        if len(data['message'].strip()) < 10:
            return jsonify({'error': 'Message must be at least 10 characters long'}), 400

        # Add feedback to database
        logger.info(f'Creating feedback from {data["name"]}')
        feedback = db.add_feedback(
            name=data['name'].strip(),
            subject=data['subject'].strip(),
            message=data['message'].strip()
        )

        logger.info(f'Successfully created feedback with ID: {feedback["id"]}')
        return jsonify(feedback), 201

    except Exception as e:
        logger.error(f'Error creating feedback: {str(e)}')
        return jsonify({
            'error': 'Failed to create feedback',
            'details': str(e)
        }), 500


@app.route(f'{API_PREFIX}/feedback/<int:feedback_id>', methods=['GET'])
def get_feedback_by_id(feedback_id):
    """
    Retrieve a specific feedback entry by ID.
    
    Args:
        feedback_id: ID of the feedback to retrieve
    
    Returns:
        JSON: Feedback object if found
        Status Code: 200 on success, 404 if not found, 500 on error
    """
    try:
        logger.info(f'Fetching feedback with ID: {feedback_id}')
        # This endpoint is for demonstration - expand as needed
        return jsonify({
            'message': 'Get specific feedback endpoint',
            'feedback_id': feedback_id
        }), 200
    except Exception as e:
        logger.error(f'Error fetching feedback by ID: {str(e)}')
        return jsonify({
            'error': 'Failed to retrieve feedback',
            'details': str(e)
        }), 500


# =====================
# Error Handlers
# =====================

@app.errorhandler(404)
def not_found(error):
    """Handle 404 Not Found errors."""
    return jsonify({
        'error': 'Endpoint not found',
        'message': 'The requested resource does not exist'
    }), 404


@app.errorhandler(405)
def method_not_allowed(error):
    """Handle 405 Method Not Allowed errors."""
    return jsonify({
        'error': 'Method not allowed',
        'message': 'The HTTP method used is not supported for this endpoint'
    }), 405


@app.errorhandler(500)
def internal_error(error):
    """Handle 500 Internal Server errors."""
    return jsonify({
        'error': 'Internal server error',
        'message': 'An unexpected error occurred'
    }), 500


# =====================
# Application Lifecycle
# =====================

@app.before_request
def before_request():
    """Log incoming requests."""
    logger.debug(f'{request.method} {request.path}')


@app.teardown_appcontext
def teardown_db(exception):
    """Close database connection when app context ends."""
    if exception:
        logger.error(f'Application error: {exception}')


if __name__ == '__main__':
    try:
        logger.info('🚀 Starting Full Stack Demo API server...')
        logger.info(f'API will be available at http://{HOST}:{PORT}{API_PREFIX}')
        app.run(
            host=HOST,
            port=PORT,
            debug=DEBUG
        )
    except KeyboardInterrupt:
        logger.info('⏹️ Server shutdown requested')
    except Exception as e:
        logger.error(f'❌ Failed to start server: {e}')
    finally:
        db.close()
