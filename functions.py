# functions.py

def get_unique_list_f(lst):
    """
    Takes a list as an argument and returns a new list with unique elements from the first list.
    """
    return list(set(lst))

def count_case_f(string):
    """
    Returns the number of uppercase and lowercase letters in the given string.
    """
    uppercase_count = sum(1 for char in string if char.isupper())
    lowercase_count = sum(1 for char in string if char.islower())
    return (uppercase_count, lowercase_count)

def remove_punctuation_f(sentence):
    """
    Removes all punctuation marks (commas, periods, exclamation marks, question marks) from a sentence.
    """
    import string
    return sentence.translate(str.maketrans('', '', string.punctuation))

def word_count_f(sentence):
    """
    Counts the number of words in a given sentence. To do this properly, first it removes punctuation from the sentence.
    """
    cleaned_sentence = remove_punctuation_f(sentence)
    words = cleaned_sentence.split()
    return len(words)