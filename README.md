# PythonCourse

In the file pseudocode is the pseudocode for the lifetime.py script

**SCRIPT NAME:** lifetime.py

**DATA FILES:** testfiles.zip

**REQUIRED MODULES:** the script lifetime.py uses the python 3 modules *statistics* and *argparse*

**USES OF THE SCRIPT**

The script **lifetime.py** calculates the lifetime for bridging water contacts between protein residues and dna residues (Protres-WAT-Dnares).
The script reads contact files of the type *bridge_x_y.dat* (x=proteinres number; y=dna nucleotide number), where the rows in the files corresponds to frame number, and each fame has either the number 1 (contact is present) or 0 (contact is not present).

**To run the script use for example one of:**

python3 lifetime.py bridge*.dat --dtime 10 --lib residuelibrary.txt --out lifetimetable.txt

python3 lifetime.py bridge*.dat -dt 10 -l residuelibrary.txt -o lifetimetable.txt

**Required inputs:**<br/>
bridge*.dat: specifies that the script should read all files that start with bridge and ends with the prefix .dat

**Optional inputs:**<br/>
*--dtime:* converts frame number into time in ps. Default value is 1. If dt=10, then the timeinterval between each frame is 10 ps.


*--lib:* takes a residuelibrary file that will be used to give the contacts correct names of the type Protres-WAT-Dnares. The file is composed of two columns: col1=residue number (x or y in bridge_x_y.dat) and col2=correct residue name. If this file is not included the contacts mantain the filename as name.


*--out:* allows one to chose the name of the output.

**The script provides a table:**<br/>
*Contactname* (name of the contact)

*Occupancy %* (the fraction of the trajectory where the contact is present)

*LifetimeMean* (average lifetime in ps)

*stdev* (standard deviation of the lifetime)

*MinVal* (min lifetime) 

*MaxVal* (max lifetime)


To test the script one can **unzip** use the files stored in **testfiles.zip** (includes bridge_x_y.dat files and residuelibary.txt).
