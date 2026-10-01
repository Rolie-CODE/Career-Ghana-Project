from pathlib import Path

import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.tree import DecisionTreeClassifier
from sklearn.pipeline import Pipeline


DATA_PATH = Path(__file__).parent / "dataset" / "data.csv"
NUMERIC_FEATURES = [
    "Logical_Thinking",
    "Coding_Skills",
    "Public_Speaking",
    "Creativity",
]
CATEGORICAL_FEATURES = ["Preferred_Environment", "Academic_Background"]
FEATURES = NUMERIC_FEATURES + CATEGORICAL_FEATURES
TARGET = "Target_Career"


def build_model(training_data: pd.DataFrame) -> Pipeline:
    """Create and fit a decision tree using the sample career dataset."""
    preprocessor = ColumnTransformer(
        transformers=[
            ("categories", OneHotEncoder(handle_unknown="ignore"), CATEGORICAL_FEATURES),
            ("scores", "passthrough", NUMERIC_FEATURES),
        ]
    )
    model = Pipeline(
        steps=[
            ("preprocessor", preprocessor),
            ("decision_tree", DecisionTreeClassifier(max_depth=5, random_state=42)),
        ]
    )
    model.fit(training_data[FEATURES], training_data[TARGET])
    return model


def prompt_score(label: str) -> int:
    while True:
        value = input(f"Rate your {label} from 1 (low) to 10 (high): ").strip()
        try:
            score = int(value)
        except ValueError:
            print("Please enter a whole number from 1 to 10.")
            continue
        if 1 <= score <= 10:
            return score
        print("The rating must be from 1 to 10.")


def prompt_choice(label: str, choices: list[str]) -> str:
    print(f"{label}: {', '.join(choices)}")
    while True:
        value = input(f"Enter your {label.lower()}: ").strip()
        for choice in choices:
            if value.casefold() == choice.casefold():
                return choice
        print("Choose one of the listed options.")


def main() -> None:
    training_data = pd.read_csv(DATA_PATH)
    model = build_model(training_data)
    print(f"Career Path Predictor (trained on {len(training_data)} sample profiles)")
    print("Rate each skill based on how strong or interested you are in it.")

    person = {
        "Logical_Thinking": prompt_score("logical thinking"),
        "Coding_Skills": prompt_score("coding skills"),
        "Public_Speaking": prompt_score("public speaking"),
        "Creativity": prompt_score("creativity"),
        "Preferred_Environment": prompt_choice(
            "preferred environment", sorted(training_data["Preferred_Environment"].unique())
        ),
        "Academic_Background": prompt_choice(
            "academic background", sorted(training_data["Academic_Background"].unique())
        ),
    }
    prediction = model.predict(pd.DataFrame([person]))[0]
    print(f"\nSuggested career category: {prediction}")
    print("This is a simple practice model, not a definitive career assessment.")


if __name__ == "__main__":
    main()
