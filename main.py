import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

titanic = pd.read_csv("cleaned_titanic.csv")
house = pd.read_csv("cleaned_housing.csv")

# Titanic Correlation
print("TITANIC CORRELATION MATRIX")
print(
    titanic[
        ["Survived", "Age", "Fare", "Pclass", "SibSp", "Parch"]
    ].corr()
)

# Housing Correlation
print("\nHOUSING CORRELATION MATRIX")
print(
    house[
        ["price", "area", "bedrooms", "bathrooms", "stories", "parking"]
    ].corr()
)

# Housing Heatmap
plt.figure(figsize=(8,6))
sns.heatmap(
    house[
        ["price", "area", "bedrooms", "bathrooms", "stories", "parking"]
    ].corr(),
    annot=True,
    cmap="coolwarm"
)

plt.title("Housing Correlation Heatmap")
plt.show()