import pandas as pd
import numpy as np
from pathlib import Path
from sklearn.preprocessing import StandardScaler

RAW_FILE = Path("data/raw/DataCoSupplyChainDataset.csv")
OUTPUT_FILE = Path("data/processed/cleaned_logistics_data.csv")

if not RAW_FILE.exists():
    raise FileNotFoundError(
        f"Dataset not found: {RAW_FILE}\n"
        "Download the authorized/public DataCo dataset and place it in data/raw/."
    )

df = pd.read_csv(RAW_FILE)
print("Original shape:", df.shape)

# 1. Standardize column names
df.columns = (
    df.columns.str.strip()
    .str.lower()
    .str.replace(" ", "_", regex=False)
)

# 2. Clean text fields
text_cols = df.select_dtypes(include="object").columns
for col in text_cols:
    df[col] = df[col].astype("string").str.strip()

# 3. Remove exact duplicate rows
print("Exact duplicates:", df.duplicated().sum())
df = df.drop_duplicates().copy()

# 4. Convert dates
date_cols = ["order_date_(dateorders)", "shipping_date_(dateorders)"]
for col in date_cols:
    if col in df.columns:
        df[col] = pd.to_datetime(df[col], errors="coerce")

# 5. Convert numeric columns
numeric_candidates = [
    "sales",
    "shipping_cost",
    "order_item_quantity",
    "days_for_shipping_(real)",
    "days_for_shipment_(scheduled)",
    "benefit_per_order",
]
for col in numeric_candidates:
    if col in df.columns:
        df[col] = pd.to_numeric(df[col], errors="coerce")

# 6. Missing-value report
missing = pd.DataFrame({
    "missing_count": df.isna().sum(),
    "missing_percentage": df.isna().mean() * 100
}).sort_values("missing_percentage", ascending=False)

print("\nMissing-value report:")
print(missing.head(20))

# 7. Example numeric imputation
for col in ["sales", "shipping_cost"]:
    if col in df.columns:
        df[col] = df[col].fillna(df[col].median())

# 8. Example categorical imputation
if "shipping_mode" in df.columns and not df["shipping_mode"].mode().empty:
    df["shipping_mode"] = df["shipping_mode"].fillna(
        df["shipping_mode"].mode()[0]
    )

# 9. IQR outlier report
def iqr_bounds(series):
    q1 = series.quantile(0.25)
    q3 = series.quantile(0.75)
    iqr = q3 - q1
    return q1 - 1.5 * iqr, q3 + 1.5 * iqr

for col in ["sales", "shipping_cost"]:
    if col in df.columns:
        low, high = iqr_bounds(df[col].dropna())
        count = ((df[col] < low) | (df[col] > high)).sum()
        print(f"{col}: {count} IQR outliers; bounds=({low:.2f}, {high:.2f})")

# 10. Standardize selected numeric features
features = [
    c for c in ["sales", "shipping_cost", "order_item_quantity"]
    if c in df.columns
]

if features:
    scaler = StandardScaler()
    df[features] = scaler.fit_transform(df[features])

# 11. Final validation
print("\nFinal shape:", df.shape)
print("Remaining duplicates:", df.duplicated().sum())
print("Remaining missing values:", int(df.isna().sum().sum()))

if "sales" in df.columns:
    print("Negative sales:", int((df["sales"] < 0).sum()))

if "order_item_quantity" in df.columns:
    print("Non-positive quantities:", int((df["order_item_quantity"] <= 0).sum()))

OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
df.to_csv(OUTPUT_FILE, index=False)
print(f"\nProcessed dataset saved to: {OUTPUT_FILE}")
