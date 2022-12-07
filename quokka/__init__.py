from flask import Flask



app = Flask(__name__)

import quokka.views.ui_views

from flask_sqlalchemy import SQLAlchemy
app.config["SQLALCHEMY_DATABASE_URI"] = r"sqlite:///c:\sqlite\test.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

db.create_all()

from quokka.models.Device import Device
from quokka.controller.utils import import_devices
for device in import_devices():
    print(device)
    device_obj = Device(**device)
    db.session.add(device_obj)

db.session.commit()