age = input("What's your age?: ")
# 18-21 wristband
# 21+ drink
# below too young
if age != "":
    age = int(age)
    if age >= 18 and age < 21:
        print("You can enter, but you need a wristband")
    elif age > 21:
        print("Normal entry")
    else:
        print("You cannot enter")
else:
    print("Please enter an age!")