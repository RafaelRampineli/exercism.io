from string import ascii_lowercase #alphabet words lowercase

def is_pangram(sentence):
    return check_pangram(sentence)

def check_pangram(sentence):
    #set is used to get unique values from string
    if len(set(ascii_lowercase) - set(sentence.lower())) == 0:
        return True
    else:
        return False
