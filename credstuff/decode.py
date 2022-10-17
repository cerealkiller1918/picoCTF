import codecs

decodedPasswords=[]
usernames=[]

with open('./leak/passwords.txt','r') as passwords:

    for password in passwords:
        decode = codecs.decode(password.replace('\n',''),'rot_13')
        decodedPasswords.append(decode)
    

del passwords 
del decode
del password

with open('./leak/usernames.txt','r') as names:
    for name in names:
        usernames.append(name.replace('\n',''))
    
del names
del name
index = 0
userInput = input("Enter user name to search for: ")

for user in usernames:
    if user == userInput:
        print(decodedPasswords[index])
        break
    index +=1