from flask import Flask
import requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/')
def hello():
    return "Hello worldsss"


# @app.route('/api',methods = ['POST', 'GET'])
# def read_root():
#     image = './plane.jpg'
#     info = requests.post("http://0.0.0.0:8000/", files={"file": open(image, "rb")}) 
#     return info