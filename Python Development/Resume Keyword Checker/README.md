# Resume Keyword Checker

A beginner-friendly command-line Python project that checks whether a resume contains important keywords from a sample job description.

## Project Structure

```text
Resume Keyword Checker/
|
|-- main.py
|-- resume.txt
|-- job_description.txt
`-- README.md
```

## Requirements

- Python 3
- No third-party packages

The program uses only Python's standard library.

## How It Works

1. `main.py` reads the resume from `resume.txt`.
2. The important keywords are listed in `main.py` after being selected from `job_description.txt`.
3. The resume and keywords are normalized to make matching case-insensitive and less affected by punctuation or extra spaces.
4. The program displays found keywords, missing keywords, totals, and a match percentage.

This project does not use machine learning, NLP libraries, databases, APIs, or web scraping.

## How to Run

Open a terminal in this folder and run:

```powershell
python main.py
```

## Sample Output

```text
========================================
       RESUME KEYWORD CHECKER
========================================

Keywords Found:
+ Python
+ FastAPI
+ PostgreSQL
+ Docker
+ Git
+ REST API
+ Testing

Keywords Missing:
- Django
- AWS
- Linux

----------------------------------------
Total Keywords: 10
Keywords Found: 7
Keywords Missing: 3
Match Percentage: 70.00%
----------------------------------------
```

## Try Different Resumes

Edit `resume.txt` and run the program again. Try these tests:

- Add `Django` and `Linux`; both should move to the found list.
- Remove `AWS`; it should move to the missing list.
- Change `Python` to `python`; it should still match.
- Add punctuation or extra spaces; the matching should still work.
- Empty `resume.txt`; the program should report that the file is empty.

## Learning Concepts

This project practices:

- Reading text files with `open()` and `with`
- Functions
- Lists
- `for` loops
- `if` statements
- String methods such as `.lower()` and `.strip()`
- Regular expressions from Python's `re` module
- Basic counting and percentage calculations
- Simple error handling with `try` and `except`
