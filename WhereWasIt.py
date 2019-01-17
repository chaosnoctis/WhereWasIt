#!/usr/bin/env python 

import os
import pathlib
import re

def find_directory():
    print('This is your current directory: ', os.getcwd())
    while True:
        user = input(
            "Please enter the absolute path of the directory at which you want searched.\n> ")
        if user == "":
            user = None
        # Asks the user to enter the path they want searched
        if os.path.isdir(f'{user}'):
            os.chdir('{}'.format(user))
            break
        print("You entered", f"{user} \n That is not a correct absolute path. Please try again.\n\n")
    result = 'You are now in this directory:\n' + os.getcwd()
    print(result)
    return os.getcwd()


def search_specific_file(pattern=None):
    # Obtain a list of the files in the current working directory and print them on the screen
    print('These are your files in this directory:\n')
    flist = [x for x in pathlib.Path().iterdir() if x.is_file()]
    for i in flist:
        print(i)
    # Allow user to choose what file they want to open and store it in a
    # variable
    while True:
        file = input("What file do you want to open?\n> ")
        if os.path.isfile(os.path.join('.', file)):
            break
        else:
            print("That is not a file in this directory. Please try again.\n\n")
    # Open the file and search of a pattern as specified in the function above
    # The statement below correctly returns whether the line contains the
    # pattern or not
    with open(f'{file}', 'r') as f:
        if pattern is None:
            print('You did not specify a pattern, file closing...')
            f.close()
        if pattern in f.read():
            print('The string is in this file!')
        elif pattern not in f.read():
            print('Pattern was not found')


def search_all_files(pattern=None):
   # Copy the list of files in the directory from the last function
   # Iterate over the list of files, opening and searching in each one until it gets a match
   # Similar to search specific file but more automated/looping
    rpattern = re.compile('{}'.format(pattern))

    print('These are your files in this directory:\n')
    flist = [x for x in pathlib.Path().iterdir() if x.is_file()]
    for num, i in enumerate(flist,1):
        print(num,'.)',i)
    print('\nWe are going to scan these files now...')
    for num, i in enumerate(flist, 1):
        with i.open(encoding="latin-1") as f:
            if pattern is None:
                print('You did not specify a pattern, file closing...')
                f.close()
            if rpattern.search(f.read()):
                print(num, i, 'The string is in this file!')
            else:
                print(num, i, 'Pattern was not found')

# find_directory()
#search_specific_file(input("What's the pattern"))
search_all_files(input("What's the pattern?\n> "))
