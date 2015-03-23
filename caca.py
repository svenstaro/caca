#!/usr/bin/env python3
# encoding: utf-8

import argparse
import shutil

DESCRIPTION = """caca - Copy And Convert Audio.

A very simple one-shot parallel audio converter that behaves a lot cp"""


def detect_utils():
    tools = ['flac', 'lame', 'oggenc']
    for tool in tools:
        if not shutil.which(tool):
            raise FileNotFoundError("'{}' was not found on your system but is required".format(tool))


def handle_file(src):
    

def main():
    parser = argparse.ArgumentParser(description=DESCRIPTION)
    parser.add_argument("sources", metavar="SOURCE", nargs='+', help="input path")
    parser.add_argument("target", metavar="TARGET", help="output path")
    parser.add_argument("-v", "--verbose", help="print progress output", action="store_true")
    parser.add_argument("-R", "-r", "--recursive", help="copy directories recursively", action="store_true")
    parser.add_argument("-a", "--archive", help="same as --recursive but preserves attributes", action="store_true")
    args = parser.parse_args()

    detect_utils()

    if args.verbose:
        print("Copying {} to {}")

if __name__ == '__main__':
    main()
