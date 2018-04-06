from flask import Flask, send_file
import urllib

app = Flask(__name__)  # Creats an app object from flask


@app.route("/")
def hello():
    # return "Howdy!"
    return send_file('images/howdy.jpg', mimetype='image/jpg')


if __name__ == "__main__":
    # app.run starts the server.
    app.run()
