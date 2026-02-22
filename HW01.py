print("Hello, World!")
print("This is my first Python program.")
print("I am learning how to write code in Python.")
while True:
    user_input = input("Enter a message (type 'exit' to quit): ")
    if user_input.lower() == 'exit':
        print("Goodbye!")
        break
    else:
        print(f"You entered: {user_input}")
