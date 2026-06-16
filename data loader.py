import os

def load_drug_data(filepath):
    # Check karenge ki kya file exist karti hai
    if os.path.exists(filepath):
        with open(filepath, 'r') as file:
            content = file.read()
            return f"Data successfully read! Content length: {len(content)} characters."
    else:
        return "Error: File nahi mili. Ek text file banao."
