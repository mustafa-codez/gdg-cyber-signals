# Lab 04: Molecular Docking (Intro)

**Track:** Helix | **Level:** Intermediate | **Time:** ~2 hours

## What is it?
**Molecular docking** is a computer simulation that predicts how a small molecule (**ligand**) fits into a protein's binding site (the **receptor**) and estimates how strongly it binds, as a **docking score** (more negative kcal/mol is generally better predicted binding). It is used in early drug discovery to narrow thousands of candidates before lab testing.

Key terms:
- **PDB file:** 3D structure of a protein from the Protein Data Bank (https://www.rcsb.org)
- **PDBQT:** the format AutoDock tools need (adds charges and atom types)
- **Binding site / grid box:** the 3D region the software searches
- **Pose:** one predicted orientation of the ligand

**Limits:** Docking scores are rough estimates. They guide experiments but never replace them.

## Setup
This lab uses a classic, well-documented teaching example. Always check each tool's `--help` as flags can change between versions.
```bash
# Option A: conda (recommended for reproducibility)
conda create -n docking python=3.10 -y
conda activate docking
pip install vina meeko rdkit biopython
conda install -c conda-forge openbabel -y
```
Tools: AutoDock Vina (https://vina.scripps.edu), Meeko (ligand prep), Open Babel (format conversion), PyMOL or UCSF ChimeraX (visualisation).

## Walkthrough (outline with real commands)

### Step 1: Get a protein structure
```bash
wget https://files.rcsb.org/download/1HSG.pdb
```
`1HSG` is a widely used teaching structure (HIV-1 protease with a bound inhibitor), good for learning because the answer is known.

### Step 2: Prepare the receptor
Remove water and the original ligand, add hydrogens, convert to PDBQT. A simple route with Open Babel:
```bash
grep -v HOH 1HSG.pdb | grep -v MK1 > receptor_clean.pdb
obabel receptor_clean.pdb -O receptor.pdbqt -xr --partialcharge gasteiger -h
```

### Step 3: Prepare a ligand
```bash
# write a SMILES string for a small molecule into ligand.smi, e.g. aspirin: CC(=O)OC1=CC=CC=C1C(=O)O
obabel ligand.smi -O ligand.pdbqt --gen3d -h --partialcharge gasteiger
```

### Step 4: Define the search box
Choose the centre from the position of the original ligand (view it in PyMOL/ChimeraX) and a box size around 20 to 25 Å. Write `config.txt`:
```
receptor = receptor.pdbqt
ligand = ligand.pdbqt
center_x = 0.0      # replace with your binding-site centre
center_y = 0.0
center_z = 0.0
size_x = 22
size_y = 22
size_z = 22
exhaustiveness = 8
out = docked.pdbqt
```

### Step 5: Run
```bash
vina --config config.txt
```
Output: a table of poses with affinities in kcal/mol.

### Step 6: Validate and compare
- **Redocking test:** dock the *original* ligand and check that your pose is close to the crystal pose (RMSD below ~2 Å is the usual success criterion).
- Compare several ligands, and include a **negative control** (a molecule that shouldn't bind).
- Always record software versions, box coordinates and random seed so someone else can reproduce your result.

## Why this is in a security repo
Reproducibility and integrity matter in science as in security: **pinned versions, checksums, recorded parameters, and shared data**. A tampered receptor file or tool would silently poison results (supply-chain risk, Lab 03).

## Exercises
1. Complete a redocking run and report the RMSD.
2. Dock two different ligands and write which you'd prioritise, with reasons and caveats.
3. Write a reproducibility checklist for your docking run (versions, checksums, parameters).

## Checkpoint
- What does a docking score tell you, and what doesn't it tell you?
- Why run a redocking and a negative control?

## Go deeper
- AutoDock Vina docs: https://autodock-vina.readthedocs.io
- RCSB Protein Data Bank: https://www.rcsb.org
- UCSF ChimeraX: https://www.cgl.ucsf.edu/chimerax/
