s=input("Enter : ")

# T - len
# F - hal


if( s == s[::-1]):
    print(len(s))
else:
    print(s[:len(s)//2])