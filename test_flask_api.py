from flask import Flask, request
from flask_restx import Api, Resource, fields
import time

import argparse

app = Flask(__name__)
api = Api(app, version='1.0', title='FE@ST DB READER',
          description='FE@ST DB READER SERVICE',
          )

@api.route('/test_fcn', methods=['get'])
@api.doc(params={
    'query': {'in': 'query', 'description': 'query', 'default': 'test'}
})
class test_fcn(Resource):
    def get(self):
        t = time.time()
        query = request.args.get('query')

        
        object = {'query': query, 'time': t} 
        print('result of the query is:',object)
        return object


if __name__ == '__main__':
    #parser = argparse.ArgumentParser()
    #parser.add_argument("-p", "--port", help="port")
    #parser.add_argument('-p', '--port', type=int, help='Port number', required=True)
    #args = parser.parse_args()


    #print('Starting feast db reader on port ', args.port)
    print('Starting feast db reader on port ', 3000)
    #print(args.port)
    #app.run(debug=false, host='0.0.0.0', port=args.port)
    app.run(debug=false, host='0.0.0.0', port=3000)