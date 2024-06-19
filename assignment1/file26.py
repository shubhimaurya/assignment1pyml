def check_prefix_suffix(string, prefix, suffix):
    starts_with_prefix = string.startswith(prefix)
    ends_with_suffix = string.endswith(suffix)
    
    return starts_with_prefix, ends_with_suffix
string = "Hello, world!"
prefix = "Hello"
suffix = "world!"

starts_with, ends_with = check_prefix_suffix(string, prefix, suffix)

print(f"The string starts with '{prefix}': {starts_with}")
print(f"The string ends with '{suffix}': {ends_with}")

