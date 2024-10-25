import os
import sys
import subprocess
import platform

# Directory structure template
flask_structure = {
    'static': {
        'css': {
            'index.css': '''body {
    margin: 0;
    padding: 0;
    height: 100vh;
    display: flex;
    justify-content: center;
    align-items: center;
    background-color: #f4f4f4;
    flex-direction: column;
}

.container {
    margin-top: auto;
    text-align: center;
    background-color: white;
    padding: 20px;
    border-radius: 10px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

h1 {
    font-size: 36px;
    color: #333;
    margin-bottom: 20px;
}

img {
    width: 100px;
    height: auto;
}

footer {
    margin-top: auto;
    background-color: #f4f4f4;
    padding: 10px 0;
    text-align: center;
    width: 100%;
}'''
        },
        'js': {},
        'img': {}
    },
    'templates': {
        'index.html': '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Hello Flask App</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha3/dist/css/bootstrap.min.css" rel="stylesheet">
  <link rel="stylesheet" href="static/css/index.css">
</head>
<body>
  <div class="container">
    <h1>Hello Flask App</h1>
    <img src="https://upload.wikimedia.org/wikipedia/commons/3/3c/Flask_logo.svg" alt="Flask Logo">
  </div>

  <footer>
    <p class="text-muted">Credit: Dilraj Singh</p>
  </footer>

  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha3/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
''',
    },
    'app.py': '''from flask import Flask, render_template
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

@app.route('/')
def home():
    return render_template('index.html')
                    
# write more routes here

if __name__ == '__main__':
    app.run(debug=True)
''',
    'config.py':'''import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'a_very_secret_key'
    # set up other variables like database uri and debug value
''',
    '.gitignore': '''
# Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]
*$py.class

# C extensions
*.so

# Distribution / packaging
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
share/python-wheels/
*.egg-info/
.installed.cfg
*.egg
MANIFEST

# PyInstaller
#  Usually these files are written by a python script from a template
#  before PyInstaller builds the exe, so as to inject date/other infos into it.
*.manifest
*.spec

# Installer logs
pip-log.txt
pip-delete-this-directory.txt

# Unit test / coverage reports
htmlcov/
.tox/
.nox/
.coverage
.coverage.*
.cache
nosetests.xml
coverage.xml
*.cover
*.py,cover
.hypothesis/
.pytest_cache/
cover/

# Translations
*.mo
*.pot

# Django stuff:
*.log
local_settings.py
db.sqlite3
db.sqlite3-journal

# Flask stuff:
instance/
.webassets-cache

# Scrapy stuff:
.scrapy

# Sphinx documentation
docs/_build/

# PyBuilder
.pybuilder/
target/

# Jupyter Notebook
.ipynb_checkpoints

# IPython
profile_default/
ipython_config.py

# pyenv
#   For a library or package, you might want to ignore these files since the code is
#   intended to run in multiple environments; otherwise, check them in:
# .python-version

# pipenv
#   According to pypa/pipenv#598, it is recommended to include Pipfile.lock in version control.
#   However, in case of collaboration, if having platform-specific dependencies or dependencies
#   having no cross-platform support, pipenv may install dependencies that don't work, or not
#   install all needed dependencies.
#Pipfile.lock

# poetry
#   Similar to Pipfile.lock, it is generally recommended to include poetry.lock in version control.
#   This is especially recommended for binary packages to ensure reproducibility, and is more
#   commonly ignored for libraries.
#   https://python-poetry.org/docs/basic-usage/#commit-your-poetrylock-file-to-version-control
#poetry.lock

# pdm
#   Similar to Pipfile.lock, it is generally recommended to include pdm.lock in version control.
#pdm.lock
#   pdm stores project-wide configurations in .pdm.toml, but it is recommended to not include it
#   in version control.
#   https://pdm.fming.dev/latest/usage/project/#working-with-version-control
.pdm.toml
.pdm-python
.pdm-build/

# PEP 582; used by e.g. github.com/David-OConnor/pyflow and github.com/pdm-project/pdm
__pypackages__/

# Celery stuff
celerybeat-schedule
celerybeat.pid

# SageMath parsed files
*.sage.py

# Environments
.env
.venv
env/
venv/
ENV/
env.bak/
venv.bak/

# Spyder project settings
.spyderproject
.spyproject

# Rope project settings
.ropeproject

# mkdocs documentation
/site

# mypy
.mypy_cache/
.dmypy.json
dmypy.json

# Pyre type checker
.pyre/

# pytype static type analyzer
.pytype/

# Cython debug symbols
cython_debug/

# PyCharm
#  JetBrains specific template is maintained in a separate JetBrains.gitignore that can
#  be found at https://github.com/github/gitignore/blob/main/Global/JetBrains.gitignore
#  and can be added to the global gitignore or merged into this file.  For a more nuclear
#  option (not recommended) you can uncomment the following to ignore the entire idea folder.
#.idea/''',
    'README.md': 'A new Flask Project.',
}

# Function to create the directory structure recursively
def create_structure(base_path, structure):
    for name, content in structure.items():
        path = os.path.join(base_path, name)
        
        # If content is a dictionary, create a directory and call function recursively
        if isinstance(content, dict):
            os.makedirs(path, exist_ok=True)
            print(f"Created directory: {path}")
            create_structure(path, content)
        
        # If content is a string (file content), create the file
        else:
            with open(path, 'w') as f:
                f.write(content)
            print(f"Created file: {path}")


# Function to initialize the Flask app structure
def create_flask_app(app_name):
    try:
        # Create project directory
        os.makedirs(app_name, exist_ok=True)
        print(f"Created project folder: {app_name}")

        # Create virtual environment
        venv_path = os.path.join(app_name, 'venv')
        subprocess.run([sys.executable, '-m', 'venv', venv_path])
        print(f"Created virtual environment at: {venv_path}")

        if platform.system() == "Windows":
            activate_script = os.path.join(venv_path, 'Scripts', 'activate')
            command = f'{activate_script} && echo "Virtual environment activated."'
            subprocess.run(command, shell=True)
        else:
            activate_script = os.path.join(venv_path, 'bin', 'activate')
            command = f'source {activate_script}'
            subprocess.run(command, shell=True, executable="/bin/bash")
        
        print(f"Activated virtual environment at: {venv_path}")

        # Determine the pip executable path based on the OS
        if platform.system() == "Windows":
            pip_executable = os.path.join(venv_path, 'Scripts', 'pip.exe')
        else:
            pip_executable = os.path.join(venv_path, 'bin', 'pip')

        # Install Flask
        subprocess.run([pip_executable, 'install', 'flask'], cwd=app_name)

        # Create requirements.txt using pip freeze 
        with open(os.path.join(app_name, 'requirements.txt'), 'w') as req_file:
            subprocess.run([pip_executable, 'freeze'], stdout=req_file)
        
        # Create the structure inside the app directory
        create_structure(app_name, flask_structure)

        print(f"Flask app '{app_name}' created successfully!")

        print(f"\nTo activate the virtual environment, run the following command:")
        print(f"    cd {app_name}")
        if platform.system() == "Windows":
            print(f"    venv\\Scripts\\activate")
        else:
            print(f"    source venv/bin/activate")

    except FileExistsError:
        print(f"Error: Folder '{app_name}' already exists.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Main function
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: create-flask-app <app-name>")
    else:
        app_name = sys.argv[1]
        create_flask_app(app_name)