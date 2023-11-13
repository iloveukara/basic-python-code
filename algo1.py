print("Enter two numbers and the code will compare")

number_one = input("Enter first number")
number_two = input("Enter second number")

if number_one < number_two:
    print(number_one + " is LESS THAN " + number_two)
elif number_one > number_two:
    print(number_one + " is GREATER THAN " + number_two)
else:
    print(number_one + " is EQUAL TO " + number_two)