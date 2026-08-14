<<<<<<< HEAD
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from Flask"

if __name__ == "__main__":
=======
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from Flask"

if __name__ == "__main__":
>>>>>>> 0a8ad19be8db1d2bceee513c32e6c66a5e76f76f
    app.run(host="0.0.0.0", port=5000)