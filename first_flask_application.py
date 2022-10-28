from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello, World!, this is very nice way to write the code, and we wll definitely build something great." \
           "We are building the application which we can used in future."


if __name__ == "__main__":
    app.run(debug=True)
