# Career Ghana Projects

A collection of beginner-friendly Python projects exploring career interests, career suggestions, and job application preparation. Each project can be run independently from its own folder.

## Projects

### 1. Career Quiz CLI Tool

A command-line quiz that asks seven multiple-choice questions about a person's interests. It tallies answers across five broad areas and recommends the highest-scoring career direction:

- Technology and Software
- Creative Design and Media
- Education and Helping Professions
- Business and Entrepreneurship
- Research and Data Analysis

**Run it** from the project folder:

```powershell
cd "Python Development/Career Quiz Tool CLI"
python main.py
```

It uses only Python's standard library. See [the quiz README](Python%20Development/Career%20Quiz%20Tool%20CLI/README.md) for an example interaction.

### 2. Career Path Predictor

A beginner machine-learning project that predicts a career category from sample skill ratings, preferred work environment, and academic background. It includes 36 illustrative profiles across six categories, a Decision Tree model, and an interactive command-line predictor. The notebook walks through training and a sample prediction.

**Install its dependencies** if they are not already available:

```powershell
python -m pip install pandas scikit-learn
```

**Run the interactive script** from the project folder:

```powershell
cd "Python Development/Career Path Prediction"
python main.py
```

Open `main.ipynb` in Jupyter or VS Code to follow the model step by step. The training data is small and synthetic; predictions are educational suggestions, not definitive career advice. More details are in [the predictor README](Python%20Development/Career%20Path%20Prediction/README.md).

### 3. Resume Keyword Checker

A command-line tool that compares a resume with keywords detected from a sample job description. It reports matching and missing terms, plus a match percentage. Edit `resume.txt` and `job_description.txt` in the project folder to try different examples.

**Run it** from the project folder:

```powershell
cd "Python Development/Resume Keyword Checker"
python main.py
```

It uses only Python's standard library. See [the Resume Keyword Checker README](Python%20Development/Resume%20Keyword%20Checker/README.md) for sample output and test ideas.

## Requirements

- Python 3.10 or newer is recommended.
- The quiz and resume checker need no extra packages.
- The Career Path Predictor requires `pandas` and `scikit-learn`.

## Project Structure

```text
Career Ghana Projects/
|-- README.md
`-- Python Development/
    |-- Career Quiz Tool CLI/
    |   |-- main.py
    |   `-- README.md
    |-- Career Path Prediction/
    |   |-- dataset/data.csv
    |   |-- main.ipynb
    |   |-- main.py
    |   `-- README.md
    `-- Resume Keyword Checker/
        |-- job_description.txt
        |-- main.py
        |-- README.md
        `-- resume.txt
```

## Learning Goals

Together, these projects practice command-line input and output, conditional logic, scoring, reading files, text matching, basic data preparation, and supervised machine learning with a Decision Tree. They are intended for learning and experimentation; their recommendations and match scores should not be treated as professional assessments.
