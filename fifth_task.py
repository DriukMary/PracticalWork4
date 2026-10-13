# This script prints the letter 'M' using a character entered by the user.

char = input("Please enter a character: ")

#  Create a template of the letter 'M' using a placeholder (e.g., '#')
template = """
#     #
##   ##
# # # #
#  #  #
#     #
"""

# Replace the placeholder '#' with the user's character
result = template.replace("#", char)

print(result)
