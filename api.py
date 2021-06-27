import random
import time
from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)



class HelloWorld(Resource):
    def get(self):
            now = time.time()
            random.seed(now//43200)
            price = random.randint(1,10)
            return {'price': price}

api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(debug=True)
