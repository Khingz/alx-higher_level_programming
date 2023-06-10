#!/usr/bin/python

def multiple_returns(sentence):
    length = len(sentence)
    first_lett = sentence[0] if length > 0 else None
    return (length, first_lett)


if __name__ == "__main__":
    multiple_returns()
