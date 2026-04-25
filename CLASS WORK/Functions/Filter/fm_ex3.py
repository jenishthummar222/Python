product =[
    {"name":"laptop","price":60000},
    {"name":"mobile","price":17500},
    {"name":"Tv","price":14999},
]

print(product)

price_details = list(map(lambda pri : pri["price"],product))

print(price_details)

price_filter = list(filter(lambda pf:pf["price"]>15000,product))
print(price_filter)

name = list(map(lambda nm : nm["name"],price_filter))
print(name)