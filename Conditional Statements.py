# Taking user input
age = int(input("Enter your age: "))

# Conditional statements
if age < 13:
    print("You are a child.")
elif 13 <= age < 18:
    print("You are a teenager.")
elif 18 <= age < 65:
    print("You are an adult.")
else:
    print("You are a senior citizen.")
