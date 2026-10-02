# Career Path Predictor

A beginner machine-learning project that suggests a career category from sample skill ratings and background details.

## Run the interactive predictor

From this project folder, run:

```powershell
python main.py
```

Rate logical thinking, coding, public speaking, and creativity from 1 to 10. Then choose a preferred work environment and academic background from the listed options. The script trains a Decision Tree from `dataset/data.csv` and prints one suggested category.

## How it works

The CSV contains 36 illustrative profiles, with six examples in each of six career categories. A scikit-learn pipeline converts the text choices into numeric features, keeps the skill ratings numeric, and trains a Decision Tree classifier. For a new profile, the trained tree follows patterns learned from those examples to select a category. This small synthetic dataset is for learning only; its predictions are not definitive career advice.

Open `main.ipynb` to see the same process step by step.
