from flask import Flask
from flask.globals import request
from flask.json import jsonify
from flask_restful import Api, Resource
import warnings
import json

# Automatically ignore warning messages
warnings.filterwarnings('ignore')

app = Flask(__name__)
api = Api(app)

f = open('Database.json')
userdatas = json.load(f)

class Home(Resource):
    def get(self):
        print('hello world')
        return jsonify({'msg':'Hello World'})

class Login(Resource):
    def post(self):
        data = request.get_json(force = True)
        print(data)
        # todo: login verification
        find = [user for user in userdatas if user["ID"] == data[0]["ID"]]       
        if len(find) == 0:
            return jsonify({'msg':'User not found'})
        else:
            user = find[0]
            if data[0]['password'] == user['password']:
                return jsonify({'msg':'User {} login successfuly!'.format(user['ID'])})
            else:
                return jsonify({'msg':'Wrong password!'})




api.add_resource(Home, '/')
api.add_resource(Login, "/Login")


# Closing file
f.close()

if __name__ == '__main__':
    app.run(host="localhost", port=8088, threaded=True, debug=True)
