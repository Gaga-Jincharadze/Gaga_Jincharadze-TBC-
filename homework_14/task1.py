data = ((33, 34, 28), (24, 31, 27), (24, 23, 27), (28, 32, 34), (33, 21, 28), (20, 25, 31), (21, 31, 28))

def get_data(x):
    average_per_day = ()
    max_per_day = ()
    min_per_day = ()
    
    for i in x:
        average_per_day += (round(sum(i[:]) / len(i),2),)
        max_per_day += (max(i),)
        min_per_day += (min(i),)
        average_per_week = round(sum(average_per_day) / len(data),2)
        


    print("Average per day:", average_per_day)
    print("Max per day:", max_per_day)
    print("Min per day:", min_per_day)
    print("Average per Week:", average_per_week)

get_data(data)