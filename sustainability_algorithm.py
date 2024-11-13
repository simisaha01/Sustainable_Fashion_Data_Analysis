from sklearn.preprocessing import MinMaxScaler

# Normalize data for scoring
scaler = MinMaxScaler()
data[['Water_Consumption', 'Chemical_Emissions', 'Energy_Usage', 'Cost_Per_Kg']] = scaler.fit_transform(
    data[['Water_Consumption', 'Chemical_Emissions', 'Energy_Usage', 'Cost_Per_Kg']])

# Define a scoring function for sustainability
def sustainability_score(row):
    return (1 - row['Water_Consumption']) * 0.4 + \
           (1 - row['Chemical_Emissions']) * 0.3 + \
           (1 - row['Energy_Usage']) * 0.2 + \
           (1 - row['Cost_Per_Kg']) * 0.1

data['Sustainability_Score'] = data.apply(sustainability_score, axis=1)

# Sort by sustainability score
sustainable_options = data.sort_values(by='Sustainability_Score', ascending=False)

# Display top 5 sustainable options
print(sustainable_options.head(5))
