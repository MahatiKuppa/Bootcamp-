print("Welcome to Python Pizza Deliveries")
size = input("What size would you like your pizza? S, M, or L:")
pepperoni = input('''Would you like pepperoni on your pizza? Y or N:''')
extra_cheese = input('''Would you like extra cheese? Y or N:''')

bill = 0
if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25

if pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

if extra_cheese == "Y":
    bill += 1

print(f"Final bill is ${bill}.")