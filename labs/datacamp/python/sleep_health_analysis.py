"""
SLEEP HEALTH ANALYSIS - DATACAMP PROJECT

OBJECTIVE:
Analyze sleep patterns across different occupations and BMI categories.

TASKS SUMMARY:
- Identify occupation with the lowest average sleep duration (lowest_sleep_occ).
- Identify occupation with the lowest average sleep quality (lowest_sleep_quality_occ).
- Compare both metrics to check for consistency (same_occ).
- Calculate insomnia ratios per BMI category (bmi_insomnia_ratios).

REQUIREMENTS:
- pandas: for data manipulation and pivot tables.
- sleep_health_data.csv: source dataset containing health and lifestyle metrics.
"""

import pandas as pd
df = pd.read_csv('sleep_health_data.csv')

# --- TASK 1: Lowest Average Sleep Duration ---
# Group by Occupation and get the median/average duration
sleep_duration_series = df.groupby('Occupation')['Sleep Duration'].median()
lowest_sleep_occ = sleep_duration_series.idxmin()

# --- TASK 2 & 3: Lowest Quality & Comparison ---
# Group by Occupation for multiple metrics
sleep_stats = df.groupby('Occupation')[['Quality of Sleep', 'Sleep Duration']].median()

lowest_sleep_quality_occ = sleep_stats['Quality of Sleep'].idxmin()
lowest_sleep_duration_occ = sleep_stats['Sleep Duration'].idxmin()

# Boolean check: Is it the same occupation for both lows?
same_occ = lowest_sleep_quality_occ == lowest_sleep_duration_occ

# --- TASK 4: BMI Insomnia Ratios ---
# Create binary flag for Insomnia
df['is_insomnia'] = (df['Sleep Disorder'] == 'Insomnia').astype(int)

# Pivot table to calculate the ratio per BMI category
bmi_pivot = df.pivot_table(values='is_insomnia', index='BMI Category').round(2)

# Manually build the dictionary as requested by the challenge
bmi_insomnia_ratios = {
    "Normal": float(bmi_pivot.loc['Normal', 'is_insomnia']),
    "Overweight": float(bmi_pivot.loc['Overweight', 'is_insomnia']),
    "Obese": float(bmi_pivot.loc['Obese', 'is_insomnia'])
}

# --- OUTPUTS (For verification) ---
if __name__ == "__main__":
    print(f"Lowest Sleep Duration Occupation: {lowest_sleep_occ}")
    print(f"Lowest Sleep Quality Occupation:  {lowest_sleep_quality_occ}")
    print(f"Are they the same? {same_occ}")
    print(f"BMI Insomnia Ratios: {bmi_insomnia_ratios}")
