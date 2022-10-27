class Package: #ID,Address,City,State,Zip,Delivery Deadline,Mass KILO,Special Notes
    def __init__(self, ID, address, city, state, zip, deadline, mass, notes, status):
      self.ID = ID
      self.address = address
      self.city = city
      self.state = state
      self.zip = zip
      self.deadline = deadline
      self.mass = mass
      self.notes = notes
      self.status = status
    
    def __str__(self):  # overwite print(Movie) otherwise it will print object reference 
        return "%s, %s, %s, %s, %s, %s, %s, %s, %s" % (self.ID, self.address, self.city, self.state, self.zip, self.deadline, self.mass, self.notes, self.status)  

