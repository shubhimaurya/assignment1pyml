n = int(input("Enter the number of terms in the Fibonacci sequence: "))
a, b = 0, 1
print("The first", n, "numbers in the Fibonacci sequence are:")
for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b
