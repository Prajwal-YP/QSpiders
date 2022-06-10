#WAP  to check character is special or not, If special print else print ascii value

ch=input("Enter : ")

if('a'<=ch<='z' or 'A'<=ch<='Z' or '0'<=ch<='9'):
    print(ord(ch))
else:
    print(ch)