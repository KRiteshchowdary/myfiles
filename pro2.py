login = {'ritesh':'Mark 1234','steve':'Stevejobs 1','elon':'Elon musk 1'}

user_id =  raw_input("Username please  ")
 
if user_id  not in login:
    print(" user_id not found")
else:
    password = raw_input("Enter password  ")
    if(password == login[user_id]):
        print("Access Granted")
        print "1.Change password."
        print "2.Continue without changing."
        input = int(raw_input("Your option is "))
        if input == 1:
            npassword = raw_input("Whats your new pasword? ")
                
            if len(npassword) < 8 :
                print("Password too short.")
            elif "npassword".islower() == False:
                print("Password must contain atleast one number and one cassed letter and no other .  ")
            elif "npassword".isalpha() == False: 
                print("Password must contain atleast one number and one cased letter and no other characters. ")
            else:
                password2 = raw_input("Retype password ")
                print("Password good.")
                if password2 == npassword:
                    print("Password matched.Congrats.")
                    print "password changed"
                else:                        
                    print "Passwords do not match.Try Again." 
        else:
            print("Thanks you may continue with your account.")
   
  
    else:
            print("Access Denied") 

