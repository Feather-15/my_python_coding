intext = int(input("enter the number"))
if intext <0 :
    print (intext," is not a palindrome number")   
rev = 0

while intext != 0 : #intext = 1512
    reverse= intext%10
    rev= (rev)*10 + (reverse)
    intext = intext //10
print (rev)
    