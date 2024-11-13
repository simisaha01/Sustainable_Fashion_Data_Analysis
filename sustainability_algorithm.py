# sustainability_algorithm.py
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def calculate_sustainability_score(data):
    # Normalize environmental metrics
    scaler = MinMaxScaler()
    data[['Water_Consumption', 'Chemical_Emissions', 'Energy_Usage', 'Cost_Per_Kg']] = \
        scaler.fit_transform(data[['Water_Consumption', 'Chemical_Emissions', 'Energy_Usage', 'Cost_Per_Kg']])

    # Define sustainability scoring function
    def sustainability_score(row):
        return (1 - row['Water_Consumption']) * 0.4 + \
               (1 - row['Chemical_Emissions']) * 0.3 + \
               (1 - row['Energy_Usage']) * 0.2 + \
               (1 - row['Cost_Per_Kg']) * 0.1

    # Apply the scoring function to each row
    data['Sustainability_Score'] = data.apply(sustainability_score, axis=1)
    
    return data.sort_values(by='Sustainability_Score', ascending=False)

if __name__ == "__main__":
    # Load cleaned data
    data = pd.read_csv("data/textile_dyeing_data.csv")
    data = calculate_sustainability_score(data)
    
    # Display top 5 sustainable dyeing options
    print("Top 5 Sustainable Dyeing Options:")
    print(data[['Dye_Type', 'Sustainability_Score']].head(5))

