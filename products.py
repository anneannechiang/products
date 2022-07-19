import os

# read the file
def read_file(filename):
    products = []
    with open(filename, 'r', encoding = 'utf-8') as f:
        for line in f:
            if 'Product, Price' in line:
                continue
            name, price = line.strip().split(',')
            products.append([name, price])
    return products

# user enters data
def user_input(products):
    while True:
        name = input('Enter the product name.. ')
        if name == 'q':
            break
        price = input('Enter the product price.. ')
        products.append([name, price])
    print(products)
    return products

# print all the history
def print_products(products):
    for p in products:
        print('The price of', p[0], 'is', p[1])

# write in data
def write_file(filename, products):
    with open(filename, 'w', encoding = 'utf-8') as f:
        f.write('Product, Price\n')
        for p in products:
            f.write(p[0] + ',' + p[1] + '\n')

def main():
    filename = 'products.csv'
    if os.path.isfile(filename): # check if file exists
        print('Yeah! Found the file!')
        products = read_file(filename)
    else:
        print('Oh no! No file found..')

    products = user_input(products)
    print_products(products)
    write_file('products.csv', products)

main()


