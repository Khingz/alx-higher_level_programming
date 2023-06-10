#!/usr/bin/python3

def multiple_returns(sentence):
    length = len(sentence)
    return (length, None) if sentence == "" else (length, sentence[0])


if __name__ == "__main__":
    multiple_returns()
