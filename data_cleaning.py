# data_cleaning.py
import pandas as pd

def load_and_clean_data(filepath):
    # Load dataset
    data = pd.read_csv(filepath)

    # Drop rows with missing values
    data.dropna(inplace=True)

    # Remove invalid or zero values for environmental metrics
    data = data[(data['Water_Consumption'] > 0) & 
                (data['Chemical_Emissions'] > 0) & 
                (data['Energy_Usage'] > 0) & 
                (data['Cost_Per_Kg'] > 0)]
    
    # Display basic information
    print("Cleaned Data Summary:")
    print(data.describe())
    
    return data

if __name__ == "__main__":
    filepath = "data/textile_dyeing_data.csv"
    data = load_and_clean_data(filepath)

