import pandas as pd

# Load the dataset
df = pd.read_csv("netflix_titles.csv")
#df = pd.read_csv("/Users/iuv/Documents/cppcrash/Elevate_Labs/netflix_titles.csv")
df.info()
df.head()
df.describe(include='all')

# Check null values
df.isnull().sum()

# Strategy:
# - Fill 'director' and 'cast' with placeholders
# - Drop rows with missing 'country' and 'date_added' as they are essential

df['director'] = df['director'].fillna('Unknown')
df['cast'] = df['cast'].fillna('Not Provided')
df = df.dropna(subset=['country', 'date_added'])

# Check for duplicates
duplicates = df.duplicated().sum()

# Drop duplicates if any
df = df.drop_duplicates()

# Normalize categorical values
df['type'] = df['type'].str.lower().str.strip()
df['country'] = df['country'].str.strip()

# Example replacements (for uniformity)
df['country'] = df['country'].replace({
    'United States': 'USA',
    'United Kingdom': 'UK'
})

# Convert 'date_added' to datetime format
df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')

# Optional: Fill any remaining NaT (if any)
df['date_added'] = df['date_added'].fillna(pd.Timestamp('2000-01-01'))

# Make headers lowercase and remove spaces
df.columns = df.columns.str.lower().str.strip().str.replace(' ', '_')

# Ensure 'release_year' is integer
df['release_year'] = df['release_year'].astype(int)

# Save the cleaned dataset
df.to_csv('netflix_cleaned.csv', index=False)
