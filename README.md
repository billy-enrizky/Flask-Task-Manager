# Task Manager Using Flask
# Project README

This project consists of a simple task manager web application developed using Flask, a micro web framework for Python. The application allows users to manage tasks, including adding, editing, and deleting tasks. It utilizes SQLAlchemy as an Object-Relational Mapping (ORM) tool to interact with a SQLite database.

## Project Structure

The project includes several files and directories:

### app.py

This is the main Python script that initializes the Flask application. It configures the secret key and database URI, sets up the SQLAlchemy database, and imports the routes from the `routes.py` file. The Flask app is run with debugging enabled when this script is executed.

### forms.py

This file defines Flask-WTF forms used in the application for user input. It includes forms for adding and editing tasks. These forms handle data validation and submission.

### models.py

The `models.py` file defines the database model used in the application. It includes a `Task` class with attributes such as `id`, `title`, `date`, and `desc` to represent tasks. This class is used for creating and querying the database.

### routes.py

In `routes.py`, you'll find the routes and views for the Flask application. It defines routes for displaying the task list, adding tasks, editing tasks, and deleting tasks. Views are implemented using Flask's render_template function.

### Templates (HTML files)

Several HTML templates are used to render the web pages. They include:

- **base.html:** The base template for all pages. It includes navigation links and handles message flashing.
- **add.html:** The template for adding a new task.
- **delete.html:** The template for confirming task deletion.
- **edit.html:** The template for editing an existing task.
- **index.html:** The main page displaying the list of tasks.

## Usage

To run the project:

1. Ensure you have Python and the required libraries installed.
2. Open your command-line interface.
3. Navigate to the project directory.
4. Execute `python app.py`.
5. Open a web browser and access the application at `http://127.0.0.1:5000/`.

## Dependencies

- Flask: A micro web framework for Python.
- Flask-WTF: An integration of the WTForms library for Flask.
- SQLAlchemy: A SQL toolkit and Object-Relational Mapping (ORM) library.
