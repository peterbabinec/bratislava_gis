from flask import Flask, jsonify, render_template

app = Flask(__name__, template_folder="./static")
app.config['TEMPLATES_AUTO_RELOAD'] = True


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/api/v1.0/hello", methods=['GET'])
def hello():
    return get_hello()


def get_hello():
    hello = {'hello': 'world'}
    return jsonify(hello)


if __name__ == "__main__":
    app.run()
