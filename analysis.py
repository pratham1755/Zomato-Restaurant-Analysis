import pandas as pd

import numpy as np

import matplotlib.pyplot as plt

import seaborn as sns

df = pd.read_csv("zomato.csv")

print(df.head())

print(df.info())

print(df.shape)

print(df.describe())

print(df.columns)

print(df.isnull().sum())

df.drop_duplicates(inplace=True)

# Rename columns based on the current dataset schema
df.rename(columns={
    "rate (out of 5)": "Rating",
    "num of ratings": "votes",
    "avg cost (two people)": "Average Cost for two",
    "cuisines type": "Cuisines",
    "area": "City"
}, inplace=True)

# Fill string/object columns with a placeholder, keep numeric columns numeric
obj_cols = df.select_dtypes(include="object").columns
if len(obj_cols) > 0:
    df[obj_cols] = df[obj_cols].fillna("unknown")

# Ensure votes is integer
if "votes" in df.columns:
    df["votes"] = df["votes"].astype(int)

# Convert rating to numeric if needed
if "Rating" in df.columns:
    df["Rating"] = pd.to_numeric(df["Rating"], errors="coerce")
    print(df["Rating"].mean())

if "City" in df.columns:
    df["City"].value_counts()

if "Cuisines" in df.columns:
    df["Cuisines"].value_counts()

# Clean cost values before computing the mean
cost_col = "Average Cost for two"
if cost_col in df.columns:
    df[cost_col] = pd.to_numeric(df[cost_col].astype(str).str.replace(",", "", regex=False), errors="coerce")
    print(df[cost_col].mean())


df["City"].value_counts().head(10).plot(kind="bar")
plt.tight_layout()
plt.show()


plt.hist(df["Rating"].dropna(), bins=20)
plt.title("Rating Distribution")
plt.xlabel("Rating")
plt.ylabel("Count")
plt.show()


if "online_order" in df.columns:
    df["online_order"].value_counts().plot(
        kind="pie",
        autopct="%1.1f%%",
        startangle=90,
        ylabel=""
    )
    plt.title("Online Order Availability")
    plt.tight_layout()
    plt.show()


plt.scatter(
    df["votes"],
    df["Rating"].fillna(0)
)
plt.title("Votes vs Rating")
plt.xlabel("Votes")
plt.ylabel("Rating")
plt.show()


df.to_csv(
"cleaned_zomato.csv",
index=False
)