import pandas as pd
import matplotlib.pyplot as plt

# Load your dataset into a DataFrame
filepath = "C:/Users/Sindiso/Documents/python/adclicksrate/ad click rates according to gender.xlsx"
df = pd.read_excel(filepath)

# Check for missing values
missing_values = df.isnull().sum()

# Print the number of missing values for each column
print("Missing values in the dataset:")
print(missing_values)

# This code will check unique values in the "Gender" and "AD clicks" columns
unique_genders = df['Gender'].unique()
unique_ad_clicks = df['AD clicks'].unique()

# Print unique values
print("Unique values in the 'Gender' column:")
print(unique_genders)
print("Unique values in the 'AD clicks' column:")
print(unique_ad_clicks)

# Verify consistency in Gender Column
if 'M' in unique_genders and 'F' in unique_genders:
    print("The 'Gender' column has consistent entries.")
else:
    print("The 'Gender' column does not have consistent entries.")

# Verify consistency in AD clicks Column
if 'Clicked' in unique_ad_clicks and 'Not Used' in unique_ad_clicks and 'Used' in unique_ad_clicks:
    print("The 'AD clicks' column has consistent entries.")
else:
    print("The 'AD clicks' column does not have consistent entries.")

# Print column names to check for correctness
print("Column names in the DataFrame:")
print(df.columns)


# Create a pivot table to analyze click trends by gender
pivot_table = df.pivot_table(index='Gender', columns='AD clicks', aggfunc='size', fill_value=0)

# Print the pivot table
print("Pivot table for click trends by gender:")
print(pivot_table)

# Calculate total users for each gender
total_users_by_gender = pivot_table.sum(axis=1)

# Calculate click rates
pivot_table['Click Rate'] = pivot_table['Clicked'] / total_users_by_gender

# Print click rates
print("Click rates by gender:")
print(pivot_table['Click Rate'])

# Plot the pivot table as a stacked bar chart
pivot_table.plot(kind='bar', color=['indigo', 'blue','green'], alpha=0.7)
plt.title('Click Trends by Gender')
plt.xlabel('Gender')
plt.ylabel('Click Counts')
plt.xticks(rotation=0)  # Rotate x-axis labels
plt.legend(['Clicked','Not Used', 'Used'], loc='upper right')  #  legend


# Put values on bars
for container in plt.gca().containers:
    plt.gca().bar_label(container, fmt='%d')
plt.show()









