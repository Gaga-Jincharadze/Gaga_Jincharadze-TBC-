import json

customer_names = []
customer_values = []
customer_quantities = []
customer_max_purchases = []

product_names = []
product_total_quantities = []

with open("data.txt", "r") as file:
    for line in file:
        name, product, amount, price = line.strip().split(",")
        amount = int(amount)
        price = float(price)
        total = amount * price

        if name not in customer_names:
            customer_names.append(name)
            customer_values.append(0) 
            customer_quantities.append(0)
            customer_max_purchases.append(0)

        index = customer_names.index(name)
        customer_values[index] += total
        customer_quantities[index] += amount
        customer_max_purchases[index] = max(customer_max_purchases[index], amount)

        if product not in product_names:
            product_names.append(product)
            product_total_quantities.append(0)

        product_index = product_names.index(product)
        product_total_quantities[product_index] += amount

max_purchase_quantity = max(customer_max_purchases)
max_purchase_value = max(customer_values)
most_sold_quantity = max(product_total_quantities)


max_quantity_customers = []
for i in range(len(customer_names)):
    if customer_max_purchases[i] == max_purchase_quantity:
        max_quantity_customers.append(customer_names[i])

max_value_customers = []
for i in range(len(customer_names)):
    if customer_values[i] == max_purchase_value:
        max_value_customers.append(customer_names[i])

most_sold_products = []
for i in range(len(product_names)):
    if product_total_quantities[i] == most_sold_quantity:
        most_sold_products.append(product_names[i])

mean_purchase_value = sum(customer_values) / len(customer_values)
mean_order_quantity = sum(customer_quantities) / len(customer_quantities)

results = {
    "max_quantity_customers": max_quantity_customers,
    "max_value_customers": max_value_customers,
    "mean_purchase_value": mean_purchase_value,
    "mean_order_quantity": mean_order_quantity,
    "most_sold_products": most_sold_products
}


with open("stats.json", "w") as stats_file:
    json.dump(results, stats_file, indent=4)



