# WITH INTEGER TYPE

def greatest(a,b,c):
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    else:
        return c

a=int(input(" \nEnter 1st Number"))

b=int(input(" \nEnter 2nd Number"))

c=int(input(" \nEnter 3rd Number"))

g=greatest(a,b,c)
print(" \n",g,"Is The Greatest Number")

