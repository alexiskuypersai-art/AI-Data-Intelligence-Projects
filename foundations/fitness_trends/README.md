# Foundational Project: Fitness Trends Analysis (2018-2023)
*Level: Beginner (Foundational)* | *Duration: 1 hour*

## Project Overview
This analysis explores global fitness industry shifts using Google Trends data. The goal was to identify market peaks and provide data-driven recommendations for business expansion.

## Project Tasks (DataCamp)
1. **Identify the year** with the highest global search interest for "workout".
2. **Compare keywords** to find the most popular fitness trend during the COVID-19 pandemic versus the current period.
3. **Analyze geographic data** to find the country with the highest interest among the US, Australia, and Japan.
4. **Evaluate expansion opportunities** by comparing search interest between the Philippines and Malaysia.

## Business Insights & Evidence
* **Market Peak:** **2020** was confirmed as the global peak for fitness interest, showing a massive spike compared to 2019 due to global lockdowns.
* **Consumer Shift:** Data highlights a clear transition. Using the `.mean().idxmax()` method, we observe that **"home workout"** was the leading trend in 2020, while **"gym workout"** became the dominant category in 2023.
* **Target Region:** The **United States** shows the highest overall search interest among the developed markets analyzed (US, AU, JP).
* **Expansion Strategy:** Recommended the **Philippines** over Malaysia for a new market entry. 
    * *Evidence:* The Philippines shows a **significantly higher search volume** (approx. 20% higher) for home-fitness keywords compared to Malaysia.

## Technical Implementation
* **Language:** Python
* **Library:** Pandas
* **Methodology:** `.to_datetime()`, `.idxmax()`, `.isin()`, and `.mean()`.
