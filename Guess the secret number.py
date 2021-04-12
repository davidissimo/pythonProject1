secret = 22
guess = int(input("What is the secret number: "))

if guess == secret:
    print("Well done")

else:
    print("Idoit, the number is not " + str(guess) + ".")

