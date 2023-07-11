#!/usr/bin/python3
"""Module that saves args of py list"""
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def main():
    with open("add_item.json", 'w') as fw:
        with open("add_item.json", 'r') as fr:
            if fr.read() == '':
                f_r = []
            else:
                f_r = load_from_json_file("add_item.json")
            for arg in sys.argv[1:]:
                f_r.append(arg)
            save_to_json_file(f_r, "add_item.json")


if __name__ == "__main__":
    main()
