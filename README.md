# PythonCourse

#PSEUDOCODE

#The script should read a file and calculate the average lifetime and standard deviation of a hydrogenbond contact.

1. Read file #list with file names for dynamical propagation of contacts which the program should calculate lifetime for.

2. While iterating over this list of filenames:

a. Open the file #each row in the file contains the number 1 (the contact is present at that frame number) or 0 (the contact is not present at that frame number)
b. Save the rows in an array #contactPropagation
c. Iterate over that array to generate a list of lifetimes

c.i. 
If the array[i]=1 -> lifetime+=1 #update a variable called lifetime
Else if array[i]=0 and lifetime ≥ 1 -> append lifetime to the array LifetimeList
Else -> continue #continue to iterate over the array

c.ii. 
From the list LifetimeList calculate average lifetime for the contact, standard deviation and max and min lifetime

c.iii 
use a residue libary file to give the contact the correct name.

c.iv.
save the contact in a class called Lifetime

3. Foreach contact saved as an object in the class Lifetime; print the attributes.
