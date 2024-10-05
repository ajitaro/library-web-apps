# Library Web App Documentation

## Overview

This documentation provides instructions for setting up and running the Library Web App. It covers the required environment, installation of dependencies, database migration, and how to run the application.

## Environment Requirements

Before you start, ensure that you have Python 3 installed on your local machine. You can download Python from the official [Python website](https://www.python.org/downloads/).

### Creating a Virtual Environment

Using a virtual environment is a good practice to manage dependencies for your project. To create a virtual environment, follow these steps:

1. Navigate to your project directory.
2. Run the following command to create a virtual environment named `venv`:

   ```bash
   python -m venv venv
   ```

### Activating the Virtual Environment

Once you have created the virtual environment, activate it using the instructions below.

#### On macOS/Linux

```bash
source venv/bin/activate
```

#### On Windows

```bash
venv\Scripts\activate
```

## Install Dependencies

Once your virtual environment is activated, install the necessary dependencies for the project. Run the following command:

```bash
pip install -r requirements.txt
```

This command reads the `requirements.txt` file and installs the required packages.

## Database Migration

After installing the dependencies, you'll need to set up your database. Run the following command to apply migrations:

```bash
python manage.py migrate
```

This command creates the necessary database tables and sets up your application’s database schema.

## Running the Application

Now that everything is set up, you can run the application. Use the following command:

```bash
python manage.py runserver
```

The server will start, and you should see output indicating that the development server is running. You can access the application by navigating to `http://127.0.0.1:8000/` in your web browser.
