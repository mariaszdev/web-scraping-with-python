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
current_order = ""   # Latin name of the order
current_orderDE = ""  # German name of the order
current_family = ""  # Latin name of the family
current_familyDE = ""  # German name of the family

# Loop through all elements (h2, h3, tables) to track hierarchy
for element in soup.find_all(["h2", "h3", "table"]):
    if element.name == "h2":  # If it's an h2 (Order)
        order_link = element.find("a")
        current_order = order_link.text.strip() if order_link else ""

        # Extract the full h2 text and split at " – " to get the German name
        full_text = element.text.strip()
        split_text = full_text.split(" – ")
        current_orderDE = split_text[1].strip() if len(split_text) > 1 else ""

    elif element.name == "h3":  # If it's an h3 (Family)
        family_link = element.find("a")
        current_family = family_link.text.strip() if family_link else ""

        # Extract the full h3 text and split at " – " to get the German name
        full_text = element.text.strip()
        split_text = full_text.split(" – ")
        current_familyDE = split_text[1].strip() if len(split_text) > 1 else ""

    elif element.name == "table" and "wikitable" in element.get("class", []):
        # Process each table
        rows = element.find_all("tr")[1:]  # Skip header row

        for row in rows:
            columns = row.find_all("td")
            if len(columns) >= 3:
                # ✅ Extract only the text inside the <a> element (ignoring "Hörprobe")
                common_name_element = columns[1].find("a")
                common_name = common_name_element.text.strip() if common_name_element else ""

                # ✅ Extract and clean the scientific name
                full_scientific_name = columns[2].text.strip().split("\n")[
                    0]  # Original name
                # Remove parentheses and content inside
                scientific_name = re.sub(
                    r"\(.*?\)", "", full_scientific_name).strip()

                # ✅ Extract status (handling missing values)
                status = columns[4].text.strip() if len(columns) > 4 else ""

                # ✅ Add data to list, including order and family
                bird_list.append({
                    "order": current_order,
                    "orderDE": current_orderDE,
                    "family": current_family,
                    "familyDE": current_familyDE,
                    "commonName": common_name,
                    "scientificName": scientific_name,
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
