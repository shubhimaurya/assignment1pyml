user_input = input("Enter a string: ")
filename = "output.txt"
with open(filename, "w") as file:
    file.write(user_input)

print(f"The string has been written to {filename}.")
