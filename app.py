from flask import Flask
from threading import Thread
from Logging_Module.logging_generator import generate_random_log
from log_monitor import monitor_bp

# Create a Flask application instance
app = Flask(__name__)

# Register the blueprint for log monitoring
app.register_blueprint(monitor_bp)

# Start log generation in a separate thread
log_generator_thread = Thread(target=generate_random_log)
log_generator_thread.daemon = True
log_generator_thread.start()

if __name__ == '__main__':
    app.run(debug=True)
