from models import analyze_molecule
from processor import clean_data, save_to_log, generate_summary

def main():
    print("--- Professional AI Drug Safety System ---")
    raw_input = input("Enter SMILES (ya seedha Enter dabao): ")
    smiles = clean_data(raw_input)
    
    # Analysis
    report = analyze_molecule(smiles)
    print(f"Report: {report}")
    
    # Saving log
    save_to_log(smiles, report)
    print("Result history.txt mein save ho gaya hai.")
    
    # Summary (Ab ye main function ke andar hai)
    print("\n--- Current Research Summary ---")
    total, safe = generate_summary()
    print(f"Total Tests: {total} | Safe Molecules: {safe}")

if __name__ == "__main__":
    main()
