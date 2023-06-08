#!/usr/bin/python3
from sys import argv, exit


def main():
    if len(argv) == 1:
        print("0")
        exit()
    sum = 0
    for i in range(1, len(argv)):
        sum += int(argv[i])
    print(sum)


if __name__ == "__main__":
    main()
