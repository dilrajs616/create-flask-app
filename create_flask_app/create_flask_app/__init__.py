# create_flask_app/__init__.py
from flask import Flask
from .cli import create_app_command

def init_app(app: Flask):
    app.cli.add_command(create_app_command)
