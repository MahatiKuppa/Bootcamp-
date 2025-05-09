friends = ["Alice", "Bob", "Charlie", "David", "Emaneul"]
import random
list_index = random.randint(0,4)
payer = friends[list_index]
print(f"{payer} has to pay the bill!")

# or
# person = random.choice(friends)