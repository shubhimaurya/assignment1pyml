
filename = "output.txt"
try:
    with open(filename, "r") as file:
        content = file.read()
    print("Content of the file:")
    print(content)
except FileNotFoundError:
    print(f"The file {filename} does not exist.")
