from pathlib import Path
import random
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score

ROOT = Path(__file__).resolve().parent
DATA = ROOT / "data" / "career_roles.csv"

def load_roles():
    return pd.read_csv(DATA).fillna("")

def train_model():
    """Train an educational role classifier from curated role-skill profiles.
    The generated variations are synthetic training examples, not labor-market data.
    """
    roles = load_roles()
    rng = random.Random(42)
    texts, labels = [], []
    for _, row in roles.iterrows():
        skills = [s.strip() for s in row["skills"].split(",")]
        for _ in range(100):
            chosen = [s for s in skills if rng.random() > 0.22]
            if not chosen:
                chosen = rng.sample(skills, min(2, len(skills)))
            extras = rng.sample(skills, min(rng.randint(0, 2), len(skills)))
            texts.append(" ".join(chosen + extras))
            labels.append(row["role"])
    X_train, X_test, y_train, y_test = train_test_split(
        texts, labels, test_size=0.2, random_state=42, stratify=labels
    )
    model = Pipeline([
        ("tfidf", TfidfVectorizer(ngram_range=(1, 2), sublinear_tf=True)),
        ("classifier", LogisticRegression(max_iter=1500, class_weight="balanced"))
    ])
    model.fit(X_train, y_train)
    score = accuracy_score(y_test, model.predict(X_test))
    return model, score, roles

def recommend(profile_text, top_n=3):
    model, score, roles = train_model()
    probabilities = model.predict_proba([profile_text])[0]
    classes = model.named_steps["classifier"].classes_
    ranked = sorted(zip(classes, probabilities), key=lambda x: x[1], reverse=True)[:top_n]
    results = []
    profile = profile_text.lower()
    for role, probability in ranked:
        row = roles.loc[roles["role"] == role].iloc[0]
        required = [s.strip() for s in row["skills"].split(",")]
        missing = [s for s in required if s.lower() not in profile]
        results.append({
            "role": role,
            "category": row["category"],
            "model_score": float(probability),
            "matched_skills": [s for s in required if s.lower() in profile],
            "missing_skills": missing,
            "roadmap": row["roadmap"],
            "salary_min_lpa": float(row["salary_min_lpa"]),
            "salary_max_lpa": float(row["salary_max_lpa"]),
        })
    return results, score
