
from flask import Flask, request, jsonify,render_template,make_response
import ping_checker

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
    p = ping_checker.ping_ip(request.get_data().decode("utf-8"))
    return make_response(p[1], 200 if p[0] else 300)
    # return jsonify({"uuid":uuid})


if __name__ == '__main__':
    app.run()
