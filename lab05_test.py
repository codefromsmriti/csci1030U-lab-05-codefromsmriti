# These tests RUN your command-line programs the same way you would in the terminal,
# then check what they print. Each test writes a small temporary file, runs your
# program against it, and compares the output.

import os
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))


def run(script, *args):
    result = subprocess.run(
        [sys.executable, os.path.join(HERE, script), *args],
        capture_output=True, text=True)
    return result.stdout


def write_temp(content, suffix):
    fd, path = tempfile.mkstemp(suffix=suffix, text=True)
    with os.fdopen(fd, "w") as f:
        f.write(content)
    return path


def test_find_matches():
    path = write_temp("apple\nBanana\ncherry\napple pie\n", ".txt")
    try:
        assert run("find.py", "apple", path) == "1: apple\n4: apple pie\n"
        assert run("find.py", "z", path) == ""
    finally:
        os.remove(path)


def test_find_ignore_case():
    path = write_temp("apple\nBanana\nBANANA split\n", ".txt")
    try:
        assert run("find.py", "-i", "banana", path) == "2: Banana\n3: BANANA split\n"
    finally:
        os.remove(path)


# STRETCH (optional) - skipping filter_csv.py still passes the two tests above.
def test_filter_csv():
    csv_text = "name,city,age\nAlice,Oshawa,30\nBob,Toronto,25\nCara,Oshawa,41\n"
    path = write_temp(csv_text, ".csv")
    try:
        assert run("filter_csv.py", path, "city", "Oshawa") == \
            "Alice,Oshawa,30\nCara,Oshawa,41\n"
        assert run("filter_csv.py", path, "city", "Nowhere") == ""
    finally:
        os.remove(path)
