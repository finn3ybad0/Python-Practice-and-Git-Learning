# Name : Finney Bado
# Date : 03/05/2024
# Description : This better version of the calculator in ex2 : it takes the operation in one input and displays the result

# function that identify operation that is requested et returns a string storing that information
def operation(equation: str) -> str:
    if "+" in equation:
        operand = equation.split("+")
        return int(operand[0]) + int(operand[1])
    elif "-" in equation:
        operand = equation.split("-")
        return int(operand[0]) - int(operand[1])
    elif "*" in equation:
        operand = equation.split("*")
        return int(operand[0]) * int(operand[1])
    else :
        operand = equation.split("/")
        return int(operand[0]) / int(operand[1])


# main function
def calculatorV_II():
    calculation=input("enter calculation: ")
    print(f" result: { operation(calculation)}")


calculatorV_II()