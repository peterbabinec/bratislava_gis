from flask import Flask, jsonify, render_template

app = Flask(__name__, static_folder="./static/dist",
            template_folder="./static")


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/hello")
def hello():
    return get_hello()


def get_hello():
    message = "Hello World!"
    return message


if __name__ == "__main__":
    app.run()
