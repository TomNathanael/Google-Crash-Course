# Counts up or down between two numbers
def counter(start, stop):
    if start > stop:
        return_string = "Counting down: "
        while start >= stop:  # Count down
            return_string += str(start)
            if start > stop:
                return_string += ","
            start -= 1  # Decrease
    else:
        return_string = "Counting up: "
        while start <= stop:  # Count up
            return_string += str(start)
            if start < stop:
                return_string += ","
            start += 1  # Increase
    return return_string

print(counter(1, 10))  # Counting up: 1,2,3,4,5,6,7,8,9,10
print(counter(2, 1))   # Counting down: 2,1
print(counter(5, 5))   # Counting up: 5
