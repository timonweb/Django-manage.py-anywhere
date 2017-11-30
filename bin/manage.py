#!/usr/bin/env python
import os
import subprocess
import sys


def main():
    managepy_path = find_managepy()
    if managepy_path:
        command = ' '.join(['python', managepy_path] + sys.argv[1:])
        run_cmd(command)
    else:
        print("Couldn't find manage.py")


def find_managepy():
    # We start in current directory
    path = '.'
    # We will stop at the root directory
    while os.path.split(os.path.abspath(path))[1]:
        check_path = os.path.join(path, 'manage.py')
        if os.path.exists(check_path):
            return os.path.abspath(check_path)
        # Go level up
        path = os.path.join('..', path)


def run_cmd(command):
    try:
        subprocess.call(command, shell=True)
    except KeyboardInterrupt:
        print("Command aborted")


main()
