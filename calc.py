def calculator(num, op, num2):
    if op == "+":
        result = num + num2 
    elif op == "-":
        result = num - num2 
    elif op == "/":
        result = num / num2 
    elif op == "*":
        result = num * num2  
     
    return result

cont = True

print("Welcome to the calculator!")  
num = float(input("What is your first number? ")) 
op = input("What operation would you like to complete? [+, -, /, *] ")
num2 = float(input("What is your second number? ")) 
final = calculator(num, op, num2)
print(f"{num} {op} {num2} = {final}")


while cont == True:
    resume = input("Would you like to continue your calculation? [Y/N] ").lower()
    if resume == "y":  
        num = final
        op = input("What operation would you like to complete? [+, -, /, *] ")
        num2 = float(input("What is your second number? ")) 
        final = calculator(num, op, num2)
        print(f"{num} {op} {num2} = {final}")
    elif resume =="n":
        print("Ending...")
        cont = False
    else: 
        print("Invalid input. Try again. ")
