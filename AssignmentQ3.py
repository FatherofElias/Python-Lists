#Question 3


#Task 1

#Extract the temperatures for the second week (7 days) of the month (index 7 to index 14). Expected Outcome:


temperatures = [72, 75, 78, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106]

second_week_temperatures = temperatures[7:14] #using list slicing for the 7th through 14th index we get our solution
print(second_week_temperatures)


#Task 2

above_100_temperatures = temperatures[24:] #using list slicing is probaly the easiest way to our solution
print("Temperatures above 100:", above_100_temperatures)