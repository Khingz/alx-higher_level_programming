#!/usr/bin/python

def multiple_returns(sentence):
    length = len(sentence)
    first_lett = None if sentence == "" else sentence[0]
    return (length, first_lett)


if __name__ == "__main__":
    multiple_returns()
