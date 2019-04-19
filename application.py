import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__,template_folder = os.getcwd() + "/web/templates",static_folder=os.getcwd() + "/web/static",root_path = os.getcwd())
app.config.from_pyfile(os.getcwd() + '/config.py')

db = SQLAlchemy()
db.init_app(app)

# 初始化，建表
import models

