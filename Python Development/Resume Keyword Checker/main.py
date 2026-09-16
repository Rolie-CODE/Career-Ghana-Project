import re


def read_text_file(filename):
    try:
        with open(filename, "r", encoding="utf-8") as text_file:
            text = text_file.read()
    except FileNotFoundError:
        print(f"Error: {filename} was not found.")
        return None

    if not text.strip():
        print(f"Error: {filename} is empty.")
        return None

    return text


resume_text = read_text_file("resume.txt")
job_description_text = read_text_file("job_description.txt")

if resume_text is None or job_description_text is None:
    raise SystemExit


def normalize_text(text):
    text = text.lower()
    text = re.sub(r"[^a-z0-9]+", " ", text)
    return re.sub(r"\s+", " ", text).strip()


TECHNICAL_TERMS = [
    "Python",
    "FastAPI",
    "Django",
    "PostgreSQL",
    "Docker",
    "Git",
    "AWS",
    "REST API",
    "Software Testing",
    "Unit Testing",
    "Machine Learning",
    "Data Analysis",
    "Cloud Computing",
    "Version Control",
    "Linux",
    "JavaScript",
    "SQL",
]


REQUIREMENT_ALIASES = {
    "software testing": ["software testing", "testing"],
}


def contains_requirement(text, requirement):
    normalized_text = normalize_text(text)
    normalized_text = re.sub(r"\bapis\b", "api", normalized_text)
    padded_text = f" {normalized_text} "
    normalized_requirement = normalize_text(requirement)
    possible_forms = REQUIREMENT_ALIASES.get(
        normalized_requirement,
        [normalized_requirement],
    )

    for form in possible_forms:
        if f" {form} " in padded_text:
            return True

    return False


def extract_keywords(job_description):
    extracted_keywords = []

    for term in TECHNICAL_TERMS:
        if contains_requirement(job_description, term) and term not in extracted_keywords:
            extracted_keywords.append(term)

    return extracted_keywords


def compare_requirements(requirements, resume_text):
    found_requirements = []
    missing_requirements = []

    for requirement in requirements:
        if contains_requirement(resume_text, requirement):
            found_requirements.append(requirement)
        else:
            missing_requirements.append(requirement)

    return found_requirements, missing_requirements


requirements = extract_keywords(job_description_text)

if not requirements:
    print("Warning: No technical requirements were found in job_description.txt.")

found_requirements, missing_requirements = compare_requirements(
    requirements,
    resume_text,
)

print("=" * 40)
print("       RESUME KEYWORD CHECKER")
print("=" * 40)

print("\nJob Requirements Found:")
for requirement in found_requirements:
    print(f"+ {requirement}")

print("\nMissing Requirements:")
for requirement in missing_requirements:
    print(f"- {requirement}")

total_requirements = len(requirements)
number_found = len(found_requirements)
number_missing = len(missing_requirements)

if total_requirements > 0:
    match_percentage = (number_found / total_requirements) * 100
else:
    match_percentage = 0

print("\n" + "-" * 40)
print(f"Total Requirements: {total_requirements}")
print(f"Requirements Found: {number_found}")
print(f"Requirements Missing: {number_missing}")
print(f"Match Percentage: {match_percentage:.2f}%")
print("-" * 40)
