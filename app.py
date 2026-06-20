import pandas as pd

# Load cleaned datasets
titanic = pd.read_csv("cleaned_titanic.csv")
house = pd.read_csv("cleaned_housing.csv")

print("========== TITANIC DATASET ==========")
print(titanic.describe())

print("\nTitanic Age Statistics")
print("Mean:", titanic["Age"].mean())
print("Median:", titanic["Age"].median())
print("Standard Deviation:", titanic["Age"].std())
print("Variance:", titanic["Age"].var())

print("\n\n========== HOUSING DATASET ==========")
print(house.describe())

print("\nHousing Price Statistics")
print("Mean:", house["price"].mean())
print("Median:", house["price"].median())
print("Standard Deviation:", house["price"].std())
print("Variance:", house["price"].var())
