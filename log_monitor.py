from flask import Blueprint, render_template
from Logging_Module.logging_generator import logger_levels,log_messages
import os

# Create a Blueprint for monitoring routes
monitor_bp = Blueprint('monitor', __name__)

def read_log_file(log_file_path):
    """
    Function to read log file and return its content as a list of lines.

    Args:
    log_file_path (str): Path to the log file.

    Returns:
    list: List of lines read from the log file.
    """
    with open(log_file_path, 'r') as file:
        lines = file.readlines()
    return lines

def generate_summary(log_lines):
    """
    Function to generate a summary of log file contents.

    Args:
    log_lines (list): List of log lines read from the log file.

    Returns:
    dict: Dictionary containing various summary statistics such as total lines, error count, warning count, 
          log level counts, and log level messages.
    """
    total_lines = len(log_lines)
    error_count = 0
    warning_count = 0
    log_level_counts = {level: 0 for level in logger_levels}

    for line in log_lines:
        for level, code in logger_levels.items():
            if level in line:
                log_level_counts[level] += 1

    log_level_messages = {level: [] for level in logger_levels}

    for level, message in log_messages.items():
        if log_level_counts[level] > 0:
            log_level_messages[level] = [message] * log_level_counts[level]

    return {
        'total_lines': total_lines,
        'error_count': error_count,
        'warning_count': warning_count,
        'log_level_counts': log_level_counts,
        'log_level_messages': log_level_messages
    }


@monitor_bp.route('/')
def display_log_and_summary():
    """
    Route to display log and its summary.

    Returns:
    str: Rendered template displaying log lines and summary, or an error message if encountered.
    """
    log_file_path = 'Logging_Module/app.log'  # Adjusted log file path
    if not os.path.exists(log_file_path):
        return "Log file not found."
    
    try:
        log_lines = read_log_file(log_file_path)
        summary = generate_summary(log_lines)
    except Exception as e:
        return f"An error occurred: {str(e)}"
    
    return render_template('log_summary.html', log_lines=log_lines, summary=summary)

@monitor_bp.route('/logs/<log_level>')
def display_log_by_level(log_level):
    """
    Route to display logs for a specific log level.

    Args:
    log_level (str): The log level for which logs are to be displayed.

    Returns:
    str: Rendered template displaying logs for the specified log level, or an error message if encountered.
    """
    log_file_path = 'Logging_Module/app.log'  # Adjusted log file path
    if not os.path.exists(log_file_path):
        return "Log file not found."

    try:
        log_lines = read_log_file(log_file_path)
        logs_for_level = [line for line in log_lines if log_level in line]
    except Exception as e:
        return f"An error occurred: {str(e)}"

    return render_template('log_level.html', log_level=log_level, logs=logs_for_level)