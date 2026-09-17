import hashlib
import os
import pickle
import sqlite3
import subprocess

import requests
import yaml
from flask import Flask, request, redirect, render_template_string

app = Flask(__name__)

AWS_SECRET_ACCESS_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"
DB_PASSWORD = "SuperSecret123!"


@app.route("/user")
def get_user():
    username = request.args.get("username")
    conn = sqlite3.connect("app.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id, email FROM users WHERE username = '" + username + "'")
    return str(cursor.fetchall())


@app.route("/ping")
def ping():
    host = request.args.get("host")
    return subprocess.check_output("ping -c 1 " + host, shell=True)


@app.route("/file")
def read_file():
    name = request.args.get("name")
    with open(os.path.join("/var/data", name)) as f:
        return f.read()


@app.route("/greet")
def greet():
    name = request.args.get("name")
    return render_template_string("<h1>Hello " + name + "</h1>")


@app.route("/load", methods=["POST"])
def load_session():
    return str(pickle.loads(request.data))


@app.route("/config", methods=["POST"])
def load_config():
    return str(yaml.load(request.data, Loader=yaml.Loader))


@app.route("/fetch")
def fetch():
    url = request.args.get("url")
    return requests.get(url, verify=False).text


@app.route("/go")
def go():
    return redirect(request.args.get("next"))


@app.route("/calc")
def calc():
    return str(eval(request.args.get("expr")))


def hash_password(password):
    return hashlib.md5(password.encode()).hexdigest()


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
