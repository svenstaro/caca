#!/usr/bin/env python3
# encoding: utf-8

import argparse
import shutil
import os

DESCRIPTION = """caca - Copy And Convert Audio.

A very simple one-shot parallel audio converter that behaves a lot like cp"""


def detect_utils():
    tools = ['flac', 'lame', 'oggenc']
    for tool in tools:
        if not shutil.which(tool):
            raise FileNotFoundError("'{}' was not found on your system but is required".format(tool))


def handle_path(src, target):
    for entry in os.walk(src):
        for file in entry[2]:
            if os.path.splitext(file)[1].tolower() == ".flac":
                #os.makedirs(
                # encoding magic
                if args.verbose:
                    print("'{}' -> '{}'".format(src, target))
            else:
                dst = target
                #os.makedirs(dst, exist_ok=True)
                if args.verbose:
                    print("'{}' -> '{}'".format(src, target))


def main():
    parser = argparse.ArgumentParser(description=DESCRIPTION)
    parser.add_argument("sources", metavar="SOURCE", nargs='+', help="input path")
    parser.add_argument("target", metavar="TARGET", help="output path")
    parser.add_argument("-v", "--verbose", help="print progress output", action="store_true")
    parser.add_argument("-R", "-r", "--recursive", help="copy directories recursively", action="store_true")
    parser.add_argument("-a", "--archive", help="same as --recursive but preserves attributes", action="store_true")
    args = parser.parse_args()

    detect_utils()

    # Handle case where we have more than one sources but target is not a directory
    if len(args.sources) > 1 and os.path.isfile(args.target):
        raise RuntimeException("target '{}' is not a directory".format(args.target))

    # Handle case where the source is a directory but target is a file
    if os.path.isdir(args.sources[0]) and os.path.isfile(args.target):
        raise RuntimeException("cannot overwrite non-directory '{}' with directory '{}'".format(args.target, args.sources[0]))

    for src in args.sources:
        handle_path(src)

if __name__ == '__main__':
    main()
