temp = int(input("Enter a temperature: "))
unit = input("Enter the unit of the temperature (C or F): ")
if unit == "C":
    print("The temperature in Fahrenheit is", 9/5 * temp + 32)
elif unit == "F":
    print("The temperature in Celsius is", 5/9 * (temp - 32))
else:
    print("Invalid unit.")
    