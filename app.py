"""App web do demo de reconhecimento de dígitos."""

from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "App no ar! Em breve a interface de desenho."


if __name__ == "__main__":
    app.run(debug=True)