import pandas as pd
from datetime import datetime

# Read the input CSV file into a pandas DataFrame
df = pd.read_csv('rawDatasets/UKAndUS.csv', encoding='utf-8')

# Filter rows for 'Daily Mail' and 'New York Times' sources
uk_df = df[df['Publication'] == 'Daily Mail'].copy()  # Create a copy of the filtered DataFrame
us_df = df[df['Publication'] == 'New York Times'].copy()  # Create a copy of the filtered DataFrame

# Convert the 'Date' column to a datetime format and format it as 'YYYYMMDD' for the copied DataFrames
uk_df['publish_date'] = pd.to_datetime(uk_df['Date'], format='%Y%m%d').dt.strftime('%Y%m%d')
us_df['publish_date'] = pd.to_datetime(us_df['Date'], format='%Y%m%d').dt.strftime('%Y%m%d')

# Rename the 'Headline' column to 'headline_text'
uk_df.rename(columns={'Headline': 'headline_text'}, inplace=True)
us_df.rename(columns={'Headline': 'headline_text'}, inplace=True)

# Select the 'publish_date' and 'headline_text' columns
uk_df = uk_df[['publish_date', 'headline_text']]
us_df = us_df[['publish_date', 'headline_text']]

# Save the filtered DataFrames to CSV files
uk_df.to_csv('rawDatasets/UK.csv', encoding='utf-8', index=False)
us_df.to_csv('rawDatasets/US.csv', encoding='utf-8', index=False)

print("Filtering and splitting complete.")
