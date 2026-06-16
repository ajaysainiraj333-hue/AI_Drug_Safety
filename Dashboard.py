import streamlit as st
import matplotlib.pyplot as plt
from models import analyze_molecule
from processor import generate_summary, save_to_log

st.title("AI Drug Safety Dashboard")

smiles = st.text_input("Enter Molecule SMILES:", "CC(=O)OC1=CC=CC=C1C(=O)O")

if st.button("Analyze"):
    report = analyze_molecule(smiles)
    st.write(report)
    save_to_log(smiles, str(report))
    
    total, safe = generate_summary()
    st.write(f"Total Tests: {total} | Safe Molecules: {safe}")
    
    # Visualization
    fig, ax = plt.subplots()
    ax.pie([safe, total-safe], labels=['Safe', 'Unsafe'], autopct='%1.1f%%', colors=['#4CAF50', '#F44336'])
    st.pyplot(fig)
