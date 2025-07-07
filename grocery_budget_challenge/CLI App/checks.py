selection_ = ['1,6,18']

#selection = input("Enter Products: ")

products_dict = {'1': 'bread', '6': 'fanta', '18': 'soaps'}

# # print(selection[0].split(","))

# print(products_dict.get(selection[0].split(",")[0]))
# print(selection)

# selection_[0].split(",").append([4,5,8])

# print(selection)

# for p in selection.split(","):
#     # print(p)
#     print(products_dict.get(p))

selection = ['2','3','t']

items = [int(i) for i in selection if i.isdigit() and int(i) in list(products_dict.keys())]

print(items)

#print([products_dict.get(int(i)) for i in selection if i.isdigit() and int(i) in products_dict.keys()])