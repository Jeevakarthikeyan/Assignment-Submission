def low_up(string):
    lower = 0
    upper = 0
    for char in string:
        if char.islower():
            lower+=1
        elif char.isupper():
            upper+=1
        else:
            pass
    return("upper and lower ",upper,lower)
        
print(low_up("Hello! This is Jeevajiivi"))
