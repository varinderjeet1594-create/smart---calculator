print("calculator is starting....")
print("Type quit anytime to stop")
print("Type history to see alculations")

history = []

while True:
    number1 = input("Enter first number: ")

    if number1 == "quit":
        print("Goodbye!")
        break
    if number1 == "history":
        for item in history:
            print(item)
        continue    

    operation = input("Enter operation(+-*/): " )   
    number2 = input("Enter second number: ")
    
    try:
        number1 = float(number1)
        number2 = float(number2)

        if operation == "+":
            result = number1 + number2
        elif operation == "-":
            result = number1 - number2
        elif operation == "*":
            result = number1 * number2
        elif operation == "/":
            result = number1 / number2
        else:
            print("invalid operation! use +-*/") 
            continue

        calculation = f"{number1} {operation} {number2} = {result}"
        history.append(calculation)

        with open("history.txt", "a") as file:
            file.write(calculation + "\n")
        if len(history) > 10:
            history.pop(0)    
    
        print("Answer:" , result)
        print("========")
    except:
        print("Invalid input! Please enters numbers only.")
        print("------")