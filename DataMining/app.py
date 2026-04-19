from flask import Flask, render_template, request
import os
from model import rank_resumes
import logging
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)
app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = os.path.join(BASE_DIR, "uploads")

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload():
    jd = request.form["job_description"]
    files = request.files.getlist("resumes")

    paths = []
    for file in files:
        path = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
        file.save(path)
        paths.append(path)

    results = rank_resumes(paths, jd)

    return render_template("result.html", results=results)


if __name__ == "__main__":
   app.run(host="0.0.0.0", port=5000, debug=False)