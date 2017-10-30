"""
Copyright (c) 2017 SimZor, SimZor Studios.
All Rights Reserved.

Free for anyone to use, as long as credits stays.

Module:      tab_check.py
Author:      Simon Arledal
Project:     Ground Wars: Existence
Description: Checks for tabs (Optimal to be used within CI)
"""

from sys import exit
from glob import glob


def check_tabs(file_extensions):
    """

    :return: Returns amount of errors found
    :rtype: int
    """
    tabs_found = 0

    # Loop through all file extensions
    for ext in file_extensions:
        print('Checking file extension {}'.format(ext))
        files = glob('*.{0}'.format(ext))

        # Loop through all files
        for file in files:
            opened_file = open(file, 'r')
            lines = opened_file.readlines()

            print('OPERATION: Checking for tabs in {0}'.format(opened_file.name))

            # Loop through all lines
            for index, line in enumerate(lines):
                # Check for any tabs
                if '\t' in line:
                    print('WARNING: Tab found at line {0}'.format(index))
                    tabs_found += 1

            if tabs_found < 1:
                print('SUCCESS: No tabs found in file {0}'.format(opened_file.name))

            opened_file.close()

    return tabs_found


if __name__ == '__main__':
    errors = check_tabs(['sqf'])
    if errors > 0:
        raise Exception('CRITICAL: Tabs found')
    else:
        exit(0)
