import pandas as pd

# Load dataset
data = pd.read_csv("textile_dyeing_data.csv")

# Clean data
data.dropna(inplace=True)
data = data[data['Water_Consumption'] > 0]  # Removing invalid data points

# Display summary
print(data.describe())
