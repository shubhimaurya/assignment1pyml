def remove_punctuation(input_string):
    punctuation = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    
    cleaned_string = ""
    for char in input_string:
        if char not in punctuation:
            cleaned_string += char
            
    return cleaned_string

input_string = "Hello, world! This is a test-string with: punctuation."
cleaned_string = remove_punctuation(input_string)
print(cleaned_string)
