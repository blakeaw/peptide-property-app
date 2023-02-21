import streamlit as st
import numpy as np
import peptides

col1, col2, col3 = st.columns(3)
with col2:
    st.title("Peptides App")
    st.image('https://upload.wikimedia.org/wikipedia/commons/c/c9/Peptide-Figure-Revised.png', width=200)
st.text(
    "A simple app to predict peptide properties using the peptides.py package."
)
st.markdown("------")

# with st.sidebar:
#     st.subheader("Amino acid sequence")
st.subheader("Input")
sequence = st.text_input("Input the amino acid sequence:", placeholder='YGGFLRRIRPKLK')

st.markdown("------")
st.subheader("Properties")
charge = None
molec_weight = None
hydro = None
ppi_index = None

if sequence != '':
    
    pep = peptides.Peptide(sequence)
    # Propeties of interest
    charge = int(np.round(pep.charge(pH=7.4), 0))
    molec_weight = np.round(pep.molecular_weight() / 1000, 3)
    hydro = np.round(pep.hydrophobicity(), 3)
    ppi_index = np.round(pep.boman(), 3)

st.write("Theoretical Net Charge (pH=7.4): ", charge)
st.write("Molecular Weight (kDa): ", molec_weight)
st.write("Hydrophobicity: ", hydro)
st.write("PPI-Index (Boman index): ", ppi_index)




