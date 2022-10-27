# example: little store with map()
# lets say, the euro is worth 0.99 dollars at this moment..

my_store = [("smartphone", 550.00),
            ("case", 10.00),
            ("laptop", 1000.00),
            ("ebook", 150.00),
            ("TV", 800.00)]

# with lambda function
to_euros = lambda data: (data[0], data[1] * 0.99)

# put it in a list for a better overview
store_in_euros = list(map(to_euros, my_store))

print(store_in_euros)
