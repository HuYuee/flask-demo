#!/usr/bin/python3 
from flask import Flask, jsonify, request, escape
from flask_cors import CORS
from my_module import showMain

app = Flask(__name__,)
CORS(app, resources=r'/*')

showMain()


def log_request(req, res):
    with open('ajax.log', 'w') as read:
        print(req.form, req.remote_addr, req.user_agent, res, file=read, sep='|')


@app.route('/')
def hello()->str:
    return 'Hello world from Flask!'


@app.route('/list')
def hello1()->str:
    return 'list'


@app.route('/viewlog')
def viewlog()->str:
    # with open('ajax.log') as log:
    #     rest = []
    #     for item in log:
    #         rest.append([])
    #         for i in item.split('|'):
    #             rest[-1].append(escape(i))
    # rest = (jsonify(rest))
    # rest.headers['Access-Control-Allow-Origin'] = '*'
    # rest.headers['Access-Control-Allow-Methods'] = 'OPTIONS,HEAD,GET,POST'
    # rest.headers['Access-Control-Allow-Headers'] = 'x-requested-with'
    # return rest
    with open('ajax.log') as log:
        rest = []
        for item in log:
            rest.append([])
            for i in item.split('|'):
                rest[-1].append(escape(i))
    return str(rest)


@app.route('/todo/api/v1.0/tasks', methods=['GET'])
def get_tasks():
    result_text = {"statusCode": 200, "message": "文件上传成功"}
    response = (jsonify(result_text))
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'OPTIONS,HEAD,GET,POST'
    response.headers['Access-Control-Allow-Headers'] = 'x-requested-with'
    log_request(request, result_text)
    return response


if __name__ == '__main__':
    app.run(debug=True)
