cache = {} 

def sequence(n):
    key = n 
    value = []  

    if n in cache:  
        return cache[n]
        
    while n != 1: 
        value.append(n)
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
    value.append(1) 

    cache[key] = value 
    return value


print(sequence(3)) 
print(cache)
print(sequence(3)) 
print(cache)  
