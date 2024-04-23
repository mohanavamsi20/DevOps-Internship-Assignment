# Flask Logging Application

This Flask application demonstrates logging functionality along with a monitoring interface to view log files.

## Installation

1. Clone this repository:

    ```
    git clone <repository-url>
    ```

2. Navigate to the project directory:

    ```
    cd <project-directory>
    ```

3. Install the required dependencies:

    ```
    pip install -r requirements.txt
    ```

## Usage

### Running with Docker

1. Build the Docker image:

    ```
    docker build -t flask-app .
    ```

2. Run the Docker container:

    ```
    docker run -p 5000:5000 flask-app
    ```

The application will be accessible at `http://localhost:5000/`.

### Running without Docker

1. Ensure you have Python 3.x installed on your system.

2. Set up a virtual environment:

    ```
    python -m venv venv
    ```

3. Activate the virtual environment:

    - On Windows:

        ```
        venv\Scripts\activate
        ```

    - On macOS and Linux:

        ```
        source venv/bin/activate
        ```

4. Install dependencies:

    ```
    pip install -r requirements.txt
    ```

5. Run the Flask application:

    ```
    python app.py
    ```

The application will start running on `http://127.0.0.1:5000/`.

## File Structure

- `app.py`: Flask application setup and routes.
- `logging_generation.py`: Script to generate random log messages.
- `log_monitor.py`: Blueprint for monitoring routes.
- `templates/`: HTML templates for rendering log and summary views.
- `static/`: Static files such as CSS and JavaScript.

## Customization

You can customize the logging behavior, log file path, and log message templates according to your requirements by modifying the `logging_generation.py` script.

## Dependencies

- Flask: Web framework for Python.
- Python 3.x: Programming language.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
