# exploratory_analysis.py
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def visualize_data(data):
    # Plot water consumption by dye type
    plt.figure(figsize=(10, 6))
    sns.boxplot(data=data, x='Dye_Type', y='Water_Consumption')
    plt.title("Water Consumption by Dye Type")
    plt.show()

    # Pairplot to show relationships between environmental metrics
    sns.pairplot(data, hue="Dye_Type")
    plt.title("Pairwise Relationship of Environmental Metrics")
    plt.show()

if __name__ == "__main__":
    # Load cleaned data
    data = pd.read_csv("data/textile_dyeing_data.csv")
    visualize_data(data)

