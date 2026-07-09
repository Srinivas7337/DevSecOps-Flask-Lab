from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to DevSecOps Lab"

@app.route("/login")
def login():
    return "Login Page"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
