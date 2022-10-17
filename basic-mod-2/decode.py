

# Reading in file
output=[] 
key = 41
letters = []
with open('message.txt','r') as code:
    codes = code.read().split(" ")
    for i in codes:
        if i =='':
            break
        x = pow(int(i),key-2,key)
        output.append(x)

with open('letters.txt','r') as temp:
    letters = temp.read().split("\n")

print("picoCTF{",end='')
for i in output:
    x = letters[i-1]
    print(x,end='')
print('}')