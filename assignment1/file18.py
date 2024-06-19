def are_anagrams(str1, str2):
    def clean_string(s):
        return ''.join(sorted(filter(str.isalpha, s.lower())))
    
    cleaned_str1 = clean_string(str1)
    cleaned_str2 = clean_string(str2)
    
    return cleaned_str1 == cleaned_str2

str1 = "Listen"
str2 = "Silent"

if are_anagrams(str1, str2):
    print(f'"{str1}" and "{str2}" are anagrams.')
else:
    print(f'"{str1}" and "{str2}" are not anagrams.')
