# Converts a number to its positive value
def make_positive(number):
    if number < 0:
        result = number * -1  # Make negative numbers positive
    else:
        result = number  # Keep positive numbers as-is
    return result

print(make_positive(-4))   # 4
print(make_positive(0))    # 0
print(make_positive(-.25)) # 0.25
print(make_positive(5))    # 5