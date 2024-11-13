# visualize_results.py
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def visualize_top_sustainable_options(data, top_n=5):
    # Get top N sustainable options
    top_techniques = data.head(top_n)

    # Bar plot for sustainability score
    plt.figure(figsize=(10, 6))
    sns.barplot(data=top_techniques, x="Dye_Type", y="Sustainability_Score", palette="viridis")
    plt.title(f"Top {top_n} Sustainable Dyeing Techniques")
    plt.xlabel("Dye Type")
    plt.ylabel("Sustainability Score")
    plt.show()

    # Heatmap to compare key environmental metrics
    metrics = top_techniques[['Dye_Type', 'Water_Consumption', 'Chemical_Emissions', 'Energy_Usage', 'Cost_Per_Kg']]
    metrics.set_index('Dye_Type', inplace=True)
    
    plt.figure(figsize=(10, 6))
    sns.heatmap(metrics, annot=True, cmap="YlGnBu")
    plt.title("Environmental Impact Metrics for Top Sustainable Dyeing Techniques")
    plt.show()

if __name__ == "__main__":
    # Load dataset with sustainability scores
    data = pd.read_csv("data/sustainable_scores.csv")
    visualize_top_sustainable_options(data)
