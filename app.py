# Simple Calculator
def calculator() :
    num1 = int(input("Enter the first number:"))
    num2 = int(input("Enter the second number"))
    num3 =int(input("Enter the third number"))
    operator = input("Enter the operator(+ , - , * , /)")
    

    # Addition
    if operator == "+" :
        result = num1 + num2 +num3
        print(f"{num1}+ {num2} + {num3} = {result}")

    # Subraction
    elif operator == "-":
        result = num1 - num2 - num3
        print(f"{num1} - {num2} -{num3}= {result}")

    # Multiply
    elif operator == "*":
        result = num1 * num2 * num3
        print(f"{num1} * {num2} *{num3}= {result}")

    # Divide
    elif operator == "/":
        if num2 & num3 == 0:
            print("Zero can not divide ")
        else:
            result = num1 / num2 
            print(f"{num1} / {num2} /{num3}= {result}")

if __name__ == "__main__":
    calculator()




