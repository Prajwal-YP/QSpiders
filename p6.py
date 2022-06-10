# QUESTION
    # WAP to check weather the first character of string is Vowel or not
        # If Vowel delete char inside string
        # Else Concate char inside string

#   AUTHOR  :   Prajwal Y P
#   EDITOR  :   V S Code

s=input("Enter String : ")

if( s[0] in 'aeiouAEIOU' ):
    s=s[1:]
else:
    s += s[0]

print("\n\n"+s)