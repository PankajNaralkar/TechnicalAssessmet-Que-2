def checkValidity(a, b, c):
     
    
    if (a + b <= c) or (a + c <= b) or (b + c <= a) :
        return False
    else:
        return True       
 

a = 3
b = 4
c = 5
if checkValidity(a, b, c):
    print("Valid Triangle")
else:
    print("Invalid Triangle")

def isRectangle(a, b, c, d):
 
    
    if (a == b and d == c) or (a == c and b == d) or (a == d and b == c):
        return True
    else:
        return False
 
 

a, b, c, d = 2, 4, 2, 4
print("Valid Rectangle" if isRectangle(a, b, c, d) else "Invalid Rectangle")
 