length = float(input("enter the length in centimeters: "))
if length < 0:
    print("Error: the length cannot be negative.")
else:
    inches = length / 2.54
    print("the length in inches is", inches)
