import numpy as np
import matplotlib.pyplot as plt

def is_operator(token):
    operators = {"+", "-", "*", "/", "^", "sin", "cos"}
    return token in operators

def infix_to_postfix(infix):
    stack = []
    output = ""

    for token in infix:
        if token.isalnum() or token.isdigit():
            output += token + " "
        elif is_operator(token):
            while stack and is_operator(stack[-1]) and (token != "^" or stack[-1] != "^"):
                output += stack.pop() + " "
            stack.append(token)
        elif token == "(":
            stack.append(token)
        elif token == ")":
            while stack and stack[-1] != "(":
                output += stack.pop() + " "
            stack.pop()  # remove (

    while stack:
        output += stack.pop() + " "

    return output.strip()

def calculate(postfix, x_value):
    stack = []
    tokens = postfix.split()

    for to_calculate in tokens:
        if to_calculate.isnumeric():
            stack.append(int(to_calculate))
        elif to_calculate == "x":
            stack.append(x_value)
        else:
            if to_calculate in ["+", "-", "*", "/", "^", "sin", "cos"]:
                val1 = stack.pop()
                if to_calculate != "sin" and to_calculate != "cos":
                    val2 = stack.pop()

                if to_calculate == "+":
                    stack.append(val2 + val1)
                elif to_calculate == "-":
                    stack.append(val2 - val1)
                elif to_calculate == "*":
                    stack.append(val2 * val1)
                elif to_calculate == "/":
                    stack.append(val2 / val1)
                elif to_calculate == "^":
                    stack.append(val2 ** val1)
                elif to_calculate == "sin":
                    stack.append(np.sin(np.radians(val1)))
                elif to_calculate == "cos":
                    stack.append(np.cos(np.radians(val1)))

    return stack.pop()

def plot_expression(expression):
    x_vals = np.linspace(-10, 10, 100)
    y_vals = [calculate(expression, x) for x in x_vals]

    plt.plot(x_vals, y_vals)
    plt.title("Graph of the Expression")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    input_expression = input("Enter an infix expression: ")
    postfix_expression = infix_to_postfix(input_expression)
    print("Postfix expression:", postfix_expression)

    if 'x' in input_expression:
        plot_expression(postfix_expression)
