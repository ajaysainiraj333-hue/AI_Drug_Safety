import streamlit as st
from rdkit import Chem
from models import analyze_molecule
from processor import clean_data, save_to_log, generate_summary

st.set_page_config(page_title="AI Drug Safety System", layout="wide")

def main():
    st.title("🧪 Professional AI Drug Safety System")
    st.markdown("---")

    with st.sidebar:
        st.header("🕒 Recent Research")
        total, safe = generate_summary()
        st.metric("Total Tests", total)
        st.metric("Safe Molecules", safe)

    raw_input = st.text_input("Enter SMILES code:")

    if raw_input:
        smiles = clean_data(raw_input)
        report = analyze_molecule(smiles)
        
        st.subheader("Safety Report")
        is_safe = report.get('is_safe', False)
        if is_safe:
            st.success("STATUS: SAFE")
        else:
            st.error("STATUS: DANGER")
        
        st.write(f"Molecular Weight: {report.get('molecular_weight', 'N/A')}")
        st.write(f"LogP: {report.get('logp', 'N/A')}")
        save_to_log(smiles, report)

if __name__ == "__main__":
    main()
