weight = float(input("Weight (kg): "))
height = float(input("Height (m): "))

bmi = weight / (height ** 2) if height > 0 else 0
if bmi < 18.5:
    category = "Underweight"
elif bmi < 25:
    category = "Normal"
else:
    category = "Overweight"

print(f"Weight: {int(weight) if weight.is_integer() else weight} kg")
print(f"Height: {height} m")
print(f"BMI: {round(bmi,1)}")
print(f"Category: {category}")