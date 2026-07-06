# Module for String Operations
# Converts the entire string to uppercase letters
def capitalize_words(text):
    return str.upper(text)
# Reverses the order of characters in a string
def reverse_string(text):
    return text[::-1]
# Counts the total number of words in the string
def word_count(text):
    words=str.split(text," ")
    return len(words)
    
