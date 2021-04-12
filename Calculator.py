number1 = int(input("Vnesi prvo številko: "))
number2 = int(input("Vnesi drugo številko: "))

operacija = input("Katero operacijo želiš + - * / ? ")

if operacija == "+":
    print(number1 + number2)
if operacija == "-":
    print(number1 - number2)
if operacija == "*":
    print(number1 * number2)
if operacija == "/":
    print(number1 / number2)

else:
    print("To ni matematična operacija")

