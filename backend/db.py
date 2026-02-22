"""
Database configuration and connection management for the Full Stack Demo application.
Handles PostgreSQL connections and CRUD operations for feedback data.
"""

import psycopg
from datetime import datetime

class Database:
    """Database connection and operations manager."""

    def __init__(self, dbname='fullstack_demo', user='postgres', password='postgres', 
                 host='localhost', port='5432'):
        """
        Initialize database connection parameters.
        
        Args:
            dbname: PostgreSQL database name
            user: PostgreSQL username
            password: PostgreSQL password
            host: PostgreSQL host address
            port: PostgreSQL port number
        """
        self.dbname = dbname
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.connection = None

    def connect(self):
        """Establish connection to PostgreSQL database."""
        try:
            self.connection = psycopg.connect(
                dbname=self.dbname,
                user=self.user,
                password=self.password,
                host=self.host,
                port=self.port
            )
            print(f"✅ Connected to database: {self.dbname}")
            self._create_tables()
        except psycopg.Error as e:
            print(f"❌ Database connection error: {e}")
            raise

    def _create_tables(self):
        """Create feedback table if it doesn't exist."""
        try:
            with self.connection.cursor() as cursor:
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS feedback (
                        id SERIAL PRIMARY KEY,
                        name VARCHAR(255) NOT NULL,
                        subject VARCHAR(255) NOT NULL,
                        message TEXT NOT NULL,
                        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                    );
                """)
                self.connection.commit()
                print("✅ Feedback table ready")
        except psycopg.Error as e:
            print(f"❌ Error creating table: {e}")
            self.connection.rollback()

    def add_feedback(self, name, subject, message):
        """
        Add new feedback to the database.
        
        Args:
            name: Feedback author's name
            subject: Feedback subject
            message: Feedback message content
            
        Returns:
            dict: The created feedback object with id and timestamp
        """
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(
                    """
                    INSERT INTO feedback (name, subject, message, created_at)
                    VALUES (%s, %s, %s, %s)
                    RETURNING id, name, subject, message, created_at;
                    """,
                    (name, subject, message, datetime.now())
                )
                result = cursor.fetchone()
                self.connection.commit()
                
                # Convert result tuple to dictionary
                if result:
                    return {
                        'id': result[0],
                        'name': result[1],
                        'subject': result[2],
                        'message': result[3],
                        'created_at': result[4].isoformat() if isinstance(result[4], datetime) else result[4]
                    }
                return None
        except psycopg.Error as e:
            print(f"❌ Error adding feedback: {e}")
            self.connection.rollback()
            raise

    def get_all_feedback(self):
        """
        Retrieve all feedback from the database.
        
        Returns:
            list: List of all feedback objects, ordered by creation date (newest first)
        """
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(
                    """
                    SELECT id, name, subject, message, created_at
                    FROM feedback
                    ORDER BY created_at DESC;
                    """
                )
                results = cursor.fetchall()
                
                # Convert tuples to dictionaries
                feedback_list = []
                for row in results:
                    feedback_list.append({
                        'id': row[0],
                        'name': row[1],
                        'subject': row[2],
                        'message': row[3],
                        'created_at': row[4].isoformat() if isinstance(row[4], datetime) else row[4]
                    })
                
                return feedback_list
        except psycopg.Error as e:
            print(f"❌ Error retrieving feedback: {e}")
            raise

    def close(self):
        """Close database connection."""
        if self.connection:
            self.connection.close()
            print("✅ Database connection closed")
