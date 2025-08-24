import pandas as pd

# Load dataset
file_path = "cleaned1_property_data for recommendation.csv"
data = pd.read_csv(file_path)

# STEP 1: Fix column names (remove spaces, lower case)
data.columns = data.columns.str.strip().str.lower().str.replace(" ", "_")

# STEP 2: Handle missing values
data = data.fillna(0)  # replace NaN with 0 (or choose strategy)

# STEP 3: Convert numeric fields safely
data["total_sqft"] = pd.to_numeric(data["total_sqft"], errors="coerce")
data["price"] = pd.to_numeric(data["price"], errors="coerce")

# STEP 4: Drop rows with invalid values if necessary
data = data.dropna(subset=["total_sqft", "price"])

# STEP 5: Save cleaned dataset
output_path = "cleaned2_property_data.csv"
data.to_csv(output_path, index=False)

print("✅ Cleaned dataset saved:", output_path)
print("Final shape:", data.shape)
print("Columns:", data.columns.tolist())
