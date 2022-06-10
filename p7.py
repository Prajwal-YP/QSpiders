# WAP to checjk weather given value is consonent or not 
    # if consonent print the replication of 3 times of that char
    # else  store value inside dictionary

# AUTHOR  :   Prajwal Y P
# EDITOR  :   V S Code

c=input("Enter char: ")

if( (c not in "aeiouAEIOU") and ('a'<=c<='z') and ('A'<=c<='Z')):
    print(c*3)
else:
    dict={'item1':c}
    print(dict)

