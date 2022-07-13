# read the file
products = []
with open('products.csv', 'r', encoding = 'utf-8') as f:
	for line in f:
		if 'Product, Price' in line:
			continue
		name, price = line.strip().split(',')
		products.append([name, price])
print(products)

# user enters data
while True:
    name = input('Enter the product name.. ')
    if name == 'q':
    	break
    price = input('Enter the product price.. ')
    products.append([name, price])
print(products)

# print all the history
for p in products:
	print('The price of', p[0], 'is', p[1])

# write in data
with open('products.csv', 'w', encoding = 'utf-8') as f:
	f.write('Product, Price\n')
	for p in products:
		f.write(p[0] + ',' + p[1] + '\n')

