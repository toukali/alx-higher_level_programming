#!/usr/bin/python3
"""This module defines a text file-writting function"""


def read_file(filename="",s=""):
    """write the contents in UTF8 text file"""
    with open(filename,"w", encoding="utf-8") as f:
        return f.write(s)
