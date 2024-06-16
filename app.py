from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Now, I can create my first CI/CD Pipeline using Jenkins and ArgoCD! Version 1.0'
