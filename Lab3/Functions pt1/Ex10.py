def is_palindrome(word):
    cleaned_word = ''.join(char.lower() for char in word if char.isalnum())
    return cleaned_word == cleaned_word[::-1]

# Example usage:
word = "Madam, I'm Adam"
if is_palindrome(word):
    print(f"'{word}' is a palindrome.")
else:
    print(f"'{word}' is not a palindrome.")
#'Madam, I'm Adam' is a palindrome.