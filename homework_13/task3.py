text = ["gaga","tako","gia","jora","ana","tbc"]

for i in map(lambda x: x , text ):
    if len(i) <= 3:
        print(i.upper())