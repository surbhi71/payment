
from flask import Flask, request, jsonify
from pymongo import MongoClient
import uuid

app = Flask(__name__)

# MongoDB connection setup
client = MongoClient('mongodb://root:password@ecp-cd-mongo-headless.lcm-mongo.svc.cluster.local:27017/?replicaSet=rs0')
db = client['test']
collection = db['payment']


@app.route('/makepayment', methods=['POST'])
def add_product():
    # Get data from request
    data = request.json
    data["order_id"] = str(uuid.uuid4())

    inserted_payment = collection.insert_one(data)
    # Return the inserted document ID
    return jsonify({'status': 'success', 'message': 'Order placed sucessfully', 'order_id': data["order_id"]}), 201


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
    #app.run(debug=True)

