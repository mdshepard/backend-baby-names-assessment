#!/usr/bin/env python
# -*- coding: utf-8 -*-

# BabyNames python coding exercise.

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import argparse

"""
Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 -Extract the year and print it
 -Extract the names and rank numbers and just print them
 -Get the names data into a dict and print it
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
"""


def extract_names(filename):
    """
    Given a file name for baby.html, returns a list starting with the year
    string followed by the name-rank strings in alphabetical order.
    ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
    """
    # +++your code here++
    name_list = []
    searched_file = open(filename, 'r')
    text = searched_file.read()
    year = re.search(r'Popularity\sin\s(\d\d\d\d)', text)
    name_list.append(year.group(1))
    names = re.findall(r'<td>(\d+)</td><td>(\w+)</td>\<td>(\w+)</td>', text)
    ranked_dict = {}

    for name in names:
        rank, boy, girl = name
        if boy not in ranked_dict:
            ranked_dict[boy] = rank
        if girl not in ranked_dict:
            ranked_dict[girl] = rank

    ordered_names = sorted(ranked_dict.keys())
    for name in ordered_names:
        name_list.append(name + ' ' + ranked_dict[name])
    return name_list


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--summaryfile', help='creates a summary file', action='store_true'
        )
    parser.add_argument(
        'files', help='filename(s) to parse', nargs='+'
        )
    return parser


def main():
    """# This command-line parsing code is provided.

    # The nargs option instructs the parser to expect 1 or more filenames.
    # It will also expand wildcards just like the shell,
    #  e.g. 'baby*.html' will work."""
    parser = create_parser()
    args = parser.parse_args()
    if not args:
        parser.print_usage()
        sys.exit(1)

    file_list = list(args.files)

    # option flag
    create_summary = args.summaryfile
    # +++your code here+++
    # For each filename, get the names, then either print the text output
    # or write it to a summary file

    for f in file_list:
        baby_file = f
        names = extract_names(baby_file)
        baby_names = '\n'.join(names)

        if create_summary:
            stripped_fname = baby_file[0:-5]
            summary_template = (stripped_fname + '.summary')
            new_summary = open(summary_template, 'w')
            new_summary.write(baby_names + '\n')
            new_summary.close()
        else:
            print(baby_names)


if __name__ == '__main__':
    main()
