up = {'tim':'cook','steve':'jobs','elon':'musk','satyam':'nadela','sundaram':'pichai'}

user_id = raw_input("user_id please  " )
if user_id  not in up:
 print("user_id not found")
else:
  password = raw_input("Enter password  ")
  if(password == up[user_id]):
    print("Access Granted  ")
  else:
    print("Access Denied")