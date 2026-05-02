# Weight Convertor Program

weight = float(input("Enter your weight: "))
unit = input("Kilograms or Pounds (k/p): ")

if unit == "k":
    weight = weight * 2.205
    unit = "Lbs."
    print(f"Your weight is: {round(weight, 2)} {unit}")
elif unit == "p":
    weight = weight / 2.205
    unit = "Kgs."
    print(f"Your weight is: {round(weight, 2)} {unit}")
else:
    print (f"{unit} was not valid.")
