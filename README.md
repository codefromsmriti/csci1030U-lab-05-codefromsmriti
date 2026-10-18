# Lab 05 - Practical Python: Command-Line Tools and Files

In this lab, we'll build small **command-line programs** - the kind you run from the
terminal and pass arguments to, like the tools you've been using all term. You'll use
the **`argparse`** module to read command-line arguments, and you'll **read files**
from disk. Unlike the earlier labs, you run these programs from the terminal rather
than calling a function.

**Time:** this lab is meant to be finished in the 80-minute session. If you don't
finish, you may keep working during the week and submit any time up to the **first 10
minutes of next week's lab**.  After 10 minutes, though, the lab will not be accepted,
to avoid a cascade effect. The **Lab 05 quiz on Canvas** closes at that moment - that is
where you hand this lab in, so read [How to Submit](#how-to-submit) before you start.

## Getting Started

Lab repositories are **templates**: you make your own copy with one click.

1. Open the **Lab 05 template** link in the Canvas lab quiz.
2. Click the green **Use this template** button, then **Create a new repository**.
3. Fill in the form:
   - **Owner:** Your own account
   - **Repository name:** `lab04-csci1030u`
   - **Visibility:** **Private**
4. Click **Create repository**.

Use **Use this template**, not **Fork** - a fork can never be made private, which would
show your solution to the whole class.  For the TA to see your work, you will need to add them as a collaborator.

Then clone it. On your new repo's page, click the green **Code** button and copy the URL.
In the folder where you keep your CSCI 1030U labs:

```
git clone https://github.com/CSCI1030U/lab05-your-username
cd lab05-your-username
```

Two small data files, `sample.txt` and `people.csv`, are included so you can try your
programs by hand as you go.

## Instructions

You'll finish two programs, `find.py` and `filter_csv.py`. In each one, the argument
parser is already started for you - look for the `# TODO` comments. Print your results
with `print()`.

### Part 1 - `find.py` (a mini "grep")

Finish `find.py` so that it prints every line of a file that **contains** a given
pattern, each prefixed with its line number (counting from 1). Then add an optional
`-i` / `--ignore-case` flag that makes the match ignore upper/lower case.

Run it from the terminal like this:

```
$ python find.py apple sample.txt
1: apple
4: apple pie

$ python find.py -i apple sample.txt
1: apple
4: apple pie
6: Apple juice
```

Hints:
- `parser.add_argument("-i", "--ignore-case", action="store_true")` adds the flag;
  its value is then available as `args.ignore_case` (`True` or `False`).
- Open the file with `open(args.filename)` and loop over its lines. `enumerate(lines,
  start=1)` gives you both the line number and the line.
- A line still has its newline on the end when you read it - `line.rstrip("\n")`
  removes it.
- To match ignoring case, compare the lowercased versions of both strings.

### Part 2 - `filter_csv.py` (filter a spreadsheet)  *(stretch - optional)*

Finish `filter_csv.py` so that it prints the rows of a CSV file where a chosen
**column** equals a chosen **value**. The first row of the file is the header (the
column names).

```
$ python filter_csv.py people.csv city Oshawa
Alice,Oshawa,30
Cara,Oshawa,41
```

Hints:
- Read the file with `csv.reader` and turn it into a list of rows.
- The header row tells you which position your column is in: `header.index(args.column)`.
- For each remaining row, compare the value at that position to `args.value`; when it
  matches, print the row's values joined by commas (`",".join(row)`).

This part is optional - Part 1 is the core of the lab. Do it if you have time.

## Verifying Correctness

Run the pre-written tests to check your work:

```
pytest
```

These tests actually **run your programs** (with their own temporary files) and check
what they print, so make sure your output matches the examples exactly. Read a failing
test closely - it shows what it expected versus what your program printed.

## Getting Help

There is a lab instructor present for the whole session. Ask them whenever you're
stuck.

*The instructor will usually help you find the problem rather than tell you how to
fix it - the goal is for you to get better at diagnosing and fixing your own bugs.*

## How to Submit

Handing in a lab is two steps: **push your work**, then **record it in the Canvas quiz**.
This is the same routine for every lab.

### Step 1 - Commit and push

Once your tests pass (or the session is ending):

```
git add --all
git commit -m "Lab 05 completed"
git push origin main
```

Then open your repository page on GitHub and check that your changed files are actually
there. That is your confirmation the push worked.

> **Check your own work with `pytest`, on your own machine.** Your repository has an
> autograder, but it does not run when you push - your instructor runs it during marking,
> against the commit hash you submit below. So `pytest` passing locally is the only
> pass/fail signal you get, and it is the one that counts. Don't submit without running it.

### Step 2 - Get the commit hash

Check that everything really is committed and pushed, then read the hash of that snapshot:

```
git status
git rev-parse HEAD
```

`git status` should say `nothing to commit, working tree clean` and that your branch is up
to date with `origin/main`. If it lists changes, go back to Step 1. Then `git rev-parse HEAD`
prints a 40-character hash, like `3f9a1c2e8b7d4056a1f2e3d4c5b6a7f8091a2b3c`.

### Step 3 - Submit the quiz

Open the **Lab 05 quiz on Canvas** and enter:

- your **repository URL**: `https://github.com/CSCI1030U/lab05-your-username`
- your **commit hash**, pasted exactly as `git rev-parse HEAD` printed it

Then answer the remaining questions and submit. **The Canvas submission time is your
submission time**, and the commit hash you give is the snapshot that gets marked - anything
you push afterwards is not seen. If you fix something important later, get the new hash and
resubmit if the quiz still allows it.

## Using AI

You may use an AI assistant to **explain ideas and help you learn** - but **not to
generate code you submit** in this half of the term. Use only a **free** model, and be
ready to explain every line you wrote; the lab instructor may ask you to walk through
your code.
