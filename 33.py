def reverse_string(s):
    if len(s) <= 1:
        return s
    return reverse_string(s[1:]) + s[0]
input_str = "Yrysbek!"
result = reverse_string(input_str)
print(result)
