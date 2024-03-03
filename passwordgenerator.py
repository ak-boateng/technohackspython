import string
import random


#ask user for length of password 

length = int(input("Enter length of password you want to generate: "))

#create a password using digits,characters, puntuation

letters = string.ascii_letters

numbers = string.digits

punctuation = string.punctuation

print('''Choose character you want to generate your password from : 
         1. Digits
         2. Letters
         3. Special characters
         4. Exit''')
 
characterSet = ""

while(True):
    userchoice = int(input("Pick a number "))
    if(userchoice == 1):
         
        # Add letters to character set
        characterSet += letters
    elif(userchoice == 2):
         
        # Add digits to character sets
        characterSet += numbers
    elif(userchoice == 3):
        # Add special characters to character set
        characterSet += punctuation
    elif(userchoice == 4):
        break
    else:
        print("Please select from 1- 3!")
 
password = []

#combine it all

for i in range(length):
   
    # Picking a random character from our character set
    randomchar = random.choice(characterSet)
     
    # appending a random character to password
    password.append(randomchar)
 
#print out generated 
print("Your generated password is " + "".join(password))