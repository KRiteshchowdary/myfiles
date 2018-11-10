import random
name = ["ritesh","chowdary","konakanchi","revanth","gopi","harsha","venu","gopal"]
surname = ["a","b","c","v","b","n","m","a"]
adress = [67-89,43-46,34-56,34-33,56-76,66-55,12-56,98-79]
street = ["ad","as","qw","er","ty","tr","lo","trr"]
branch = ['BCE','BIT','MCE','ARC','MIT','EEE','BBT']
hobies = ["playing","singing","reading","vedio games","cooking"]
print("profile is")
print("name is ",random.choice(name),".",random.choice(surname))
print("adress is ",random.choice(adress),",",random.choice(street))
print("reg number is",random.randint(10,99),random.choice(branch),random.randint(1000,9999))
print("hobies are ",random.choices(hobies,k = 2))
print("Phone number ",random.randint(10000000,99999999))
