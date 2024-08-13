# 1. Declare and assign the variables here:
shuttle_name = 'Determination'
shuttle_speed_mph = 175000
Distance_to_Mars_km = 225000000
Distance_to_Moon_km = 384400
miles_per_kilometer_mkm = 0.621

# 2. Use print() to print the 'type' each variable. Print one item per line.
print(type(shuttle_name))
print(type(shuttle_speed_mph))
print(type(Distance_to_Mars_km))
print(type(Distance_to_Moon_km))
print(type(miles_per_kilometer_mkm))

# Code your solution to exercises 3 and 4 here:
miles_to_mars = Distance_to_Mars_km * miles_per_kilometer_mkm
hours_to_mars = miles_to_mars / shuttle_speed_mph
days_to_mars = hours_to_mars / 24

# Code your solution to exercise 5 here
