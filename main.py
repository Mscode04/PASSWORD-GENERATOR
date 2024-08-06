import random
import string


# print(string.ascii_letters)
# print(string.ascii_lowercase)
# print(string.ascii_uppercase)
# print(string.digits)
# print(string.punctuation)

def password(length, lower, upper, digit, symbol):
    result = ""
    if lower:
        data1= string.ascii_lowercase
    if upper:
        data2= string.ascii_uppercase
    if digit:
        data3= string.digits
    if symbol:
        data4= string.punctuation
    if not result:
        print("Invalid Input")
    AllData=data1+data2+data3+data4
    for x in range(int(length)):
        data5 = random.choice(AllData)
        result+=data5
    print(result)


length = input("How many Length you Wanted: ")
lower = input("include the lowercase yes / no : ").lower() == "yes"
upper = input("include the uppercase yes / no : ").lower() == "yes"
digit = input("include the digits yes / no : ").lower() == "yes"
symbol = input("include the symboles yes / no : ").lower() == "yes"
password(length,lower,upper,digit,symbol)
