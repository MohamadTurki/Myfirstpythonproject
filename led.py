import datetime
import os


print("Hello my name is led")
name = input("What is your name: ")

def main():
    print("Ok " + name + " type in one of the following (calc, personal-details, date, clear, quit)")

    while(True):
        cmd = input("Led: ")

        if (cmd == "calc"):
            calculator()
        elif (cmd == "personal-details"):
            personal_details()
        elif (cmd == "date"):
            get_date()
        elif (cmd == "quit"):
            print("Bye Bye")
            break
        elif (cmd == "clear"):
            os.system("clear")
        else:
            print("Invalid command")

def personal_details():
    age = int(input("How old are you: "))
    if age < 0:
        print("Ok " + name + " stop lying to me")
    elif age < 10:
        print("Thats so cute child thank you for using me")
    elif age < 20:
        print("Ok " + name + " you are still a teenager")
    elif age < 35:
        print("You must build your future, young man")
    elif age < 120:
        print("Watch yourself, old man")
    else:
        print("Ok " + name + " stop lying to me")

def calculator():
    op = input("Select an operator +, -, /, *, %: ")
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    if op == '+':
        print(num1, "+", num2, "=", (num1 + num2))
    elif op == '-': 
        print(num1, "-", num2, "=", (num1 - num2))
    elif op == '/': 
        print(num1, "/", num2, "=", (num1 / num2))
    elif op == '*': 
        print(num1, "*", num2, "=", (num1 * num2))
    elif op == '%': 
        print(num1, "%", num2, "=", (num1 % num2))
    else:
        print("Invalid operator")

def get_date():
    print(datetime.datetime.now().date())


main()