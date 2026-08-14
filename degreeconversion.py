inscale = int(input("Press 1 for Celcius Press 2 for farenheit"))
temp =float(input("enter the temperature"))

if inscale==1:
    output= (temp*1.8)+32
else:
    output= (temp-32)/1.8
    
print("the result is ",output)