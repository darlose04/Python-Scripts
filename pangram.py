import string


def is_pangram(sentence):
    alpha = set(string.ascii_lowercase)
    return alpha <= set(sentence.lower())

print(is_pangram(""))