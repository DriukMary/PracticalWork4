# This script calculates the percentage of uppercase and lowercase letters
# in a text string entered by the user, ignoring spaces and punctuation.

# Request text input from the user
text = input("Please enter your text: ")

# Initialize counters for uppercase, lowercase, and total letters
upper_count = 0
lower_count = 0
total_letters = 0

# Iterate through each character in the provided text
for char in text:
    if char.isalpha():  # Check if the character is a letter (ignore spaces/symbols)
        total_letters += 1

        if char.isupper():  # Check if the letter is uppercase
            upper_count += 1
        elif char.islower():  # Check if the letter is lowercase
            lower_count += 1

# Calculate and display percentages if the text contains any letters
if total_letters > 0:
    upper_percent = (upper_count / total_letters) * 100
    lower_percent = (lower_count / total_letters) * 100

    print(f"Uppercase letters: {upper_percent:.2f}%")
    print(f"Lowercase letters: {lower_percent:.2f}%")
else:
    print("There are no letters in the text!")
