import requests
from bs4 import BeautifulSoup
import json
import re  # Import regex module
import os  # Import os for folder management

# Wikipedia URL with the bird list
url = "https://de.wikipedia.org/wiki/Liste_der_V%C3%B6gel_%C3%96sterreichs"

# Fetch HTML content
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Find all tables on the page
tables = soup.find_all("table", {"class": "wikitable"})

bird_list = []

# Loop through each table
for table in tables:
    rows = table.find_all("tr")[1:]  # Skip the first row (header)

    for row in rows:
        columns = row.find_all("td")
        if len(columns) >= 3:
            common_name = columns[1].text.strip()
            full_scientific_name = columns[2].text.strip().split("\n")[
                0]  # Original name

            # Remove everything inside parentheses, including the parentheses themselves
            scientific_name = re.sub(
                r"\(.*?\)", "", full_scientific_name).strip()

            status = columns[4].text.strip() if len(columns) > 4 else "Unknown"

            bird_list.append({
                "commonName": common_name,
                "scientificName": scientific_name,  # canonical name
                "status": status
            })

# ✅ Ensure the 'export' folder exists
export_folder = "export"
os.makedirs(export_folder, exist_ok=True)

# ✅ Save JSON file inside 'export' folder
json_file_path = os.path.join(export_folder, "birds-of-austria.json")
with open(json_file_path, "w", encoding="utf-8") as file:
    json.dump(bird_list, file, ensure_ascii=False, indent=4)

print(
    f"✅ The bird list has been successfully extracted and saved as '{json_file_path}'!")
