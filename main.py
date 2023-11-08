"""The route accepts a POST request with JSON data in the format {"number": x}
where x is an integer. The route should return a JSON object {"result": y},
where y is the square of x. If the request is not a POST request,
the route should return a 405 status code.
If the request does not contain JSON data or the JSON data does not contain the key "number",
 or the value of "number" is not an integer, the route should return a 400 status code with the message "Bad Request"."""

from flask import Flask, jsonify, request, make_response
import requests
import json

app = Flask(__name__)

@app.route('/', methods= ['GET'])
def main():
    return 'hellow world'

@app.route('/suqare', methods=['GET','POST'])
def suquare():
    if request.method != "POST":
        return make_response(jsonify({'result': 'Bad Request'}), 405)
    body = request.get_json()
    if not isinstance(body, dict):
        return make(jsonify({'result': 'Bad Request'}), 405)
    number = body.get('number')
    if not number:
        return make_response(jsonify({'result': 'Please specify number key'}), 400)
    if not isinstance(number, int):
        return make_response(jsonify({'result': 'Bad Request'}), 400)
    y = number*number
    return jsonify({"success": y})

if __name__=='__main__':
    app.run()