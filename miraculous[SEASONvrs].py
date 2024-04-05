import csv
import os
import time
import re
from colorama import Fore, Back, Style

# Adjust these paths according to your environment
csv_path = './episode_list.csv'
directory_path = './episodes/'

# intro
os.system('cls' if os.name == 'nt' else 'clear')
print(f"\n")
print(f"{Fore.CYAN}▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀ ")
print(f"{Fore.CYAN}▀▄▀▄▀▄▀▄▀▄ {Fore.CYAN} welcome to my  {Fore.CYAN}▄▀▄▀▄▀▄▀▄▀ ")
print(f"{Fore.CYAN}▀▄▀▄				 ▄▀▄▀{Style.RESET_ALL}")
print(f"{Fore.CYAN}▀▄▀▄ {Fore.YELLOW}♥ {Fore.RED}Miraculous {Fore.YELLOW}file {Fore.MAGENTA}renamer{Fore.YELLOW} ♥{Fore.CYAN} ▄▀▄▀{Style.RESET_ALL}")
print(f"{Fore.CYAN}▀▄▀▄				 ▄▀▄▀{Style.RESET_ALL}")
print(f"{Fore.CYAN}▀▄▀▄				 ▄▀▄▀{Style.RESET_ALL}")
print(f"{Fore.CYAN}▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀ {Style.RESET_ALL}")
# print(f"{Fore.CYAN}▀▄▀▄{Fore.CYAN}			by {Fore.YELLOW}elt0n {Fore.CYAN}▄▀▄▀{Style.RESET_ALL}")
print(f"\n")
# ◌♠♣♥☼☺☻

# Prompt the user for the season number
print(f"{Fore.CYAN}for wich season do you wanna rename files?{Style.RESET_ALL}")
season_number = input("enter season number [available: 2 - 3]\n").strip()

# prompt for viweing order
print(f"{Fore.CYAN} wich viewing order do you want to use?{Style.RESET_ALL}")
print(f"{Fore.CYAN}• {Fore.MAGENTA}1 {Fore.CYAN}: production order (recommanded by Thomas Astruc){Style.RESET_ALL}")
print(f"{Fore.CYAN}• {Fore.MAGENTA}2 {Fore.CYAN}: TF1 diffusion order{Style.RESET_ALL}")
print(f"{Fore.CYAN}• {Fore.MAGENTA}3 {Fore.CYAN}: Disney Channel diffusion order{Style.RESET_ALL}")
print(f"{Fore.CYAN}• {Fore.MAGENTA}4 {Fore.CYAN}: Netflix order{Style.RESET_ALL}")
print(f"{Fore.CYAN}• {Fore.MAGENTA}5 {Fore.CYAN}: Disney+ order{Style.RESET_ALL}")
print(f"{Fore.CYAN}")
viewing_order = input("enter answer [e.g., 1]\n").strip()
if viewing_order == "1":
	print(f"{Fore.CYAN}using production order. (perfect choice){Style.RESET_ALL}")
else:
	print(f"{Fore.CYAN}fuck you. using production order instead.{Style.RESET_ALL}")
print(f"{Fore.CYAN}starting renaming...")
time.sleep(1)


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
pattern = fr'Miraculous, les aventures de Ladybug et Chat Noir S0{season_number}E\d+ - (.+)\.mkv'

# Step 2: Loop through the files in the directory
for filename in os.listdir(directory_path):
	if filename.endswith(".mkv"):
		# Use regex to extract the episode title from the filename
		match = re.search(pattern, filename)
		if match:
			title = match.group(1).strip()
			print(f"match found! title: {title}")

			print(f"Use the mapping to find the corresponding production code")
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
