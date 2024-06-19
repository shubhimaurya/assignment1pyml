input_string = input("Enter a string: ")
char_frequency = {char: input_string.count(char) for char in input_string}

print("Character frequencies:")
for char, freq in char_frequency.items():
    print(f"{char}: {freq}")
