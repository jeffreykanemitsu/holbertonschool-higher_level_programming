#!/usr/bin/python3
"""
Prints a text with 2 new lines after each character: '.', '?', and ':'.
"""


def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError('text must be a string')

    reptext = text.replace('.', '.\n\n')
    reptext = text.replace('?', '?\n\n')
    reptext = text.replace(':', ':\n\n')
