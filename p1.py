# WAP to check weather the length of the list collection is even or odd, if its even print entire list

def isValidList(a):
    if( len(a)%2==0 ):
        print("Even Length List")
    else:
        print("Odd Length List")
        print("Middle Element: ",a[len(a)//2])

l=eval('['+input("Enter list Values: ")+']')
isValidList(l)