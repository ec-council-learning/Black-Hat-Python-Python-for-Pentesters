#!/bin/python
"""
zip_file_cracker.py

Purpose: Crack compressed ZIP file password

Author: Cody Jackson

Date: 12/30/2018
########################
Version 0.1
    Initial build
"""
import argparse
import zipfile

from threading import Thread


def argument_parser():
    """Allow user to specify plain-text password repository and zipped file."""
    parser = argparse.ArgumentParser(description="Password protected ZIP file cracker")
    parser.add_argument("file", help="Location of the ZIP file")
    parser.add_argument("passwords", nargs="?", default="./plaintext_repo.txt", help="Location of the plain-text "
                                                                                     "password file. Default: "
                                                                                     "./plaintext_repo.txt")

    var_args = vars(parser.parse_args())  # Convert argument namespace to dictionary

    return var_args


def threaded_ops():
    """Use threads to iterate through all possible passwords."""
    zipped_file = zipfile.ZipFile(zip_file)
    with open(passwords) as pass_file:
        for line in pass_file.readlines():  # Check each password in the file
            password = line.strip('\n')  # Get rid of newline characters
            t = Thread(target=extract_file, args=(zipped_file, password))
            t.start()


def extract_file(zipped_file, password):
    """For each password, check if it opens the ZIP file."""
    try:
        zipped_file.extractall(pwd=password.encode("cp850", "replace"))  # Encoding required to passwords are parsed
        print("[+] Found ZIP file password: {}".format(password))
    except RuntimeError:  # Ignore invalid passwords
        pass
    except FileExistsError:  # Ignore existing extraction directory
        pass


if __name__ == '__main__':
    # Get command-line arguments
    user_args = argument_parser()
    zip_file = user_args["file"]
    passwords = user_args["passwords"]

    threaded_ops()
