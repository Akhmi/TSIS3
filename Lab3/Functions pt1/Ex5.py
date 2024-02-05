def reverse_sentence(sentence):
    words = sentence.split() 
    reversed_sentence = ' '.join(words[::-1])  
    return reversed_sentence

# Example usage:
user_input = input("Enter a sentence: ")
reversed_result = reverse_sentence(user_input)
print("Reversed sentence:", reversed_result)