#!/usr/bin/python3
"""hat inserts a line of text to a file, after each line"""


def append_after(filename="", search_string="", new_string=""):
    """nserts a line after a a sting matching line"""
    with open(filename, "r") as f:
        with open(filename, "a") as fw:
            r_line = f.readlines()
            fw.truncate(0)
            for line in r_line:
                if search_string in line:
                    fw.write(line)
                    fw.write(new_string)
                else:
                    fw.write(line)


if __name__ == "__main__":
    append_after()
