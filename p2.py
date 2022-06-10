#WAP to check weather given character is alphabet or not

ch=input("Enter a chracter: ")
ch=ord(ch)
if((65<=ch<=90) or (ch>=90 and ch<=122)):
    print("Alphabet")
else:
    print("Not Alphabet")
