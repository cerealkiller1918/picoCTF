

# Reading in file
output=[] 
key = 37
letters = []
with open('message.txt','r') as code:
    codes = code.read().split(" ")
    for i in codes:
        if i =='':
            break
        output.append(int(i)%key)

with open('letters.txt','r') as temp:
    letters = temp.read().split("\n")

print("picoCTF{",end='')
for i in output:
    x = letters[i]
    print(x,end='')
print('}')