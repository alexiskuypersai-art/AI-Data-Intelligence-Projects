"""
PROJECT: Fitness Trends Analysis
OBJECTIVE: Identify global workout peaks and expansion targets using Pandas.
CONCEPTS: Time-series analysis, Data filtering, Geospatial comparison.
"""

import pandas as pd

# --- 1. Global search peak for 'workout' ---
wo = pd.read_csv('data/workout.csv')
wo['month'] = pd.to_datetime(wo['month'])

valeur_max = wo['workout_worldwide'].idxmax()
resultat = wo.loc[valeur_max,:]
year_str = str(resultat['month'].year)
print(f"Year of peak interest: {year_str}") 

# --- 2. Popular keywords: COVID vs Current ---
keywords = pd.read_csv('data/three_keywords.csv')
keywords['month'] = pd.to_datetime(keywords['month']).dt.year

categories = ['home_workout_worldwide', 'gym_workout_worldwide', 'home_gym_worldwide']

# Current (2023)
actual_year = keywords[keywords['month'] == 2023]
current = actual_year[categories].mean().idxmax()

# Covid (2020)
covid_year = keywords[keywords['month'] == 2020]
peak_covid = covid_year[categories].mean().idxmax()

print(f"Peak Covid: {peak_covid}")
print(f"Current trend: {current}")

# --- 3. Highest interest country (US, Australia, or Japan) ---
geo = pd.read_csv('data/workout_geo.csv')
pays_target = ['Australia', 'Japan', 'United States']
three_country = geo[geo['country'].isin(pays_target)]
best_country_idx = three_country['workout_2018_2023'].idxmax()
top_country = three_country.loc[best_country_idx, 'country']

print(f"Top country: {top_country}")

# --- 4. Expansion recommendation (Philippines vs Malaysia) ---
df = pd.read_csv('data/three_keywords_geo.csv')
df_clean = df.dropna()

selection_pays = ['Malaysia', 'Philippines']
top_index = df_clean[df_clean['Country'].isin(selection_pays)]['home_workout_2018_2023'].idxmax()
home_workout_geo = df_clean.loc[top_index, 'Country']

print(f"Expansion target: {home_workout_geo}")
