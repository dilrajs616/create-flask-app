# create-flask-app

`create-flask-app` is a command-line tool that helps developers quickly setup a basic Flask web application with a basic directory structure and virtual environment setup. With just one command, you can create a fully-functional Flask app, install dependencies, and get started with development immediately.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Directory Structure](#directory-structure)
- [Virtual Environment](#virtual-environment)
- [How It Works](#how-it-works)
- [Requirements](#requirements)
- [Contributing](#contributing)
- [License](#license)

## Features

- Automatically creates a project folder with Flask's recommended directory structure.
- Sets up a Python virtual environment inside the project.
- Provides a simple `app.py` file with a working Flask app.
- Includes a sample `index.html` file in the templates folder to get you started with a basic HTML view.
- Includes index.css that has the styling for the index page

## Installation

To install `create-flask-app`, follow these steps:

1. Clone the repository or download the source code:
   ```bash
   git clone https://github.com/dilrajs616/create-flask-app.git
   cd create-flask-app
   ```

2. (Optional) Create a virtual environment to isolate the package dependencies:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install the package locally:
   ```bash
   pip install .
   ```

After the installation is complete, you can use the `create-flask-app` command to setup new Flask applications.

## Usage

To generate a new Flask application, run the following command in your terminal:

```bash
create-flask-app <app-name>
```

For example:

```bash
create-flask-app my-flask-app
```

This will create a new folder called `my-flask-app` containing the Flask app's structure, a virtual environment, and a `requirements.txt` file.

### Steps:
1. **Navigate to the new folder**: After running the command, `cd` into the newly created folder:
   ```bash
   cd my-flask-app
   ```

2. **Activate the virtual environment**:
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

3. **Run the app**:
   Start the development server:
   ```bash
   python app.py
   ```

4. Visit the app in your browser:
   - Open [http://127.0.0.1:5000](http://127.0.0.1:5000) to view the running Flask app.

## Directory Structure

The generated Flask app will have the following structure:

```bash
my-flask-app/
├── venv/               # Virtual environment directory
├── static/             # css files
│   └── index.css       # Static files like CSS, JS, images
├── templates/          # HTML templates
│   └── index.html      # Sample template
├── app.py              # Main Flask app script
└── requirements.txt    # Installed dependencies (including Flask)
```

### Virtual Environment

A Python virtual environment is automatically created inside your project folder (`venv/`). This isolates your project's dependencies from your global Python environment.

You can activate the virtual environment using the following commands:

- **Windows**:
  ```bash
  venv\Scripts\activate
  ```

- **macOS/Linux**:
  ```bash
  source venv/bin/activate
  ```

After activation, any installed packages, such as Flask, will be isolated within this environment.

### requirements.txt

A `requirements.txt` file is generated after Flask is installed. This file lists the installed packages in your virtual environment. You can install the dependencies in another environment by running:

```bash
pip install -r requirements.txt
```

## How It Works

- The `create-flask-app` script:
  1. Creates a new folder with the specified app name.
  2. Sets up a Python virtual environment in the folder.
  3. Installs Flask in the virtual environment.
  4. Creates the required Flask app structure (`app.py`, `static/`, `templates/`).
  5. Generates a simple `index.html` file and a `requirements.txt` file.

## Requirements

- Python 3.6 or higher
- `pip` (Python's package installer)
- Virtual environment (`venv`)

Make sure you have Python installed and `pip` set up correctly on your machine. If you're unsure, you can check your Python version by running:

```bash
python --version
```

## Contributing

Contributions are welcome! If you'd like to improve the tool or add new features, feel free to open an issue or submit a pull request. Here's how you can contribute:

1. Fork the repository.
2. Create a new branch for your feature (`git checkout -b feature/new-feature`).
3. Make your changes and commit (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature/new-feature`).
5. Create a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
```

### Explanation of Sections

1. **Features:** Highlights what the tool does.
2. **Installation:** Explains how to install the package and optionally activate a virtual environment.
3. **Usage:** Detailed instructions on how to run the tool, activate the virtual environment, and start the Flask app.
4. **Directory Structure:** Describes the structure of the generated app.
5. **Virtual Environment:** Explains what the virtual environment does and how to activate it.
6. **How It Works:** A behind-the-scenes explanation of what the tool does.
7. **Requirements:** Lists the prerequisites (Python 3.6+, pip, etc.).
8. **Contributing:** Guidelines for contributing to the project.
9. **License:** Information about the license of the project (MIT in this case).

You can customize the text and links as per your needs. Let me know if you'd like any further details added!