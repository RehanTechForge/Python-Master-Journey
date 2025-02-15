# Hand-on Exercise

# ?Print Statements Problems
# 1. Write a Python program that prints "Hello, World!"
# print("Hello, World!")

# ?2. Write a program to print your name.
# my_name = "Muhammad Rehan"
# print(my_name)

# ?3. Print "Python" and "Programming" on separate lines.
# print("Python")
# print("Programming")

# ?4. Print "5 + 3 = ?" and then the result.
# print("5 + 3 =", 5 + 3)

# ?5. Print a multi-line string with at least 3 lines.
# print("""Lorem ipsum dolor sit amet, consectetur adipiscing elit.
# Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
# Ut enim ad minim veniam, quis nostrud exercitation.""")

# !Input Handling Problems

# ?6. Ask the user for their name and print a greeting.
# user_name = input("Please enter your username: ")
# print("Hello", user_name, "!")

# ?7. Take two numbers as input and print their sum.
# num_one = int(input("Please enter your first number: "))
# num_two = int(input("Please enter your second number: "))
# sum_of_nums = num_one + num_two
# print("Sum of", num_one, "and", num_two, "is", sum_of_nums)

# ?8. Ask the user for a sentence and print it.
# sentence = input("Please enter a sentence: ")
# print(sentence)

# ?9. Take two numbers as input and print their difference.
# num_three = int(input("Enter first number: "))
# num_four = int(input("Enter second number: "))
# difference_of_nums = num_three - num_four
# print("Difference of", num_three, "and", num_four, "is", difference_of_nums)

# ?10. Take a number as input and print its square.
# number_to_square = int(input("Please enter a number: "))
# square_of_number = number_to_square ** 2
# print("Square of", number_to_square, "is", square_of_number)

# !Arithmetic Operations Problems

# ?11. Take two numbers and perform sum, difference, multiplication, and division.
# num_five = int(input("Enter your first number: "))
# num_six = int(input("Enter your second number: "))

# sum_of_nums = num_five + num_six
# difference_of_nums = num_five - num_six
# multiplication_of_nums = num_five * num_six
# division_of_nums = num_five / num_six

# print("Sum of", num_five, "and", num_six, "is", sum_of_nums)
# print("Difference of", num_five, "and", num_six, "is", difference_of_nums)
# print("Multiplication of", num_five, "and", num_six, "is", multiplication_of_nums)
# print("Division of", num_five, "and", num_six, "is", division_of_nums)

# ?12. Take a number as input and print its cube.
# number_to_cube = int(input("Enter a number: "))
# cube_of_number = number_to_cube ** 3
# print("Cube of", number_to_cube, "is", cube_of_number)

# ?13. Take three numbers as input and print their average.
# num_seven = int(input("Enter your first number: "))
# num_eight = int(input("Enter your second number: "))
# num_nine = int(input("Enter your third number: "))
# average_of_nums = (num_seven + num_eight + num_nine) / 3
# print("Average of the three numbers is", average_of_nums)

# ?14. Take a number as input and check if it is even or odd.
# num_ten = int(input("Enter a number: "))
# if num_ten % 2 == 0:
#     print(num_ten, "is even.")
# else:
#     print(num_ten, "is odd.")

# ?15. Take the radius of a circle as input and calculate its area using πr².
# PI = 3.142
# radius = float(input("Enter radius of the circle: "))
# area_of_circle = PI * (radius ** 2)
# print("Area of the circle is", area_of_circle)

# !Challenges

# ?Fahrenheit to Celsius Conversion
# Taking temperature input in Fahrenheit
fahrenheit_temp = input("Enter Temperature in Fahrenheit: ")

# Converting Fahrenheit to Celsius using the formula: (F - 32) * 5/9
convert_to_degrees = (int(fahrenheit_temp) - 32) * 5 / 9

# Printing the converted Celsius temperature
print("Temperature in Celsius is", convert_to_degrees)

# ?Simple Interest Calculation
# Taking input for initial amount, interest rate, and time
initial_amount = input("Initial amount: ")
interest_rate = input("Interest rate (in percentage): ")
time_in_years = input("Time in years: ")

# Calculating Simple Interest using the formula: (P * R * T) / 100
simple_interest = (float(initial_amount) * float(interest_rate) * float(time_in_years)) / 100

# Calculating total amount after interest is added
amount_after_time = float(initial_amount) + simple_interest 

# Printing the total amount after interest
print("Amount after", time_in_years, "years is", amount_after_time)

# ?BMI Calculator
# Taking user input for weight in kg and height in meters
weight_in_kg = input("Enter your weight in (KG): ")
height_in_meter = input("Enter your height in (M): ")

# Calculating BMI using the formula: weight (kg) / height (m)^2
bmi = float(weight_in_kg) / (float(height_in_meter) ** 2)

# Categorizing BMI based on standard BMI ranges
if bmi < 18.5:
    print("Underweight")
elif 18.5 <= bmi < 25:
    print("Normal weight")
elif 25 <= bmi < 30:
    print("Overweight")
else:
    print("Obese")
