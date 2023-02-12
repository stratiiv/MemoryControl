from flask import Flask,request,jsonify


app = Flask(__name__)

@app.route('/',methods = ['GET'])
def get_data():
    return jsonify({'message':'hello world'})











if __name__=='__main__':
    app.run(host='127.0.0.1',port=8080,debug=True)