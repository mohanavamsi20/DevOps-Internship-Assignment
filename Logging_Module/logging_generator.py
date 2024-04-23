import random
import logging
import time
from datetime import datetime

# Configure logging
logging.basicConfig(filename='Logging_Module/app.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Create a logger
logger = logging.getLogger(__name__)

# Define logger levels and their corresponding HTTP status codes
logger_levels = {
    "FATAL": 500,
    "ERROR": 404,
    "WARN": 302,
    "INFO": 200,
    "DEBUG": 101,
    "TRACE": 100,
    "NOTICE": 201,
    "CRITICAL": 503,
    "ALERT": 429,
    "EMERGENCY": 500
}

# Define log messages templates
log_messages = {
    "FATAL": "Critical error: Database connection failed. Application terminated.",
    "ERROR": "Error: Requested resource not found.",
    "WARN": "Warning: Redirecting to a different URL.",
    "INFO": "Request processed successfully.",
    "DEBUG": "Debug: Switching protocols for WebSocket communication.",
    "TRACE": "Trace: Received 'Continue' response, proceeding with the request.",
    "NOTICE": "Notice: New resource created successfully.",
    "CRITICAL": "Critical: Service unavailable due to high traffic.",
    "ALERT": "Alert: Rate limit exceeded. Too many requests.",
    "EMERGENCY": "Emergency: Server crashed due to memory overflow."
}

# Function to generate a random log message and write it to the log file
def generate_random_log():
    """
    Function to generate a random log message and write it to the log file.

    This function runs indefinitely, generating random log messages
    with random log levels and corresponding HTTP status codes.
    """
    while True:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        level = random.choice(list(logger_levels.keys()))
        http_code = logger_levels[level]
        message = log_messages[level]
        log_message = f"{timestamp} - {level} - {message} - HTTP Status Code: {http_code}"
        logging.log(logger_levels[level], log_message)
        time.sleep(1)

# Run log generation continuously
if __name__ == "__main__":
    generate_random_log()
