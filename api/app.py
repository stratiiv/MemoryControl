from flask import Flask,request,jsonify
from pymongo import MongoClient
from bson import json_util
import json

app = Flask(__name__)

mongodb_client = MongoClient('mongodb://root:pass@localhost:27018/')
db = mongodb_client.test_db
coll = db.test_collection

@app.route('/api/v1/list',methods = ['GET'])
def get_data():
    try:
        if coll.find().count() > 0:
            return json.loads(json_util.dumps([obj for obj in coll.find()]))
        else:
            return jsonify([])
    
    except:
        return jsonify({'message':'Error while trying to fetch the resource'}), 500
 

@app.route('/api/v1/list',methods = ['POST'])
def post_data():
    try:
        try:
            body = request.get_json()
        except:
            return jsonify({'message':'Bad request body'}),400
            
        ins_result = coll.insert_one(body)
        return jsonify({'message':'Sucess!'})
    except:
        return jsonify({'message':'Error while trying to fetch the resource'}), 500
    
@app.route('/api/v1/list/<obj_id>',methods = ['PUT'])
def put_data(obj_id):
    print(obj_id)
    try:
        try:
            body = request.get_json()
        except:
            return jsonify({'message':'Bad request body'}), 400
        
        upd_result = coll.update_one({"id":int(obj_id)},body)
        if upd_result.modified_count > 0:
            return jsonify({'message':'Updated sucessfully'}), 200
        else:
            return jsonify({'message':'Not available to update'}), 404
    
    except Exception as e:
        print(e)
        return jsonify({'message':'Error while trying to fetch the resource'}), 500
 
if __name__=='__main__':
    app.run(host='127.0.0.1',port=8080,debug=True)