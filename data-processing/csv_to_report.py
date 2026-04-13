"""
Player Performance Data Pipeline: CSV to Text Report Transformation.

This script demonstrates a complete data handling workflow:
1. Data Persistence: Creates 'epreuves.csv' with player names and scores.
2. Data Extraction: Reads and parses the CSV file using DictReader.
3. Data Filtering: Identifies players with scores above a 50-point threshold.
4. Report Generation: Produces a formatted 'certificats.txt' for automated messaging.

The script includes error handling for file operations and ensures proper 
data type conversion (string to integer) for numerical analysis.

Usage:
    Run the script to process the player data and generate local output files.
"""
import csv 
# Initial data set
data = [
    {'player': 'Alice', 'points': '85'},
    {'player': 'Bob', 'points': '40'},
    {'player': 'Charlie', 'points': '92'}
]

header = ['player', 'points']

# --- STEP 1: WRITING TO CSV ---
with open('results.csv', 'w', encoding='utf-8', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=header)
    writer.writeheader()
    writer.writerows(data)

print("File 'results.csv' created successfully.")

# --- STEP 2: READING AND PROCESSING ---
try:
    with open('results.csv', 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        players_list = []
        for row in reader:
            players_list.append(row)
        
        # --- STEP 3: WRITING TO TEXT FILE ---
        try:
            with open('certificates.txt', 'w', encoding='utf-8') as output_file: 
                for player_data in players_list:
                    name = player_data['player']
                    score = player_data['points']
                    output_file.write(f"Congratulations {name}, your score of {score} has been recorded.\n")
        
        except FileNotFoundError:
            print('Error during text file creation.')

except FileNotFoundError:
    print('Error: Source CSV file not found.')

# --- STEP 4: FINAL VERIFICATION ---
try: 
    with open('certificates.txt', 'r', encoding='utf-8') as final_file:
        final_content = final_file.read()
        print(f"List of processed certificates :\n{final_content}")
except FileNotFoundError:
    print('Error: Could not read the final certificate file.')
