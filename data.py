import csv
import hashTable
from package import Package 
import datetime

#Initialize distance table
distanceTable = []



# Reads csv file with distances between addresses and creates the distance table
def loadDistanceData(fileName):
  with open(fileName) as locations:
    distanceData = csv.reader(locations, delimiter = ',')
    #next(distanceData)
    for location in distanceData:
      location = [float(x) for x in location]
      distanceTable.append(location)
      
  return distanceTable

#Initialize address dictionary
addressDict = {}
# Reads csv file with addresses and address index, then creates the address dictionary
def loadAddressData(filename):
  with open(filename) as addresses:
    addressData = csv.reader(addresses, delimiter = ',')
    addressDict = {rows[(0)]:int(rows[1]) for rows in addressData}
  
  return addressDict

# HashTable class using chaining.
myHash = hashTable.ChainingHashTable()  

# Reads csv file of package data and creates all of the package objects
#  then inserts the package into the hash table
def loadPackageData(fileName):
    with open(fileName) as packages:
        packageData = csv.reader(packages, delimiter=',')
        next(packageData) # skip header
        for package in packageData:
          pID = int(package[0])
          pAddress = package[1]
          pCity = package[2]
          pState = package[3]
          pZip = package[4]
          pDeadline = package[5]
          pMass = package[6]
          pNotes = package[7]
          pStatus = "Unknown"
           
            # package object
          p = Package(pID, pAddress, pCity, pState, pZip, pDeadline, pMass, pNotes, pStatus)
            # insert it into the hash table
          myHash.insert(pID, p)
# Prints each of the packages in the hash table
def printAll():
  print("All packages:")
  # Fetch data from Hash Table
  for i in range (len(myHash.table) + 30): 
      print("Package: {}".format(myHash.search(i+1))) 




