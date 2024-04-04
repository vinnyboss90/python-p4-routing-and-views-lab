#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>' ,200

@app.route('/print/<string:parameter>')
def print_string(parameter):
    print(parameter)
    return parameter

# @app.route('/count/<int:parameter>')
# def count(parameter):
#     numbers = ''
#     for num in range(1, parameter + 1):
#         numbers += str(num) + '\n'
#     return numbers 

@app.route('/count/<int:parameter>')
def count(parameter):
    numbers = ''
    for num in range(parameter):  # Start the range from 0
        numbers += str(num) + '\n'
    return numbers, 200

@app.route('/math/<int:num1>/<string:operation>/<int:num2>')
def math(num1, operation, num2):
    result = None
    if operation == '+':
        result = num1 + num2, 200
    elif operation == '-':
        result = num1 - num2, 200
    elif operation == '*':
        result = num1 * num2, 200
    elif operation == 'div':
        result = num1 / num2, 200
    elif operation == '%':
        result = num1 % num2, 200 
    if result is not None:
        return str(result)
    else:
        return None
