# python-rest-service

A sample rest service written in python.

## Installantion of Flask

![Flash Installation](/images/FlaskInstallation.png)

### Test Flask with "HELLO WORLD !"

Create a helloworld.py and add below code.

```python
from flask import Flask
app = Flask(__name__)
@app.route("/")
def hello():
    return "Howdy!"
if __name__ == "__main__":
    app.run()
```

Run your python script as shown below

![Executing Script](/images/ScriptExecution.png)

Copy the ip address - http://127.0.0.1:5000/ and load it in a browser and you will see below response

![Response](/images/Response.png)
