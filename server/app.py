from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:param>')
def print_string(param):
    print(param)
    return param

@app.route('/count/<int:param>')
def count(param):
    numbers = '\n'.join(str(i) for i in range(param))  # Start from 0 and go up to param - 1
    numbers += '\n'  # Add a trailing newline character
    return numbers

@app.route('/math/<int:num1>/<operation>/<int:num2>')
def math(num1, operation, num2):
    result = None
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        if num2 != 0:
            result = num1 / num2
        else:
            return 'Division by zero is not allowed'
    elif operation == '%':
        result = num1 % num2

    if result is not None:
        return str(result)  # Return only the result as a string
    else:
        return 'Invalid operation'

if __name__ == '__main__':
    app.run(debug=True)