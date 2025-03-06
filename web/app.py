from flask import Flask, render_template, jsonify
import json
import os
from datetime import datetime

# Single Responsibility Principle - Separate data handling from route handling
class FinancialDataService:
    """Responsible for loading and providing financial analysis data"""
    
    def __init__(self, data_file_path):
        self.data_file_path = data_file_path
    
    def get_analysis_data(self):
        """Get analysis data from file"""
        if not os.path.exists(self.data_file_path):
            return None
        
        with open(self.data_file_path, 'r') as f:
            return json.load(f)
    
    def data_exists(self):
        """Check if data file exists"""
        return os.path.exists(self.data_file_path)

# Creating the Flask application
app = Flask(__name__)
app.config['DATA_FILE'] = 'data/processed_analysis.json'

# Add Python built-in functions to Jinja environment
app.jinja_env.globals.update(
    min=min,
    max=max
)

# Initialize the data service
data_service = FinancialDataService(app.config['DATA_FILE'])

@app.route('/')
def index():
    """Main dashboard route"""
    analysis_data = data_service.get_analysis_data()
    
    if not analysis_data:
        return render_template('error.html', 
                              message="No analysis data available. Please run the main script first.")
    
    return render_template('index.html', 
                          analysis_data=analysis_data, 
                          last_updated=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

@app.route('/api/data')
def get_data():
    """API endpoint for raw data"""
    analysis_data = data_service.get_analysis_data()
    
    if not analysis_data:
        return jsonify({"error": "No data available"}), 404
    
    return jsonify(analysis_data)

@app.errorhandler(404)
def page_not_found(e):
    """Handle 404 errors"""
    return render_template('error.html', message="Page not found"), 404

@app.errorhandler(500)
def server_error(e):
    """Handle 500 errors"""
    return render_template('error.html', message="Server error occurred"), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)