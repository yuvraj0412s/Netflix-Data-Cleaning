import pandas as pd

df = pd.read_csv("netflix_titles.csv")
#df = pd.read_csv("/Users/iuv/Documents/cppcrash/Elevate_Labs/netflix_titles.csv")
df.info()
df.head()
df.describe(include='all')

df.isnull().sum()

df['director'] = df['director'].fillna('Unknown')
df['cast'] = df['cast'].fillna('Not Provided')
df = df.dropna(subset=['country', 'date_added'])

duplicates = df.duplicated().sum()

df = df.drop_duplicates()

df['type'] = df['type'].str.lower().str.strip()
df['country'] = df['country'].str.strip()

df['country'] = df['country'].replace({
    'United States': 'USA',
    'United Kingdom': 'UK'
})

df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')

df['date_added'] = df['date_added'].fillna(pd.Timestamp('2000-01-01'))

df.columns = df.columns.str.lower().str.strip().str.replace(' ', '_')

df['release_year'] = df['release_year'].astype(int)

df.to_csv('netflix_cleaned.csv', index=False)
