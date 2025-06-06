import json
import os

DB_FILE = "labs.json"

def load_data():
    if not os.path.exists(DB_FILE):
        return []
    with open(DB_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_data(data):
    with open(DB_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def add_lab(name, number, grade, status):
    data = load_data()
    data.append({
        "name": name,
        "number": number,
        "grade": grade,
        "status": status
    })
    save_data(data)

def list_labs(filter_status=None):
    data = load_data()
    if filter_status:
        data = [lab for lab in data if lab["status"].lower() == filter_status.lower()]
    return data
