# my_program.py

def is_palindrome(word):
    # is_palindrome from Task 12
    cleaned_word = ''.join(char.lower() for char in word if char.isalnum())
    return cleaned_word == cleaned_word[::-1]

def histogram(numbers):
    # histogram from Task 11
    for num in numbers:
        print('*' * num)

# Main
if __name__ == "__main__":
    word = "Madam, I'm Adam"
    if is_palindrome(word):
        print(f"'{word}' is a palindrome.")
    else:
        print(f"'{word}' is not a palindrome.")
    
    histogram([4, 9, 7])

#'Madam, I'm Adam' is a palindrome.
#****     
#*********
#*******  
