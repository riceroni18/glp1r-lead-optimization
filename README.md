# glp1r-lead-optimization
A structural bioinformatics pipeline utilizing Python and deep learning (Boltz-2) for GLP-1R receptor-ligand docking.

# GLP-1R Small Molecule Lead Optimization Pipeline
## Automated Variant Generation and Machine Learning Docking Framework

This repository contains an end-to-end computational biology workflow developed during the OMTX AI Hackathon (May 2026). The project automates the extraction of target sequences from raw structural biology data, executes combinatorial R-group variations on a target lead compound, and deploys candidates to deep-learning structural models to optimize small-molecule binding against the human GLP-1 Receptor.

---

## 🧬 Project Architecture & Engineering Workflow

The pipeline bridges raw structural biology data with machine learning-driven lead optimization through a three-tiered modular design:

1. **Structural Data Ingestion [`scripts/get_seq.py`](scripts/get_seq.py):** A custom Python parser designed to map and convert three-letter amino acid residues from target PDB files [`data/6XOX_GLP1R_chainR.pdb`](data6XOX_GLP1R_chainR.pdb) into a continuous single-letter FASTA sequence required by modern ML architectures.
2. **Combinatorial Ligand Library Generation [`scripts/generate_keys.py`](scripts/generate_keys.py):** An algorithmic string-manipulation utility that automates site-specific chemical modifications (including Fluorination and Chlorination) across a library of small-molecule candidates, systematically mutating a core Danuglipron scaffold using SMILES string slicing.
3. **Biophysical Evaluation:** Deployed generated candidates to cloud infrastructure to evaluate spatial binding and affinity using the state-of-the-art **Boltz-2** structural prediction model.

---

## 🛠️ Technical Challenges & Infrastructure Triage

* **Cloud Infrastructure Optimization:** Identified and resolved standard cloud preemption challenges (`GCP Batch VM Exit Code 50002`) during high-throughput execution. Successfully audited task sequences, refined input string formatting to eliminate illegal string headers, and managed job resubmissions through alternative cloud zones to guarantee completion.
* **Relative Path Management:** Refactored Python file I/O operations to utilize relative directory mapping (`data/`), ensuring pipeline portability across distinct local and cloud environments.

---

## 📊 Key Results & Metrics

* **Baseline Target Hit:** Achieved a successful structural docking alignment inside the active binding pocket of the GLP-1 receptor with a **34.8% affinity confidence score** on the initial baseline compound.
* **Structural Validation:** Visual inspection confirmed precise ligand positioning nestled within the receptor's alpha-helical transmembrane domain bundle.

### Binding Pocket Visualization
[GLP-1R Binding Pocket](<results/Screenshot 2026-05-10 201838.png>)

---

## 🚀 Future Directives
* Integrate `RDKit` to handle advanced chemical syntax validation and true structural molecular mutations.
* Automate binding affinity delta ($\Delta$) tracking across the full 11-candidate library to generate quantitative Structure-Activity Relationship (SAR) data models.
