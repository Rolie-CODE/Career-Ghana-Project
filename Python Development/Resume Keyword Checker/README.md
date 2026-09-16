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
2. The important keywords are currently written manually in a list inside `main.py`.
3. The resume and keywords are normalized to make matching case-insensitive and less affected by punctuation or extra spaces.
4. The program displays found keywords, missing keywords, totals, and a match percentage.

This project does not use machine learning, NLP libraries, databases, APIs, or web scraping.

`job_description.txt` is currently a reference file only. The program does not read or extract keywords from it yet.

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

## Future Improvement Plan

The next major improvement will be to remove the hardcoded keyword list from `main.py`.

### Planned Workflow

1. Read the job description from `job_description.txt`.
2. Store the job description in a variable.
3. Extract likely requirements from the description using simple rules from Python's standard library.
4. Normalize the extracted requirements in the same way as the resume text.
5. Compare the extracted requirements with the resume.
6. Print the found requirements, missing requirements, and match percentage.

### Possible Implementation Steps

The improvement could be built gradually:

1. Create a reusable function such as `read_text_file()` for reading both text files.
2. Create an `extract_keywords()` function.
3. Begin with a simple list of known technical terms and check which ones appear in the job description.
4. Improve the rules to recognize phrases such as `REST API`, `software testing`, and `cloud platforms`.
5. Keep the matching case-insensitive and tolerant of punctuation and extra spaces.
6. Add error handling for a missing or empty `job_description.txt`.
7. Test the program with several job descriptions.

### Important Limitation

Automatically deciding which words are requirements is more difficult than simply finding every word in a job description. A simple standard-library solution may need a list of common skills or rules for recognizing technical terms. It may also include unimportant words or miss requirements written in an unusual way.

The goal of this future version is to create a useful and understandable rule-based extractor without adding machine learning, NLP libraries, databases, APIs, or web scraping.
