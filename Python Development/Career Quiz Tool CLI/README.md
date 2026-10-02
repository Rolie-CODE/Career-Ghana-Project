# Career Quiz CLI Tool

A short Python command-line quiz that recommends a broad career direction based on your interests. It uses only Python's standard library; no packages need to be installed.

## Run it

Open a terminal in this folder and run:

```powershell
python main.py
```

For each of the seven questions, enter the number beside the option that sounds most interesting to you. The quiz counts your selections by category and recommends the category with the most points. If categories tie, it uses a consistent built-in category order.

## Example run

```text
Career Interest Quiz
Choose the option that sounds most like you for each question.

1. Which project sounds most interesting?
  1. Build an app
  2. Design a poster
  3. Tutor someone
  4. Plan a small business
  5. Investigate a question with data
Choose 1-5: 1

... (answer the remaining six questions)

Your recommended career direction:
Technology and Software
This is a starting point for exploration, not a definitive assessment.
```

The five possible directions are technology and software, creative design and media, education and helping professions, business and entrepreneurship, and research and data analysis. Each answer adds one point to its category, and the highest-scoring category becomes the recommendation.
