# This script finds the minimum number of characters that need to be
# added to the right side of a word to make it a palindrome.

word = input("Please enter the word: ").lower()

#  Find the shortest part to cut from the left to leave a palindrome
for i in range(len(word)):
    # word[i:] cuts the first 'i' characters from the left
    remaining_part = word[i:]

    # Check if the remaining part reads the same backwards
    if remaining_part == remaining_part[::-1]:
        # 'i' is exactly the number of characters we cut and need to add to the right
        print(i)
        break
