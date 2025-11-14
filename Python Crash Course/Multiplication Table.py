# Prints multiplication table up to 5, stops if result > 25
def multiplication_table(number):
    multiplier = 1  # Start with 1
    while multiplier <= 5:
        result = number * multiplier
        if result > 25:  # Stop if result exceeds 25
            break
        print(f"{number}x{multiplier}={result}")  # Print the result
        multiplier += 1  # Move to next multiplier

multiplication_table(3)  # 3x1 to 3x5
multiplication_table(5)  # 5x1 to 5x5
multiplication_table(8)  # 8x1 to 8x3 (stops at 24)