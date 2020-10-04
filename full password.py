import re
corrPass = 0
password = "8274612S"

for i in range(3):
    inputed_password = input("Enter the password:")
    if inputed_password == password:
        print("password is correct")
        print("Access Granted")
        inputed_password = re.sub('[.:()" "]', '', inputed_password)

    else:
        print('You have enter the wrong')
        print('Acess Deined')

