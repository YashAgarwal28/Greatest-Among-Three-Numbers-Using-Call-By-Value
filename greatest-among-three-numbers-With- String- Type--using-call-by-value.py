# WITH STRING TYPE

def greatest(a,b,c):
    if(a>b and a>c):
        print("A Is greatest Than All")
    elif(b>a and b>c):
        print("B Is Greatest Than All")
    else:
        print("C Is Greatest Than All")

a=int(input("Enter 1st Number"))

b=int(input("Enter 2nd Number"))

c=int(input("Enter 3rd Number"))

g=greatest(a,b,c)