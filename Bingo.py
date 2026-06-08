# Import the random module to generate stochastic numbers
import random

# Generate a random integer between 0 and 10 (inclusive)
random_num = random.randint(0, 10)
guess_left = 3  # Set the maximum number of attempts allowed
name = None  # Initialize the name variable as None


def check_answer(answer):
    """
    Validates the user's guess against the target number.
    Returns a tuple: (Boolean status, String message)
    """
    if answer > random_num:
        return (False, "choose lower number")  # Logic for a guess that is too high
    elif answer < random_num:
        return (False, "choose higher number")  # Logic for a guess that is too low
    elif answer == random_num:
        return (True, "bingo!")  # Logic for a correct guess


# Prompt the user to enter their name for a personalized experience
name = input("please enter name: ")

# Main game loop to handle repetitive guessing logic
while True:

    # Termination condition: Check if the user has exhausted all guesses
    if guess_left == 0:
        print(f"you ran out of the guesses\nanswer was {random_num}")
        break  # Exit the loop if no guesses are left

    # Input handling: Convert the raw string input into an integer
    answer_input = int(input(f"please enter number {name}: "))

    # Store the result of the validation function in a variable
    answer_result = check_answer(answer_input)

    # Check the boolean part of the returned tuple (Index 0)
    if answer_result[0] == False:
        print(answer_result[1])  # Display the feedback (higher/lower)

    else:
        # If the guess is correct, print success message and exit
        print(answer_result[1])
        break

    # Decrement the remaining guesses counter by 1 after each attempt
    guess_left -= 1

# Final execution step after exiting the loop
print("end of game")
