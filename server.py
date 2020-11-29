
from flask import Flask, request, jsonify,render_template
import asyncio
import time

from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def hi():
    # return "Hello"
    return render_template('index.html')

@app.route('/static/')
def hello():
    # return "Hello"
    return render_template('index.html')


@app.route('/api/add_message/<uuid>', methods=['GET', 'POST'])
def add_message(uuid):
    content = request.json
    for i in range(10):
        print(i)
        time.sleep(1)
    print (content['mytext'])
    return jsonify({"uuid":uuid})


if __name__ == '__main__':
    app.run()
