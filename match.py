sign=input("given an operator:")
num1=int(input())
num2=int(input())
match sign:
    case '-':
        print("substuction is",num1-num2)
    case '*':
        print("Multiplication is",num1*num2)
    case '+':
        print("addition is",num1+num2)
    case '/':
        print("diviton is",num1/num2)
    case _:
        print("wrong sign")