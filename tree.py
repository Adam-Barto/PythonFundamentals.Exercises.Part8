import os
import sys
import logging

print_to_file_path = 'tree.txt'


def print_out(to_print):
    f = open(print_to_file_path, 'a', newline='\n')
    print(to_print, file=f)


def print_to_file(*file_path):
    path = file_path[0][1]
    for (root, dirs, file) in os.walk(path):
        print_out(str(root).replace(path, '.'))


print_to_file(sys.argv)

## Exercise 2

# Create a program called *tree.py*
#
# Given a file path (absolute or relative), the program should write to a file all of the contents of the directory and the child directories bellow it.
# The output file should look something like this:
#
# ./file1.py
# ./file2.py
# ./dir1/file1_in_dir1.txt
# ./dir1/file2_in_dir1.txt
# ./dir3/file1_in_dir3.txt
