# Module for String Operations

def capitalize_words(text):
    return str.upper(text)

def reverse_string(text):
    return text[::-1]

def word_count(text):
    words=str.split(text," ")
    return len(words)
    
