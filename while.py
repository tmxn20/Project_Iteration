# Explaining what the user has to do 
print("Welcome! This program will calculate the average of numbers you enter.")
print("Enter numbers one by one.")
print("If you want to stop, type -1.")
print("Note: The number 0 is not allowed as input.")

# Creating a list store to valid numbers
valid_numbers = []

# Creating a while loop to keep asking the user to input numbers until they type -1
while True:
    # Ask the user to enter a number
    user_input = input("Please enter a number: ")
    
    # Convert the input to an integer
    try:
        number = int(user_input)
    except ValueError:
        # If the user enters something that is not a number, show a message
        print("That's not a valid number. Please try again.")
        continue  # Go back to the beginning of the loop
    
    # If the user types -1, stop the loop
    if number == -1:
        print("You chose to stop. Let's calculate the average!")
        break  # Exit the loop

    # If the user types 0, skip it
    if number == 0:
        print("0 is not a valid input. Please enter a different number.")
        continue  # Skip this input and ask for the next number

    # Add the valid number to the list
    valid_numbers.append(number)

# After exiting the loop, calculate the average if there are valid numbers
if valid_numbers:  # Check if the list is not empty
    total = sum(valid_numbers)  # Add up all the valid numbers
    count = len(valid_numbers)  # Count how many numbers were entered
    average = total / count  # Calculate the average
    print(f"The average of the numbers you entered is: {average:.2f}")
else:
    # If no valid numbers were entered, show a message
    print("You didn't enter any valid numbers to calculate an average.")