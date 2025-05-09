print("Welcome to the roller coaster")
height = int(input("What is your height?"))

bill = 0
if height > 120:
    age = int(input("What is your age?"))
    if age<12:
        bill += 5
    elif age<=18:
        bill += 7
    elif 45<=age<=50:
        print("Your ride is on us!")
    else:
        bill += 12

    photo = input("Would you want photos? Y or N:")
    if photo == "Y":
        bill += 3

    print(f"Your total bill is: {bill}")
else:
    print("Sorry, you have to grow taller before you can ride the coaster.")



