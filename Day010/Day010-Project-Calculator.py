logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""
def add(n1,n2):
    """takes 2 number and return sum as output"""
    return n1+n2

def subtract(n1,n2):
    """takes 2 number and return by substract 2nd from 1st as output"""
    return n1-n2

def multiply(n1,n2):
    """takes 2 number and return multiply as output"""
    return n1*n2

def divide(n1,n2):
    """takes 2 number and return by dividing 1st from 2nd as output"""
    return n1/n2

def power(n1,n2):
    return n1**n2

def mod(n1,n2):
    return n1%n2

operations={'+':add,'-':subtract,'*':multiply,'/':divide,'^':power,'%':mod}

def calculator():
    print(logo)
    num1=float(input("Enter 1st number: "))
    go_on=True
    while go_on:
        for symbol in operations:
            print(symbol)
        operation_symbol=input("Pick an operation from above. ")
        num2=float(input("Enter next number: "))
        calculation_funtion=operations[operation_symbol]
        answer=calculation_funtion(num1,num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        run=input(f"Enter 'y' to continue calculating with {answer}, or type 's' to start new calculation , or 'e' exit calculator.: ")
        if run=='y':
            num1=answer
        elif run=='s':
            go_on=False
            calculator()
        else:
            go_on=False
            

calculator()
