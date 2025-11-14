# Lists all numbers from minimum to maximum (inclusive)
def all_numbers(minimum, maximum):
    return_string = ""  # Start with an empty string
    for num in range(minimum, maximum + 1):  # Loop from min to max (inclusive)
        return_string += str(num) + " "  # Add each number and a space
    return return_string.strip()  # Remove the trailing space

print(all_numbers(2, 6))   # 2 3 4 5 6
print(all_numbers(3, 10))  # 3 4 5 6 7 8 9 10
print(all_numbers(-1, 1))  # -1 0 1
print(all_numbers(0, 5))   # 0 1 2 3 4 5
print(all_numbers(0, 0))   # 0