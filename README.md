# PythonCourse

In the file pseudocode is the pseudocode for the lifetime.py script

SCRIPT NAME: lifetime.py
DATA FILES: testfiles.zip
REQUIRED MODULES: the script lifetime.py uses the python 3 modules statistics and argparse

USES OF THE SCRIPT

The script lifetime.py calculates the lifetime for bridging water contacts between protein residues and dna residues (Protres-WAT-Dnares).

python3 lifetime.py bridge*.dat --dtime 10 --lib residuelibrary.txt --out lifetimetable.txt

python3 lifetime.py bridge*.dat -dt 10 -l residuelibrary.txt -o lifetimetable.txt

The script requires three files:
1. filenames.txt; a list of filenames of contacts which the script should calculate lifetimes for
2. residuelibrary.txt; list of residue names; column 1: residue number; column 2: correct residue name
3. bridge_x_y.dat; several contacts files that are listed in filenames.txt, where x is proteinresidue number and y is dna resiude number.

To test the script one can use the files in testfiles.zip
