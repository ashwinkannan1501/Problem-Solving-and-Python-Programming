# Python program to find the exponent of a given number

#def power(base, exponent):
    #if(exponent == 1):
        #return base
    #else:
        #return (base * power(base, exponent - 1))
    
base = int(input("Enter the base value : "))
exponent = int(input("Enter the exponent value : "))

#print(power(base, exponent))

print(f"{base} ** {exponent} = {base ** exponent}")
