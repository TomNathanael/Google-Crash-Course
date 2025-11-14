# Recommends clothing based on temperature
def clothing_type(temp):
    if temp > 65:
        clothing = "T-Shirt"  # Hot weather
    elif temp > 50:
        clothing = "Sweatshirt"  # Mild weather
    elif temp > 32:
        clothing = "Jacket"  # Cool weather
    else:
        clothing = "Heavy Coat"  # Cold weather
    return clothing

print(clothing_type(72))  # T-Shirt
print(clothing_type(55))  # Sweatshirt
print(clothing_type(65))  # Sweatshirt
print(clothing_type(50))  # Jacket
print(clothing_type(45))  # Jacket
print(clothing_type(32))  # Heavy Coat
print(clothing_type(0))   # Heavy Coat