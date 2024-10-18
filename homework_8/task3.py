#because of format is same in all example provided in word documnet, i just write my code without input function. just supposed  that customer will type same date format as provided in my example 
text = "2024-03-22T19:17:42.956376+04:00"


def short_date():
    short_date = text[0:text.find('T')]   
    year = short_date[0:4]
    month = short_date[5:7]  
    day = short_date[8:10]
    reversed_date = day + "-" + month + "-" + year
    return reversed_date


def time():
    time = text[text.find('T')+1:text.find('.')]
    hour, minute, sec = int(time[:2]), time[3:5], time[6:8]
    hour = hour - 12 if hour > 12 else (12 if hour == 0 else hour)
    return f"{hour:02}:{minute}:{sec}"



def timezone():
    timezone = text[text.find('+')+2]
    return timezone

print(short_date(), time(), "+",timezone())