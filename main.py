import os
from flask import Flask,render_template, url_for
import pprint

app = Flask(__name__, static_folder='.', static_url_path='')

@app.route('/hello/<name>')
def hello(name):
  pprint.pprint(type(name) is str)
  return name

@app.route("/")
def index():
    return url_for("show_user_profile", username="ai_academy")

@app.route("/user/<username>")
def show_user_profile(username):
    return render_template('index.html', message="花子さん", username=username)

@app.route("/post/<int:post_id>")
def show_post(post_id):
    return "Post" + str(post_id)

if __name__ == "__main__":
    app.run(port=8000, debug=True)