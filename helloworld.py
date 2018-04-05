from flask import Flask
app = Flask(__name__) # Creats an app object from flask

@app.route("/")
def hello():
    return "Howdy!"

if __name__ == "__main__":
    # app.run starts the server.
    app.run() 