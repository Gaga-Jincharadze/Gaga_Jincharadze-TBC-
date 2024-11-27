with open('data.txt', 'r') as data, open('small.txt', 'w') as small, open('high.txt', 'w') as high:
    for line in data:
        line = line.strip()
        columns = line.split(',')
        user_name, product_name, amount, price = columns
        amount = int(amount)
        price = float(price)
        Sales = amount * price
        if Sales < 10:
            small.write(line + '\n')
        else:
            high.write(line + '\n')