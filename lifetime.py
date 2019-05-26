#!/usr/bin/env python3
#Title: Lifetime of bridging water contacts (Protres-WAT-DNAres)
#Author: Johanna Hörberg
#Course: Python programming applied to research (SC00032)
#Description: This python script calculates the lifetime of a bridging water contact between a protein residue and a dna residue.

"""––––––MODULES––––––"""

import statistics


"""––––––CLASSES––––––"""

class Lifetime:
	#A class that stores data about the lifetime and occupancy of a bridging water contact between a protein residue and a dna residue.
	#contactName: name of the contact "ProtRes-WAT-DNAres" (str)
	#occupancy: the fraction in percent/occurence of the contact during the trajectory. (int)
	#lifetimeMean: average lifetime in ps (int)
	#stdev: standard deviation of the lifetime (int)
	#minVal: lowest lifetime value in ps (int)
	#maxVal: highest lifetime value in ps (int)

	def __init__(self, contactName, occupancy, lifetimeMean, stdev, minVal, maxVal):
		#creates an object to the class with the attributes contactName, occupancy, liftimeMean, stdev, minVal, maxVal.
		self.contactName = contactName
		self.occupancy = occupancy
		self.lifetimeMean = lifetimeMean
		self.stdev = stdev
		self.minVal = minVal
		self.maxVal = maxVal

	def __repr__(self):
		#returns a string that describes the Lifetime object
		return self.contactName + "\t" + str(self.occupancy)+ "\t" +  str(self.lifetimeMean) + "\t" + str(self.stdev) + "\t" + str(self.minVal) + "\t" + str(self.maxVal) + "\n"



class Contacts:
	#A class that stores all bridging water contacts from a file. 

	def __init__(self):
		#when an object for this class is created, an emty list is generated that will store all Lifetime objects.
		self.bridgingcontacts = []


	def NewLifetimeObject(self):
		#method for creating objects to the class Lifetime for bridning water contacts read from a text file.
		residueLibrary = importResidueNames() #imports the residueLibrary containing the correct residue names
		file = open("filenames.txt","r") #opens the file filenames.txt, where each row contains the filename (bridge_x_y.dat) for a bridging water contact
		filename = file.readline().strip() #store the filename in a variable
		while filename !="":
			contactName = changeName(filename, residueLibrary) #creates the name of the bridging water contact
			contactPropagation = openFile(filename) #opens the contactfile and stores its content in a list
			occupancy = calcOccupancy(contactPropagation) #calculates the occupancy of the contact
			lifetimes = calcLifetime(contactPropagation) #calculates the lifetimes for the contact
			lifetimeMean = int(statistics.mean(lifetimes)) #calculates the average lifetime
			stdev = int(statistics.stdev(lifetimes)) #calculates the std
			minVal = int(min(lifetimes)) #extract the lowest lifetime
			maxVal = int(max(lifetimes)) #extract the highest lifetime
			newObject = Lifetime(contactName, occupancy, lifetimeMean, stdev, minVal, maxVal) #creates a Lifetime object for the contact
			self.bridgingcontacts.append(newObject) #append the contact in the list self.bridgingcontacts
			filename = file.readline().strip() #read a new filename from the file filenames.txt
		file.close()

	def PrintLifetime(self):
		#creats a file allLifetimes and prints for each bridging contacts the Lifetimeattributes (prints the string from __repr__(self) in a table
		lifetimeFile = open('allLifetimes.txt', 'w')
		lifetimeFile.write("Bridgingcontact\t occupancy(%)\t Lifetime (average, ps) \tstdev\tMIN\tMAX\n")
		for contact in self.bridgingcontacts:
			lifetimeFile.write(str(contact))
		lifetimeFile.close()


"""––––––FUNCTIONS––––––"""

def openFile(filename):
	#Opens a contact file (bridge_x_y.dat) and append each row to a list
	#input: name of the file to be open (filename)
	#output: returns a list where each element in the list contains the number 1 (contact is present) or 0 (contact is not present).
	file = open(filename, "r")
	list = []
	row = file.readline().strip()
	while row !="":
		list.append(row)
		row = file.readline().strip()
	file.close()
	return list

def importResidueNames():
	#opens a file residuelibrary.txt that contains names of the residues of the trajectory in column 1 and the real names in column 2
	#store the names in a list of a list.
	#input: none
	#output: returns the list of list residueNames 
	file = open("residuelibrary.txt", "r")
	residueNames = []
	for residue in file:
		residue = residue.split()
		residueNames.append(residue)
	return residueNames

def changeName(filename, residueLibrary):
	#creat the correct name for the bridging water contact.
	#input: filename (bridge_x_y.dat) and residueLibrary (names of the residues)
	#output: returns contactname of the type Protres-WAT-Dnares

	splitVariable = filename[7:-4].split("_") #stores the residue numbers x (protres) and y (dnares) in a list.

	#two for loops are used to change the name of the protein residue (x) and dna residue (y).
	for proteinres in residueLibrary:
		if proteinres[0] == splitVariable[0]:
			splitVariable[0] = proteinres[1]
			break
		else:
			continue
	for dnares in residueLibrary:
		if dnares[0] == splitVariable[1]:
			splitVariable[1] = dnares[1]
			break
		else:
			continue

	name = splitVariable[0] + "-WAT-" + splitVariable[1] #name of the contact
	return name


def calcOccupancy(list):
	#calculates the occupancy of a contact; that is the number of frames relative to the length of the trajectory in percent.
	#input: a list where each element in the list contains a number 1 (contact is present) or 0 (contact is not present)
	#output: returns the occupancy.

	#for loop interates over each element in the list and update the variable frames if the element is equal to 1.
	frames = 0
	for contact in list:
		contact = int(contact)
		if contact == 1:
			frames += 1
		else:
			continue
	fraction = int((frames/len(list))*100) #calculates the fraction (occupancy) in percent.
	return fraction

def calcLifetime(list):
	#calculates the lifetime for a contact
	#input: a list where each element in the list contains a number 1 (contact is present) or 0 (contact is not present)
	#output: returns a list of lifetimes for the contact
	lifetimeList = []
	lifetime = 0

	#a for loop iterates over each element in the list and updates a variable lifetime if the line is equal to 1
	#if the line is equal to 0 and the variable lifetime has a value > 1, the value is appended to the lifetime list
	#else it continues.
	for line in list:
		line = int(line)
		if line == 1:
			lifetime +=1
		elif line == 0 and lifetime >= 1:
			lifetime = lifetime*10 #values are in 10 ps so to get number in ps the parameter is multiplied by 10
			lifetimeList.append(lifetime)
			lifetime = 0
		else:
			continue
	return lifetimeList


def main():
	#main function that will initiate the script. Creates an object in the class Contacts.
	#call the methods NewLifetimeObject and PrintLifetime to print the lifetimes of the contacts to a textfile.
	bridgingcontacts = Contacts()
	bridgingcontacts.NewLifetimeObject()
	bridgingcontacts.PrintLifetime()

main()
