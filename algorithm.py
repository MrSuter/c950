import data
import datetime

# get the address dictionary
addressDict = data.loadAddressData('addresses.csv')

# Create the list of packages for each truckload
load1IDList = [1, 5, 8, 13, 14, 15, 16, 19, 20, 21, 27,
               30, 34, 35, 37, 39]
load2IDList = [18,36,3,11,9,17,12,38,23,10]
load3IDList = [25,26,4,40,31,32,6,7,29,28]
load4IDList = [24,22,2,33]
truckLoad = []
deliveredPackages = []

truck1 = []
truck2 = []
truck3 = []
# Create the dates and times to be used in the search function
startDay = datetime.date.today()
startTime = datetime.time(8,0,0)
startTime2 = datetime.time(10,20,0)
startTime3 = datetime.time(9,5,0)

start1 = datetime.datetime.combine(startDay, startTime)
start2 = datetime.datetime.combine(startDay, startTime2)
start3 = datetime.datetime.combine(startDay, startTime3)

searchTime = datetime.datetime.combine(datetime.date.today(),
                                       datetime.time(19, 0,0))

# Takes the list of package ID's and appends each package to the
# truckload list of package objects
# also changes the status of the package to 'En route' at the given time 
def loadTruck(load, t):
  for id in load:
    package = data.myHash.search(id)
    time1 = t.strftime("%H:%M:%S")
    package.status = 'En route %s' %(time1)
    truckLoad.append(package)
  return truckLoad


# Takes address string and finds address ID from address dictionary
def getAddressID(address):
  addressID = addressDict[address]
  return addressID

# Takes two address ID's and finds the distance between using the distance table
def distanceBetween(address1, address2):
  distance = data.distanceTable[address1][address2]
  return distance

# Takes an address and a list of packages 
# returns the address of the package that is closest to the current address 
# by calling distanceBetween on each package in the list
def minDistanceFrom(fromAddress, truckLoad):
  minDistanceFrom = float('inf')
  for package in truckLoad:
    address = package.address
    addressID = getAddressID(address)
    nextDistance = distanceBetween(fromAddress, addressID)
    if nextDistance < minDistanceFrom:
      minDistanceFrom = nextDistance
      nextPackage = package
  
  return nextPackage, minDistanceFrom

# Accepts a list of packages, start time and search time
# Runs the delivery algorithm until the truck is empty or the time passes the serach time.
def deliverPackages(truck, startTime, searchTime):
  fromAddress = 1
  totalDistance = 0
  totalTime = 0
  while truck and startTime < searchTime:
    getData = minDistanceFrom(fromAddress, truck)
    nextPackage = getData[0]
    nextDistance = getData[1]
    nextTime = nextDistance / 18
    timeDelta = datetime.timedelta(hours = nextTime)
    startTime += timeDelta
    totalDistance = round(totalDistance + nextDistance, 1)
    totalTime += nextTime
    timeDelivered = startTime # + timeDelta
    fromAddress = nextPackage.address
    fromAddress = getAddressID(fromAddress)
    truck.remove(nextPackage)
    timeDelivered = timeDelivered.strftime("%H:%M:%S")
    nextPackage.status = 'Delivered %s' %(timeDelivered)
    deliveredPackages.append(nextPackage)
  if startTime < searchTime:
    toHub = distanceBetween(fromAddress, 1)
    totalDistance = totalDistance + toHub
    totalTime = totalTime + (toHub / 18)
  
  return totalDistance, totalTime

# Updates the given package in the hash table  
def updatePackage(package):
  pID = package.ID
  package
  data.myHash.insert(pID, package)

# Changes the status of each package to 'at hub' or 'delayed'
def initializePackages():
  i = 1
  while i <= 40:
    package = data.myHash.search(i)
    delayed = 'Delayed on flight---will not arrive to depot until 9:05 am'
    if package.notes != delayed:
      package.status = 'At hub'
    else:
      package.status = 'Delayed'
    i += 1

# Resets all package status, then delivers packages up until search time
# by calling deliverPackages    
def startDeliveries(searchTime):
  initializePackages()
  miles1 = 0
  miles2 = 0
  miles3 = 0  
  miles4 = 0  
  #Determines which loads of packages will get started before the search time
  if start1 < searchTime:
      truck2 = loadTruck(load1IDList, start1)
      miles1 = deliverPackages(truck2, start1, searchTime)[0]
  if start2 < searchTime:
      truck2 = loadTruck(load2IDList, start2)
      miles2 = deliverPackages(truck2, start2, searchTime)[0]
  if start3 < searchTime:
      truck1 = loadTruck(load3IDList, start3)
      miles3 = deliverPackages(truck1, start3, searchTime)[0]
      print('-----------------------------')
  if start1 < searchTime:
      truck1 = loadTruck(load4IDList, start1)
      miles4 = deliverPackages(truck1, start1, searchTime)[0]
  miles = round(miles1 + miles2 + miles3 + miles4, 1)
  hours = miles / 18
  return miles, hours

#search by package ID number 0 cancels search
def search():
  searchTime = trySearch()
  startDeliveries(searchTime)
  while True:
    print('-----------------------------')
    print('Choose package ID. Use 0 to exit search.')
    try: 
      pID = int(input('Search: '))
      if pID != 0:
        
        print(data.myHash.search(pID))
      else:
        break
    except:
      print('Wrong format')
      
    
# repeats until a valid time is input
def trySearch():
  try:
    searchTime = input('Choose time HH:MM - ')
    hh, mm  = map(int, searchTime.split(':'))
    searchTime = datetime.datetime.combine(datetime.date.today(), datetime.time(hh, mm))
  except:
    print('Wrong format')
    trySearch()
  return searchTime
