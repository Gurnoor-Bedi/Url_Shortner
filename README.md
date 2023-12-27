# Url_Shortner
# Flask URL Shortener

This repository contains a Flask web application that provides a simple interface for shortening URLs using the `pyshorteners` library.

## Features

- Web interface for easy URL shortening.
- Uses the TinyURL service for creating short links.

## Usage

The application provides a simple web interface where users can enter a URL to be shortened. After submission, the shortened URL is displayed and can be easily copied or clicked on.

## Installation and Setup

### Prerequisites

- Python 3
- Flask
- pyshorteners

### Steps

1. Clone the repository or download the source code.
2. Ensure Python 3 is installed on your system.
3. Install Flask and pyshorteners using pip:
    ```bash
    pip install Flask pyshorteners
    ```

### Running the Application

1. Navigate to the application directory.
2. Run the application using:
    ```bash
    python app.py
    ```
3. Open a web browser and go to `http://127.0.0.1:5000/`.

## Application Structure

- `app.py`: The main Flask application script.
- `templates/index.html`: HTML template for the main page.
- `templates/result.html`: HTML template for displaying the shortened URL.

## Contributing

Feel free to fork the repository, make changes, and submit pull requests. Contributions to improve the application or add new features are always welcome.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

---

Note: The README provides a basic guide on how to set up and run your Flask web application. You might need to adjust the instructions based on your specific setup or additional files you might have in your project.
