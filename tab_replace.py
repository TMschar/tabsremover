"""
Copyright (c) 2017 SimZor, SimZor Studios.
All Rights Reserved.

Free for anyone to use, as long as credits stays.

Module:      tab_replace.py
Author:      Simon Arledal
Project:     Ground Wars: Existence
Description: Replaces tabs with 4 spaces
"""

from glob import glob


def add_to_string(string, times, addition):
    for i in range(times):
        string += addition
    return string


def replace_tabs_with_spaces(file_extensions, spaces):
    """

    :return: Returns amount of errors found
    :rtype: int
    """
    tabs_found = 0

    # Loop through all file extensions
    for ext in file_extensions:
        print('Checking file extension {}'.format(ext))
        files = glob('src/**/*.{0}'.format(ext), recursive=True)

        # Loop through all files
        for file in files:
            print('OPERATION: Checking for tabs in {0}'.format(file))
            opened_file = open(file, 'r+')
            lines = opened_file.readlines()

            # Loop through all lines
            newlines = []
            for index, line in enumerate(lines):
                # Check for a tab character in the line
                if '\t' in line:
                    # Increment tabs found
                    tabs_found += 1

                    # Notify
                    print('INFO: Found a tab at line {0} in {2}. Replaced with {1} spaces.'.format(index, spaces, file))

                # Replace with x spaces
                chars = add_to_string('', spaces, ' ')
                replaced = line.replace('\t', '{0}'.format(chars))
                newlines.append(replaced)

            opened_file.close()
            opened_file = open(file, 'w')
            opened_file.writelines(newlines)

    if tabs_found < 1:
        print('SUCCESS: Found 0 tabs')

    return tabs_found


if __name__ == '__main__':
    replace_tabs_with_spaces(['sqf'], 4)
