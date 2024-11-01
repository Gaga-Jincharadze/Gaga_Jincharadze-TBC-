def sorted_list(list1, list2):
    new = []
    full_list = list1 + list2
    
    for _ in range(len(full_list)):
        min_value = min(full_list)
        if min_value not in new:            # i just removed duplicates :)
            new.append(min_value)
        full_list.remove(min_value)
    return new

if __name__ == "__main__":

        a,b = [1, 3, 10], [0, 4, 7, 9, 10]
        c,d = [1, 2, 2, 3], [2, 3, 3, 4]
        e,f = [5, 5, 5], [5, 6, 6, 6]
        
print(sorted_list(a,b))
print(sorted_list(c,d))
print(sorted_list(e,f))