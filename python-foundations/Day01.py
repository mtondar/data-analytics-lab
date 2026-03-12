# Day01 - Python Basics for Water Data Analysis Bootcamp

# Print examples

print("Hello Water Data")
print("I am learning Python for Water Data Analysis")

# Variables

river_name = "Karun"
rainfall = 12
water_level = 3.5
is_flood = False

print(river_name)
print(rainfall)
print(water_level)
print(is_flood)

# Data Types

print(type(river_name))
print(type(rainfall))
print(type(water_level))
print(type(is_flood))

# Rainfall calculation

rain_day1 = 12
rain_day2 = 8
rain_day3 = 15

total_rain = rain_day1 + rain_day2 + rain_day3
print("Total Rainfall:", total_rain)

# River flow average

flow_day1 = 80
flow_day2 = 95

average_flow = (flow_day1 + flow_day2) / 2
print("Average Flow:", average_flow)

# User input example

rainfall = float(input("Enter rainfall (mm): "))
river_flow = float(input("Enter river discharge (m3/s): "))

print("Rainfall:", rainfall)
print("River Flow:", river_flow)
