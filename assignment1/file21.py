def count_occurrences(lst, element):
    count = 0
    for item in lst:
        if item == element:
            count += 1
    
    return count
lst = [1, 2, 3, 4, 2, 2, 5, 2]
element = 2
result = count_occurrences(lst, element)
print(f"The element {element} occurs {result} times in the list.")
