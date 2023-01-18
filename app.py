import logging

from flask import Flask, request, render_template, send_from_directory
# from main.py import
from main.main import show_photo
from loader.loader import photo_download

POST_PATH = "posts.json"
UPLOAD_FOLDER = "uploads/images"

app = Flask(__name__)

app.register_blueprint(show_photo)
app.register_blueprint(photo_download)

logging.basicConfig(filename='basic.log', level=logging.INFO)

@app.route("/uploads/<path:path>")
def static_dir(path):
    return send_from_directory("uploads", path)


app.run()

