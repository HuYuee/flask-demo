from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__,)
CORS(app, resources=r'/*')
print(__name__)


@app.route('/')
def hello()->str:
    return 'Hello world from Flask!'


@app.route('/list')
def hello1()->str:
    return 'list'


@app.route('/todo/api/v1.0/tasks', methods=['GET'])
def get_tasks():
    result_text = {"statusCode": 200,"message": "文件上传成功"}
    response = (jsonify(result_text))
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'OPTIONS,HEAD,GET,POST'
    response.headers['Access-Control-Allow-Headers'] = 'x-requested-with'
    return response


app.run()
