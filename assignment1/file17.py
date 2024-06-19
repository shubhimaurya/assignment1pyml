input_string = input("Enter a string: ")
words = input_string.split()
title_case_words = []
for word in words:
    capitalized_word = word.capitalize()
    title_case_words.append(capitalized_word)

title_case_string = ' '.join(title_case_words)
print("String in title case:", title_case_string)
