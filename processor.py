import datetime
import os

def clean_data(raw_text):
    return raw_text.strip()

def save_to_log(molecule, result):
    with open("history.txt", "a") as f:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"[{timestamp}] Mol: {molecule} | Result: {result}\n")

def generate_summary():
    if not os.path.exists("history.txt"):
        return 0, 0
    with open("history.txt", "r") as f:
        lines = f.readlines()
        safe_count = sum(1 for line in lines if "'is_safe': True" in line)
        total_count = len(lines)
        return total_count, safe_count
