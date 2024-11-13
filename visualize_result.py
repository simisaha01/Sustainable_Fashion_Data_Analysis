# Top sustainable dyeing techniques
top_techniques = sustainable_options.head(5)

plt.figure(figsize=(10, 6))
sns.barplot(data=top_techniques, x="Dye_Type", y="Sustainability_Score", palette="viridis")
plt.title("Top Sustainable Dyeing Techniques")
plt.xlabel("Dye Type")
plt.ylabel("Sustainability Score")
plt.show()
