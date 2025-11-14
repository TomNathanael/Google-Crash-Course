# Checks if a number is a power of two
def is_power_of_two(number):
    if number == 0:  # 0 is not a power of two
        return False
    while number % 2 == 0 and number != 1:  # Divide by 2 until odd or 1
        number = number / 2
    return number == 1  # True if 1, False otherwise

# Test cases
print(is_power_of_two(0))  # False
print(is_power_of_two(1))  # True
print(is_power_of_two(8))  # True
print(is_power_of_two(9))  # False