# Formats an address string into house number and street name
def format_address(address_string):
    address_parts = address_string.split()  # Split the address
    house_number = address_parts[0]  # First part is the house number
    street_name = " ".join(address_parts[1:])  # Rest is the street name
    return f"House number {house_number} on a street named {street_name}"

print(format_address("123 Main Street"))
# House number 123 on a street named Main Street
print(format_address("1001 1st Ave"))
# House number 1001 on a street named 1st Ave
print(format_address("55 North Center Drive"))
# House number 55 on a street named North Center Drive