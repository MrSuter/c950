# Jason Suter 000318620
# W-2_ChainingHashTable_zyBooks_Key-Value_CSV_Greedy.py
# Ref: zyBooks: Figure 7.8.2: Hash table using chaining.
# Ref: zyBooks: 3.3.1: MakeChange greedy algorithm.

import data
import algorithm
import datetime

print('WGUPS app')


# Load packages to Hash Table
print("Loading package data...")
data.loadPackageData('packages.csv')
# Load distances between locations to distanceTable
print("loading distance data...")
distanceTable = data.loadDistanceData('distances.csv')
print('loading address data...')
# Load addresses with their index to address dictionary
addressDict = data.loadAddressData('addresses.csv')
# set all package status to 'at hub' or 'delayed'
algorithm.initializePackages()

truck1 = []
truck2 = []
truck3 = []
startDay = datetime.date.today()
startTime = datetime.time(8,0,0)
startTime2 = datetime.time(10,20,0)
startTime3 = datetime.time(9,5,0)

start1 = datetime.datetime.combine(startDay, startTime)
start2 = datetime.datetime.combine(startDay, startTime2)
start3 = datetime.datetime.combine(startDay, startTime3)

# Time to stop delivering packages
# Initialized at a time well after all packages are delivered
searchTime = datetime.datetime.combine(datetime.date.today(),
                                       datetime.time(19, 0,0))

# Command line user interface menu
while True:
  print('-----------------------------')
  print('Menu:')
  print('1: Display all packages')
  print('2: Deliver all packages')
  print('3: Search for a package at given time')
  print('4: Display all packages at a given time')
  print('Q: Exit')
  choice = input('Type your choice: ')
  
  if choice == 'q' or choice == 'Q':
    print('-----------------------------')
    print('Goodbye')
    break
  # Displays all packages details
  elif choice == '1':
    print('-----------------------------')
    data.printAll()
  # Runs the program to deliver all the packages and displays total miles and time
  elif choice =='2':
    print('-----------------------------')
    searchTime = datetime.datetime.combine(datetime.date.today(),
                                       datetime.time(19, 0,0))
    miles = algorithm.startDeliveries(searchTime)[0]
    hours = miles / 18
    print('Total miles: ', miles)
    print('Total hours: ', hours)
  # Searches for a package at a chosen time
  elif choice == '3':
    print('-----------------------------')
    algorithm.search()
  # Displays all packages at a chosen time
  elif choice == '4':
    print('-----------------------------')
    searchTime = algorithm.trySearch()
    algorithm.startDeliveries(searchTime)
    data.printAll()
  # If input is invalid shows error message
  else:
    print('-----------------------------')
    print('Invalid option, please try again...')