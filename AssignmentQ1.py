#question 1 

#Task 1 
#Sort the grades in descending order print sorted list
#i used the .sort(reverse=true) process to execute the solution


grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]

grades.sort(reverse=True)
print(grades)


# Task 2  Calculate the average grade and print it.

average_grade = sum(grades) / len(grades) #calculates the total sum of all grades then divides it by the number of grades in the list

print("The average grade is:", average_grade)