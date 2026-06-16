from rdkit import Chem
from rdkit.Chem import Descriptors, Lipinski

def analyze_molecule(smiles):
    if not smiles: smiles = "CC(=O)OC1=CC=CC=C1C(=O)O"
    mol = Chem.MolFromSmiles(smiles)
    if not mol: 
        return {"status": "Error", "message": "Invalid SMILES"}
    
    mw = Descriptors.MolWt(mol)
    logp = Descriptors.MolLogP(mol)
    is_safe = mw < 500 and logp < 5
    
    return {
        "status": "Success",
        "molecular_weight": round(mw, 2),
        "logp": round(logp, 2),
        "is_safe": is_safe
    }
