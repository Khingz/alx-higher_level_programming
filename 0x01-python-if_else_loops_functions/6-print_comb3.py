#!/usr/bin/python3
for i in range(100):
    num1 = i / 10
    num2 = i % 10
    if num1 < num2 and num1 != num2:
        if i != 89:
            print("{:02d}, ".format(i), end='')
        else:
            print("{:02d}".format(i))
