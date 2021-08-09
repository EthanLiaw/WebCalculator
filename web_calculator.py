from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def landing_page(name=None):
    return render_template('calculator_input.html')

@app.route("/calculate", methods=['POST'])
def calculate():
    input1 = request.form['input1']
    input2 = request.form['input2']
    operator = request.form['operator']
    print(operator + " " + input1 + " and " + input2)
    result = result_of_calculation(float(input1), float(input2), operator)
    return render_template('calculation_result.html', input1=input1, input2=input2, operator=operator, result=result)

def result_of_calculation(input1, input2, operator):
    if operator == "add":
        return addition(input1, input2)
    elif operator == "subtract":
        return addition(input1, -1 * input2)
    elif operator == "multiply":
        return multiplication(input1, input2)
    elif operator == "divide":
        return division(input1, input2)
    else:
        return "Uh oh, something went wrong."

def addition(x, y):
    return x + y

def multiplication(x, y):
    return x * y

def division(x, y):
    return x / y