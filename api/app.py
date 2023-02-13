from flask import Flask,request,jsonify
from flask_pymongo import PyMongo
import os 
app = Flask(__name__)

app.config["MONGO_URI"] = os.environ.get('MONGO_URI')
mongodb_client = PyMongo(app)
db = mongodb_client.db


@app.route('/',methods = ['GET'])
def get_data():
    return jsonify({'message':'hello world'})

@app.route('/',methods = ['POST'])
def post_data():
    return jsonify({'message':'post hello world'})

@app.route('/',methods = ['PUT'])
def put_data():
    return jsonify({'message':'put hello world'})







if __name__=='__main__':
    app.run(host='127.0.0.1',port=8080,debug=True)