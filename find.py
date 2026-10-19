# Part 1 - a small "find" tool (like a simplified `grep`).
#
# This is a COMMAND-LINE program: you run it from the terminal and pass it
# arguments, e.g.   python find.py apple sample.txt
#
# The argument parser is started for you. Finish the TODOs below.

import argparse


def main():
    parser = argparse.ArgumentParser(
        description="Print the lines of a file that contain a given pattern.")
    parser.add_argument("pattern", help="the text to look for")
    parser.add_argument("filename", help="the file to search")
    parser.add_argument(
        "-i", "--ignore-case", 
        action="store_true",
        help="ignore uppercase/lowercase differences"
    )

    args = parser.parse_args()

    with open(args.filename) as file:
        for number, line in enumerate(file, start=1):
            if args.ignore_case:
                match = args.pattern.lower() in line.lower()
            else:
                match = args.pattern in line
            if match:
                print(f"{number}: {line.rstrip('\n')}")

if __name__ == "__main__":
    main()
