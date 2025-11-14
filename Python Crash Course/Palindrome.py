# Checks if a string is a palindrome (ignores spaces and case)
def is_palindrome(input_string):
    new_string = ""       # Builds the cleaned string
    reverse_string = ""   # Builds the reversed string
    for letter in input_string:
        if letter != " ":
            new_string = new_string + letter.lower()      # Add to forward string
            reverse_string = letter.lower() + reverse_string  # Add to reversed string
    return new_string == reverse_string  # Compare both strings

print(is_palindrome("Never Odd or Even"))  # True
print(is_palindrome("abc"))                # False
print(is_palindrome("kayak"))             # True