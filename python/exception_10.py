# exception = events detected during execution that 
#             interrupt the flow of a program
correct = False
while not correct :
    try:
        numerator = int(input("Enter a number to divide:"))
        denominator = int(input("Enter a number to divide by: "))
        result = numerator / denominator
    except ZeroDivisionError as e:
        print(e)
        print("You can't divide by zero")
    except ValueError as e:
        print(e)
        print("Enter only numbers plz")
    except Exception as e:
        print(e)
        print("something went wrong :(")
    else:
        print(result)
        correct = True
    finally:
        print("This will always excute")