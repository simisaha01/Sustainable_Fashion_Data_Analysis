import matplotlib.pyplot as plt
import seaborn as sns

# Visualize water consumption by dye type
plt.figure(figsize=(10, 6))
sns.boxplot(data=data, x='Dye_Type', y='Water_Consumption')
plt.title("Water Consumption by Dye Type")
plt.show()

# Pairplot to show relationships between key metrics
sns.pairplot(data, hue="Dye_Type")
plt.show()
