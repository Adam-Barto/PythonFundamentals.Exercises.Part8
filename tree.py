import os
import sys
import logging

print_to_file_path = 'tree.txt'
user_input = sys.argv


def print_out(to_print):
    f = open(print_to_file_path, 'a', newline='\n')
    print(to_print, file=f)


def print_to_file(path):
    for (root, dirs, file) in os.walk(path):
        print_out(str(root).replace(path, '.'))


def file_checker(user_input: str) -> None:
    file = None
    try:
        file = open(print_to_file_path)
    except OSError as e:
        print("Error opening the file. Please ensure the file exists and has appropriate permissions.")
        logging.error(e)
    else:
        print_to_file(user_input)
    finally:
        file.close() if file else logging.warning("No file resource available to close.")


if len(user_input) > 1:
    file_checker(user_input[1])
else:
    file_checker(os.curdir) # outprints a different directory then expected

