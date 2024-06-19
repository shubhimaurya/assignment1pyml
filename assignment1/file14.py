
lines = []

print("Enter lines of text. Press Enter on an empty line to finish:")
while True:
    line = input()
    if line == "":
        break
    lines.append(line)
print("\nLines entered:")
for line in lines:
    print(line)
