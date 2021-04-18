username = "Simona"
ponovi="DA"

print("Živjo " + username + ", namen tega programa je, da pretvorim kilometre v milje.")

while ponovi == "DA":

    vneseno=int(input("Vnesi št. kilometrov, ki jih rada pretvorila: "))

    print ("Rezultat je: " + str(vneseno * 0.621371192))

    ponovi=input("Želiš še pretvarjati, odgovori DA ali NE?")

else:
    print("Hvala za sodelovanje")

