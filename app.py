import streamlit as st
from rdkit import Chem
from rdkit.Chem import Draw
from models import analyze_molecule
from processor import clean_data, save_to_log, generate_summary
from PIL import Image
import io

# Professional UI setup
st.set_page_config(page_title="AI Drug Safety System", layout="wide")

def main():
    st.title("🧪 Professional AI Drug Safety System")
    st.markdown("---")

    with st.sidebar:
        st.header("🕒 Recent Research")
        total, safe = generate_summary()
        st.metric("Total Tests", total)
        st.metric("Safe Molecules", safe)

    raw_input = st.text_input("Enter SMILES code:", placeholder="e.g., CC(=O)OC1=CC=CC=C1C(=O)O")

    if raw_input:
        smiles = clean_data(raw_input)
        
        try:
            mol = Chem.MolFromSmiles(smiles)
            if mol:
                col1, col2 = st.columns([1, 2])
                
                with col1:
                    st.subheader("Structure")
                    # Using PIL (Pillow) instead of Cairo
                    img = Draw.MolToImage(mol, size=(300, 300))
                    st.image(img, use_column_width=True)
                
                with col2:
                    report = analyze_molecule(smiles)
                    st.subheader("Safety Report")
                    is_safe = report.get('is_safe', False)
                    if is_safe:
                        st.success("STATUS: SAFE")
                    else:
                        st.error("STATUS: DANGER")
                    
                    st.metric("Molecular Weight", report.get('molecular_weight', 'N/A'))
                    st.metric("LogP", report.get('logp', 'N/A'))
                    
                    save_to_log(smiles, report)
            else:
                st.error("Invalid SMILES structure.")
        except Exception as e:
            st.error(f"Error: {e}")

if __name__ == "__main__":
    main()
