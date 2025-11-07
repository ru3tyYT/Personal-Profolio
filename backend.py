"""
Portfolio Website Backend
A simple Flask server to serve the portfolio website
"""

from flask import Flask, send_file, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend-backend communication

# Route to serve the main HTML page
@app.route('/')
def index():
    """Serve the main portfolio HTML page"""
    return send_file('index.html')

# API endpoint to get project data (for future expansion)
@app.route('/api/projects')
def get_projects():
    """Return project information as JSON"""
    projects = [
        {
            'id': 1,
            'title': 'Custom Learning Website',
            'icon': '🌐',
            'description': [
                'Built with HTML & Python',
                'Custom system prompts tailored for student learning',
                'Interactive AI-powered education platform',
                'Similar to Gemini interface with educational focus'
            ],
            'link': None,
            'status': 'Private – Source code available for purchase'
        },
        {
            'id': 2,
            'title': 'Discord Support Bot',
            'icon': '🤖',
            'description': [
                'Advanced slash commands system',
                'Automated response handling',
                'AI integration with Gemini API',
                'Member verification system',
                'Intelligent moderation features'
            ],
            'link': 'https://github.com/ru3tyYT/Revolution-Support',
            'status': 'Closed source – Available for purchase'
        }
    ]
    return jsonify(projects)

# API endpoint to get typing animation words
@app.route('/api/typing-words')
def get_typing_words():
    """Return words for typing animation"""
    words = ['code', 'decompile', 'obfuscate', 'and more']
    return jsonify(words)

# Health check endpoint
@app.route('/health')
def health():
    """Health check endpoint"""
    return jsonify({'status': 'healthy', 'message': 'Portfolio backend is running'})

if __name__ == '__main__':
    # Check if index.html exists
    if not os.path.exists('index.html'):
        print("Warning: index.html not found in the current directory!")
        print("Please make sure index.html is in the same folder as backend.py")
    
    # Run the Flask application
    print("Starting Portfolio Backend Server...")
    print("Server will be available at: http://localhost:5000")
    print("Press CTRL+C to stop the server")
    
    # Run on all interfaces, port 5000
    app.run(host='0.0.0.0', port=5000, debug=True)
