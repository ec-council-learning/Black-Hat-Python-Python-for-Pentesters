#!/bin/python
"""
unix_password_cracker.py

Purpose: Crack Unix hashed passwords

Author: Cody Jackson

Date: 12/29/2018
########################
Version 0.2
    Added command-line argument parser
Version 0.1
    Initial build
"""
import argparse
import crypt


def argument_parser():
    """Allow user to specify plain-text password repository and username:password file."""
    parser = argparse.ArgumentParser(description="Crack Unix hashed passwords by generating a rainbow table.")
    parser.add_argument("--repo", nargs="?", default="./plaintext_repo.txt", help="Location of the plain-text password "
                                                                                  "file. Default: ./plaintext_repo.txt")
    parser.add_argument("--pass_file", nargs="?", default="./user_passwords.txt", help="Location of the user:password "
                                                                                       "file from the target system. "
                                                                                       "Default: ./user_passwords.txt")
    var_args = vars(parser.parse_args())  # Convert argument namespace to dictionary

    return var_args


def password_check(hashed_pass):
    """Generate a hash digest of plain-text words, then compare to username password digest."""
    salt = hashed_pass[:2]
    with open(plaintext_pwords) as repo:
        for word in repo.readlines():
            word = word.strip("\n")
            digest = crypt.crypt(word, salt)
            if digest == hashed_pass:
                print("[+] Found password: {}\n".format(word))


def parse_file(usernames):
    """Parse a username:password file to find hashed passwords for comparison."""
    with open(usernames) as pass_file:
        for line in pass_file.readlines():
            if ":" in line:
                username = line.split(":")[0]
                pass_digest = line.split(":")[1].strip(" ")
                print("[*] Cracking password for: {}".format(username))
                password_check(pass_digest)


if __name__ == "__main__":
    # Get command-line arguments
    user_args = argument_parser()
    plaintext_pwords = user_args["repo"]
    digests = user_args["pass_file"]

    parse_file(digests)
