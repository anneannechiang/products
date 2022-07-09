products = []
while True:
    name = input('Enter the product name.. ')
    if name == 'q':
    	break
    price = input('Enter the product price.. ')
    products.append([name, price])
print(products)
