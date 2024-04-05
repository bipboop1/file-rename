import csv
import os
import time
import re

# Adjust these paths according to your environment
csv_path = './episode_list.csv'
directory_path = './episodes/'

# Prompt the user for the season number
season_number = input("for wich season do you wanna rename files? enter season number [e.g., 2 for Season 2]").strip()

# Step 1: Create a mapping from episode titles to production codes
title_to_code = {}
with open(csv_path, newline='', encoding='utf-8') as csvfile:
	reader = csv.DictReader(csvfile)
	for row in reader:
		title = row['Titre français'].strip()
		code = row['Code de production'].strip()
		if code.startswith(season_number):
			title_to_code[title] = code

# Define a regex pattern to extract the title from filenames, while maintaining the season number
pattern = r'Miraculous, les aventures de Ladybug et Chat Noir S0{season_number}E\d+ - (.+)\.mkv'

# Step 2: Loop through the files in the directory
for filename in os.listdir(directory_path):
    if filename.endswith(".mkv"):
        # Use regex to extract the episode title from the filename
        match = re.search(pattern, filename)
        if match:
            title = match.group(1).strip()

            # Step 3: Use the mapping to find the corresponding production code
            if title in title_to_code:
                full_code = title_to_code[title]
                # Truncate the first digit from the production code
                if len(full_code) == 3:
                    new_code = full_code[1:]
                else:
                    new_code = full_code

                new_episode_number = f'S0{season_number}E{new_code}'
                new_filename = f"Miraculous, les aventures de Ladybug et Chat Noir {new_episode_number} - {title}.mkv"

                # Step 4 and 5: Generate the new filename and rename the file
                old_file_path = os.path.join(directory_path, filename)
                new_file_path = os.path.join(directory_path, new_filename)
                os.rename(old_file_path, new_file_path)
                print(f'Renamed "{filename}" to "{new_filename}"')
                time.sleep(0.3)

print("Renaming complete.")
