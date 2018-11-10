dictionary = {"Name":"Ritesh","Roll_no":"167326065","Class":"CO","Floor":"Ground","Room_no":"GS11","College_name":"Sri_Chaitanya","Gender":"Male"}

resource = raw_input("What  do you need?")

if(resource in dictionary):
  print("Entering database")
  print("loading......")
  print("Your requested " + resource + " is " + dictionary[resource])
else:
  print("Entering database")
  print("waiting......loading")
  print(" Requested information not available.Do you want to search any other information?")

resource2 = raw_input("What else do you need?")

if(resource2 in dictionary):
  print("Entering database")
  print("loading......")
  print("Your requested " + resource2 + " is " + dictionary[resource2])
else:
  print("Entering database")
  print("waiting......loading")
  print(" Requested information not available.Do you want to search any other information?")
  
resource3 = raw_input("what else do you need?")
  
if(resource3 in dictionary):
  print("Entering database")
  print("loading......")
  print("Your requested " + resource3 + " is " + dictionary[resource3])
else:
  print(" Requested information not available.Do you want to search any other information?")
