import bson.objectid
import json
import datetime
import pymongo


class TodoDao:

    def json_handler(self, x):
        if isinstance(x, bson.objectid.ObjectId):
            return str(x)
        elif isinstance(x, datetime.datetime):
            return x.isoformat()
        else:
            TypeError(x)

    def get_all_todos_dao(self):
        client = pymongo.MongoClient('mongodb', 27017)
        db = client.todos
        results = []
        todos = db.delete_me.find()
        print(todos)
        for todo in todos:
            results.append(json.dumps(todo, default=self.json_handler))
        return results
