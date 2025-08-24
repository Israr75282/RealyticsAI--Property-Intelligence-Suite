import pandas as pd
import re
from rapidfuzz import process
from utils import parse_bhk, parse_budget

# ===== Load Dataset =====
def _load_data():
    path = "final_property_data.csv"
    try:
        data = pd.read_csv(path)
    except FileNotFoundError:
        raise FileNotFoundError(
            f"Dataset not found at '{path}'. Place '{path}' in the same folder as app.py."
        )

    # Normalize column names
    data = data.rename(columns={
        "userid": "user_id",
        "propertyid": "property_id",
        "rating_(1-5)": "rating",
        "bedrooms": "bedrooms",
        "location": "location",
        "total_sqft": "total_sqft",
        "price": "price"
    })

    # Drop rows with missing location/price
    data = data.dropna(subset=["location", "price"])
    data["location"] = data["location"].astype(str).str.lower().str.strip()
    return data

DATA = _load_data()

# ===== Get Recommendations =====
def get_recommendations(query: str, top_k: int = 10) -> pd.DataFrame:
    query = query.lower()

    # Parse bedrooms
    bhk = parse_bhk(query)

    # Parse budget
    budget = parse_budget(query)

    # Extract location keyword
    words = query.split()
    location = None
    if len(words) > 1:
        best_match = process.extractOne(
            " ".join(words),
            DATA["location"].unique(),
            score_cutoff=70
        )
        if best_match:
            location = best_match[0]

    # Start filtering
    df = DATA.copy()

    if bhk:
        df = df[df["bedrooms"] == bhk]

    if budget:
        df = df[df["price"] <= budget]

    if location:
        df = df[df["location"].str.contains(location, case=False, na=False)]

    return df.head(top_k)
