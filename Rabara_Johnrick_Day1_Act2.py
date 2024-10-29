# Taking input for each variable
name = input("Name: ")
math_grade = float(input("Math Grade: "))
science_grade = float(input("Science Grade: "))
english_grade = int(input("English Grade: "))
status = input("Status: ")

# Calculating the average grade
average = (math_grade + science_grade + english_grade) / 3

# Displaying the results
print("\nResults:")
print("Name:", name)
print("Math Grade:", math_grade)
print("Science Grade:", science_grade)
print("English Grade:", english_grade)
print("Average:", round(average, 2))
print("Status:", status)
