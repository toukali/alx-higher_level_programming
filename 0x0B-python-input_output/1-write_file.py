#!/usr/bin/python3
"""This module defines a text file-writting function"""


def read_file(filename="",s):
    """write the contents in UTF8 text file"""
    with open(filename, encoding="utf-8") as f:
        f.write(s)
