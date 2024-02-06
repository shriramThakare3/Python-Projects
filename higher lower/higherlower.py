from gamedata import game_data  # Assuming this imports the game_data properly
from art import higher, vs 
import random 

print(higher)

def format_data(account):
    """Function to format account data for display"""
    account_name = account["name"]  # Corrected variable name
    account_desc = account["description"]  # Corrected variable name
    account_country = account["country"]  # Corrected variable name
    return f"{account_name}, a {account_desc}, from {account_country}"  # Changed print to return

def check_answer(guess, a_followers, b_followers):
    """Function to check if the guess is correct"""
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"

score = 0 

account_a = random.choice(game_data)
account_b = random.choice(game_data)
while account_a == account_b:  # Ensure two different accounts are chosen
    account_b = random.choice(game_data)

print(f"Compare A: {format_data(account_a)}")
print(vs)
print(f"Against B: {format_data(account_b)}")

guess = input("Who has more followers? Type 'A' or 'B': ").lower()

a_follower_count = account_a["follower_count"]
b_follower_count = account_b["follower_count"]

is_correct = check_answer(guess, a_follower_count, b_follower_count)  # Corrected variable name

if is_correct:
    score += 1
    print(f"You're right! Current score: {score}")
else:
    print(f"Your answer is incorrect. Final score: {score}")
