# Web Scraping with Python

This repository contains Python scripts for extracting structured data from websites and saving it in JSON format inside the export/ folder.

✅ Automates web data collection  
✅ Uses requests for fetching web pages  
✅ Uses BeautifulSoup for parsing and extracting information  
✅ Saves data in JSON format for easy access  

## 🛠️ Setup Guide

### 1️⃣ Install Python
Ensure you have **Python 3.7+** installed. You can check your version with:
```sh
python --version
```

### 2️⃣ Clone This Repository
```sh
git clone https://github.com/YOUR-USERNAME/web-scraping-with-python.git
cd web-scraping-with-python
```

### 3️⃣ Create a Virtual Environment (Recommended)
Avoid dependency conflicts by using a **virtual environment**:
```sh
python -m venv venv
```

Activate it:
- **Windows (PowerShell)**:  
  ```sh
  venv\Scripts\Activate
  ```
- **Mac/Linux**:  
  ```sh
  source venv/bin/activate
  ```

### 4️⃣ Install Required Libraries
Inside the **activated virtual environment**, install dependencies:
```sh
pip install -r requirements.txt
```

## 🚀 Running a Scraper

To run a specific scraper (e.g., **Wikipedia birds list**):
```sh
python wiki_get_austrian_birds.py
```

---

## 📜 Available Python Scripts

### 🦜 `wiki_get_austrian_birds.py`

This script scrapes bird species data from **[Wikipedia’s List of Birds of Austria](https://de.wikipedia.org/wiki/Liste_der_V%C3%B6gel_%C3%96sterreichs)**.  
It extracts **order, family, common names, scientific names, and status** of birds found in Austria and saves the data as a **JSON file** inside the `export/` folder.

✅ **Technologies Used:** `requests`, `BeautifulSoup`, `json`, `re`  
✅ **Output:** `export/birds-of-austria.json`

To run the script:
```sh
python wiki_get_austrian_birds.py
```

---