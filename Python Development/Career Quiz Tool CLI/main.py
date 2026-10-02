"""A short interest quiz that suggests a career direction."""


CAREER_PATHS = {
	"technology": "Technology and Software",
	"creative": "Creative Design and Media",
	"helping": "Education and Helping Professions",
	"business": "Business and Entrepreneurship",
	"analytical": "Research and Data Analysis",
}

QUESTIONS = [
	(
		"Which project sounds most interesting?",
		[("Build an app", "technology"), ("Design a poster", "creative"), ("Tutor someone", "helping"), ("Plan a small business", "business"), ("Investigate a question with data", "analytical")],
	),
	(
		"What kind of problem do you enjoy solving?",
		[("A computer or phone issue", "technology"), ("How to make something more attractive", "creative"), ("How to support someone", "helping"), ("How to organize a team or project", "business"), ("Why a result or pattern occurred", "analytical")],
	),
	(
		"Which school or personal task do you enjoy most?",
		[("Coding or using technology", "technology"), ("Drawing, writing, or making videos", "creative"), ("Working with or encouraging others", "helping"), ("Leading a group or planning an event", "business"), ("Math, experiments, or careful research", "analytical")],
	),
	(
		"What would you most like to create?",
		[("A useful digital tool", "technology"), ("A story, image, or piece of music", "creative"), ("A welcoming learning space", "helping"), ("A product people want to buy", "business"), ("A report that explains what is happening", "analytical")],
	),
	(
		"Which role would you choose on a group project?",
		[("Set up the tools", "technology"), ("Make the presentation look great", "creative"), ("Make sure everyone feels included", "helping"), ("Coordinate tasks and deadlines", "business"), ("Check the facts and results", "analytical")],
	),
	(
		"Which workday sounds best?",
		[("Making or improving software", "technology"), ("Designing or producing creative work", "creative"), ("Teaching, coaching, or caring for people", "helping"), ("Making plans and working with customers", "business"), ("Finding insights in information", "analytical")],
	),
	(
		"What would you most like to learn next?",
		[("Programming or robotics", "technology"), ("Photography or graphic design", "creative"), ("Counselling or teaching", "helping"), ("Marketing or starting a business", "business"), ("Statistics or scientific research", "analytical")],
	),
]


def ask_question(number: int, question: str, options: list[tuple[str, str]]) -> str:
	print(f"\n{number}. {question}")
	for option_number, (description, _) in enumerate(options, start=1):
		print(f"  {option_number}. {description}")

	while True:
		answer = input("Choose 1-5: ").strip()
		if answer.isdigit() and 1 <= int(answer) <= len(options):
			return options[int(answer) - 1][1]
		print(f"Please enter a number from 1 to {len(options)}.")


def run_quiz() -> None:
	scores = {category: 0 for category in CAREER_PATHS}
	print("Career Interest Quiz")
	print("Choose the option that sounds most like you for each question.")

	for number, (question, options) in enumerate(QUESTIONS, start=1):
		category = ask_question(number, question, options)
		scores[category] += 1

	# Stable ordering makes ties produce the same result every time.
	winner = max(CAREER_PATHS, key=lambda category: scores[category])
	print("\nYour recommended career direction:")
	print(CAREER_PATHS[winner])
	print("This is a starting point for exploration, not a definitive assessment.")


if __name__ == "__main__":
	run_quiz()
