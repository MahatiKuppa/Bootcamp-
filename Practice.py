def greet():
    print("Good Morning Mahati")
    print("Hope you have a good day!")
    print("Enjoy your learning!")
greet()

#defining greet fucntion with input:
def greet_input(name):
    print(f"Good morning {name}")
    print("Hope you have a good day!")
    print("Enjoy your learning!")
name = "MK"
greet_input(name)

#Functions with more than one parameter:
def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is the weather like in {location}?")
greet_with("Obsidian", "India")

#Using keyword arguments:
greet_with(location = "Bengaluru", name = "Mahati K")


