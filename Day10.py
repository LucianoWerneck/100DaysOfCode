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
num1 = int(input("What's the first number: "))
for type in operation:
    print(type)
operation_type = input("Pick an operation from the line above: ")
num2 = int(input("What's the second number: "))
calculation_function = operation[operation_type]
answer = calculation_function(num1, num2)
print(f"{num1} {operation_type} {num2} = {answer}")

new_operation = input("pick an operation: ")
num3 = int(input("What's the next number? "))
new_function = operation[new_operation]
new_calcualtion = new_function(answer, num3)
print(f"{answer} {new_operation} {num3} = {new_calcualtion}")
