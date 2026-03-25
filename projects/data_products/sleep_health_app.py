import pandas as pd 

# Load the dataset
sleep = pd.read_csv('sleep_health_data.csv')
pd.set_option('display.max_columns', None)

# --- DATA CLEANING ---

# 1. Normalize column names 
sleep.columns = [col.lower().replace(' ', '_') for col in sleep.columns]
sleep = sleep.rename(columns = {'person_id' : 'id'})

# 2. Handle missing values 
sleep['sleep_disorder'] = sleep['sleep_disorder'].fillna('None')

# 3. Feature Engineering: Split 'blood_pressure' into 'systole' and 'diastole'
# Converting string "120/80" into two separate numeric columns
sleep['systole'] = sleep['blood_pressure'].str.split('/').str[0].astype(int)
sleep['diastole'] = sleep['blood_pressure'].str.split('/').str[1].astype(int)

# 4. Drop the original column
sleep = sleep.drop(columns = ['blood_pressure'])

# --- DATA VERIFICATION ---
print(sleep.head())
print(sleep.info())
print(sleep.describe())
print(sleep.shape)
