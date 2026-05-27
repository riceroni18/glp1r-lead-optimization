# generate_keys.py
base_smiles = "CC1=C(C=C(C=C1)C2=CC(=NN2C)C3=CC=C(C=C3)CN4C5=C(C=C(C=C5)C(=O)O)N=C4C)C"
tweaks = ["(F)", "(Cl)", "(OC)", "(N)", "(C)"] 
candidates = [base_smiles]

for group in tweaks:
    candidates.append(group + base_smiles)
    candidates.append(base_smiles[:25] + group + base_smiles[25:])

print("\n--- COPY THESE STRINGS TO OMTX ---")
for i, smiles in enumerate(candidates):
    print(f"Candidate {i+1}: {smiles}")
print("----------------------------------\n")
