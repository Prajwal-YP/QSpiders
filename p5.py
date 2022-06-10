# WAP to check weather given value is present inside the collection or not 
#     If value present modify value.
#     If value not present delete start end value of collection

coll=eval('['+input("Enter List values: ")+']')
a=eval(input("Enter value: "))

if( a in coll):
    for i in range(len(coll)):
        if( a == coll[i] ):
            coll[i]='yp'
else:
    coll=coll[1:len(coll)-1]

print("\n\n"+str(coll))