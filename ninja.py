with open("ninja.txt", "r") as ninja_file:
    ninja_lines = ninja_file.read().splitlines()

    for line in ninja_lines:
        print(line)

with open("ninja2.txt", "w") as ninja_file_2:
     ninja_file_2.write("Hello, new file!")

print("Sem zapisal v fajl: Hello, new file!")
