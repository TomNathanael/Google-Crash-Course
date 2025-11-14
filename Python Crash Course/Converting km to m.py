# Converts kilometers to meters
def convert_distance(km):
    m = km * 1000  # 1 km = 1000 m
    return m

my_trip_kilometers = 55
my_trip_meters = convert_distance(my_trip_kilometers)  # Convert to meters
print("The distance in meters is " + str(my_trip_meters))  # Print result