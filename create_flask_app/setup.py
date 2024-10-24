from setuptools import setup, find_packages

setup(
    name="create-flask-app",  # Name of your package
    version="0.1.0",  # Initial version
    description="A custom Flask CLI command to create a new Flask app with a basic structure",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    author="Dilraj Singh",  # Replace with your name
    author_email="your_email@example.com",  # Replace with your email
    url="https://github.com/yourusername/flask-create-app",  # URL of your package, if applicable
    license="MIT",  # Choose your license
    packages=find_packages(),
    install_requires=[
        "Flask",  # Add other dependencies here if needed
    ],
    entry_points={
        'flask.commands': [
            'create-app=create_flask_app.cli:create_app_command',
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
