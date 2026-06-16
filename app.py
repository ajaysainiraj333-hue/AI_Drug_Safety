import streamlit as st
from models import analyze_molecule
from processor import clean_data, save_to_log, generate_summary

def main():
    st.title("Professional AI Drug Safety System")
    
    # User input ke liye text_input ka use
    raw_input = st.text_input("Enter SMILES (ya seedha Enter dabao):")
    
    # Jab user input dega, tabhi code aage badhega
    if raw_input:
        smiles = clean_data(raw_input)
        
        # Analysis
        report = analyze_molecule(smiles)
        st.write(f"Report: {report}")
        
        # Saving log
        save_to_log(smiles, report)
        st.success("Result history.txt mein save ho gaya hai.")
        
        # Summary
        st.subheader("--- Current Research Summary ---")
        total, safe = generate_summary()
        st.write(f"Total Tests: {total} | Safe Molecules: {safe}")

if __name__ == "__main__":
    main()
