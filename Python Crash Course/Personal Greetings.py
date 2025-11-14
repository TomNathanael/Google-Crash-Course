# Greets a person by name
def greeting(name):
    if name == "Taylor":
        return "Welcome back Taylor!"  # Special greeting for Taylor
    else:
        return "Hello there, " + name  # Generic greeting for others

print(greeting("Taylor"))  # Test with "Taylor"
print(greeting("John"))    # Test with "John"