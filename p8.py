s='abcdemoprqabbczxy'

i=0
l=[]
while i<len(s):
    p=ord(s[i])
    try:
        if(ord(s[i+1])==p+1 and ord(s[i+2])==p+2 ):
            l.append(s[i]+s[i+1]+s[i+2])
            i+=3
            continue
    except:
        pass
    i+=1


print(l)
print(len(l))