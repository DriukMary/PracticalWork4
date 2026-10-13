# This script replaces all occurrences of a specific lowercase letter
# with its uppercase version, except for the first and the last ones.

phrase = input("Please input phrase: ")
letter = input("Please input letter: ")

#  Find the positions (indexes) of the first and the last occurrence
first_index = phrase.find(letter)
last_index = phrase.rfind(letter)

result = ""

for i in range(len(phrase)):
    current_char = phrase[i]

    # Check if it's the target letter AND not the first/last one
    if current_char == letter and i != first_index and i != last_index:
        result += current_char.upper()  # Convert to uppercase and add
    else:
        result += current_char  # Keep the character as it is and add

print(result)
