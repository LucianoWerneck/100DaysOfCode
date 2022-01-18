from calculator_art import logo
#adition
def add(n1,n2):
    return n1+n2

#subtraction
def subtract(n1, n2):
    return n1-n2

#multiplycation
def multiply(n1, n2):
    return n1*n2

#division
def divide(n1, n2):
    return n1/n2

operation = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}
def calculator():
    print(logo)
    num1 = float(input("What's the first number: "))
    for type in operation:
        print(type)
    should_continue = True
    while should_continue:
        operation_type = input("Pick an operation from the line above: ")
        num2 = float(input("What's the second number: "))
        calculation_function = operation[operation_type]
        answer = calculation_function(num1, num2)
        print(f"{num1} {operation_type} {num2} = {answer:.2f}")
        question = input(f"Type 'y' to continue calculating with {answer:.2f}, or type 'n' to start a new calculation, or type 'e' to exit.:")
        if question == 'y':
            num1 = answer
        elif question == "n":
            calculator()
        elif question == "e":
            should_continue = False

calculator()