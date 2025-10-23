weight = float(input("Weight (kg): "))
height = float(input("Height (m): "))

bmi = weight / (height ** 2) if height > 0 else 0
print(f"Weight: {weight} kg")
print(f"Height: {height} m")
print(f"BMI: {round(bmi,1)}")