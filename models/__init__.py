from application import app

from .videos import *
db.create_all(app=app)
