weight = float(input("Weight : "))
unit = input("(L)bs or (K)g : ").lower()

while True:
    if unit == "k":
        calculated_weight = round(weight / 0.45, 2)
        print(f"You are {calculated_weight} pounds")
        break
    elif unit == "l":
        calculated_weight = round(weight * 0.45, 2)
        print(f"You are {calculated_weight} KGs")
        break
    else:
        print("\nWrong selection!")
        unit = input("(L)bs or (K)g : ").lower()
