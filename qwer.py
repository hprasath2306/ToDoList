from flask import Flask
from flask_restful import Resource, Api, reqparse, abort
from pymongo import MongoClient
from dotenv import load_dotenv
from bson import ObjectId
import os
load_dotenv() 
uri=os.getenv("uri")#Connection string with Mongodb
app = Flask(__name__)
api = Api(app)
apo = reqparse.RequestParser()
apo.add_argument("tasks", type=str, help="Task is must", required=True)
apo.add_argument("summary", type=str, help="Summary is must", required=True)
client = MongoClient(uri)
db = client['your_database_name']
collection = db['your_collection_name']

class ToDoList(Resource):
    def get(self, todoid):
        task = collection.find_one({'_id': ObjectId(todoid)})
        if task:
            return {'tasks': task['tasks'], 'summary': task['summary']}
        else:
            abort(404, message="Task not found")

    def post(self, todoid):
        a = apo.parse_args()
        task_id = collection.insert_one({'tasks': a['tasks'], 'summary': a['summary']}).inserted_id
        return {'id': str(task_id)}

    def delete(self, todoid):
        result = collection.delete_one({'_id': ObjectId(todoid)})
        if result.deleted_count > 0:
            return {'message': 'Task deleted successfully'}
        else:
            abort(404, message="Task not found")

class ToDo(Resource):
    def get(self):
        tasks = collection.find()
        result = []
        for task in tasks:
            result.append({'id': str(task['_id']), 'tasks': task['tasks'], 'summary': task['summary']})
        return result

api.add_resource(ToDoList, "/todo/<string:todoid>")
api.add_resource(ToDo, "/todo")

if __name__ == "__main__":
    app.run(debug=True)
