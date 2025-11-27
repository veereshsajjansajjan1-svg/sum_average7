import sys

def is_palindrome(s):
    return s == s[::-1]

if len(sys.argv) == 2:
    script_name = sys.argv[0]
    input_string = sys.argv[1]
else:
    script_name = sys.argv[0]
    input_string = "malayalam"

if is_palindrome(input_string):
    print(f"{input_string} is a palindrome.")
else:
    print(f"{input_string} is not a palindrome.")
