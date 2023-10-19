# Create Your First Web App with Python and Flask

This is a beginner's guide to creating a simple web application using Python and Flask. Flask is a lightweight web framework that allows you to build web applications quickly and easily. By following this guide, you will learn how to set up a basic Flask application, create routes, handle HTTP requests, and render HTML templates.

## Prerequisites

Before getting started, make sure you have the following installed on your machine:

- Python (version 3.6 or higher)
- Flask (you can install it using pip: `pip install flask`)

## Getting Started

1. Create a new directory for your project.
2. Open a command prompt or terminal and navigate to the project directory.
3. Create a virtual environment (optional but recommended) by running the following command:

   ```shell
   python -m venv venv
   ```

4. Activate the virtual environment:

   - For Windows:

     ```shell
     venv\Scripts\activate
     ```

   - For macOS/Linux:

     ```shell
     source venv/bin/activate
     ```

5. Create a new Python file called `app.py` in the project directory.

## Setting Up the Flask Application

Open `app.py` in a text editor and add the following code:

```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run()
```

This code sets up a basic Flask application with a single route `/` that returns the string `'Hello, World!'` when accessed.

## Running the Application

To run the Flask application, make sure you are still in the project directory and the virtual environment is activated. Then, run the following command:

```shell
python app.py
```

You should see an output similar to:

```
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

This means your Flask application is running locally on `http://127.0.0.1:5000/`.

Open your web browser and navigate to `http://127.0.0.1:5000/`. You should see the message "Hello, World!" displayed in your browser.

## Creating Routes and Handling Requests

Flask allows you to create multiple routes to handle different URLs. Let's add a new route to handle a "About" page.

Add the following code to `app.py`:

```python
@app.route('/about')
def about():
    return 'This is the About page.'
```

Save the file and restart the Flask application if it's still running. Now, when you navigate to `http://127.0.0.1:5000/about`, you should see the message "This is the About page." displayed in your browser.

## Rendering HTML Templates

While returning plain text from routes is useful for simple responses, Flask also allows you to render HTML templates to create more complex web pages. Let's create an HTML template for the "About" page.

1. Create a new directory called `templates` in your project directory.
2. Inside the `templates` directory, create a new file called `about.html`.
3. Open `about.html` and add the following code:

   ```html
   <!doctype html>
   <html>
     <head>
       <title>About</title>
     </head>
     <body>
       <h1>About</h1>
       <p>This is the About page.</p>
     </body>
   </html>
   ```

4. Modify the `about` route in `app.py` to render the `about

.html` template:

   ```python
   from flask import render_template

   @app.route('/about')
   def about():
       return render_template('about.html')
   ```

Save both files and restart the Flask application. Now, when you navigate to `http://127.0.0.1:5000/about`, you should see the HTML page with the title "About" and the content "This is the About page."

## Conclusion

Congratulations! You have created your first web application using Python and Flask. You learned how to set up a basic Flask application, create routes to handle different URLs, handle HTTP requests, and render HTML templates. This is just the beginning, and Flask offers many more features to explore and build powerful web applications. Keep experimenting and learning, and enjoy building your web apps with Python and Flask!
