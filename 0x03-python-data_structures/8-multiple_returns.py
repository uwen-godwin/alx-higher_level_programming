#!/usr/bin/python3
def multiple_returns(sentence):
    """Return a tuple with the length and first character of a string."""
    length = len(sentence)
    first_char = sentence[0] if length > 0 else None
    return length, first_char
