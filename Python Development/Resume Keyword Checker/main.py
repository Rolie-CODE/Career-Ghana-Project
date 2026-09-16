import re


def read_resume(filename):
    with open(filename, "r", encoding="utf-8") as resume_file:
        return resume_file.read()


try:
    resume_text = read_resume("resume.txt")
except FileNotFoundError:
    print("Error: resume.txt was not found.")
    raise SystemExit

if not resume_text.strip():
    print("Error: resume.txt is empty.")
    raise SystemExit


def normalize_text(text):
    text = text.lower()
    text = re.sub(r"[^a-z0-9]+", " ", text)
    return re.sub(r"\s+", " ", text).strip()


resume_normalized = normalize_text(resume_text)

job_keywords = [
    "Python",
    "FastAPI",
    "Django",
    "PostgreSQL",
    "Docker",
    "Git",
    "AWS",
    "REST API",
    "Testing",
    "Linux"
]

found_keywords = []
missing_keywords = []

for keyword in job_keywords:
    normalized_keyword = normalize_text(keyword)
    if normalized_keyword in resume_normalized:
        found_keywords.append(keyword)
    else:
        missing_keywords.append(keyword)

print("=" * 40)
print("       RESUME KEYWORD CHECKER")
print("=" * 40)

print("\nKeywords Found:")
for keyword in found_keywords:
    print(f"+ {keyword}")

print("\nKeywords Missing:")
for keyword in missing_keywords:
    print(f"- {keyword}")

total_keywords = len(job_keywords)
number_found = len(found_keywords)
number_missing = len(missing_keywords)

if total_keywords > 0:
    match_percentage = (number_found / total_keywords) * 100
else:
    match_percentage = 0

print("\n" + "-" * 40)
print(f"Total Keywords: {total_keywords}")
print(f"Keywords Found: {number_found}")
print(f"Keywords Missing: {number_missing}")
print(f"Match Percentage: {match_percentage:.2f}%")
print("-" * 40)
