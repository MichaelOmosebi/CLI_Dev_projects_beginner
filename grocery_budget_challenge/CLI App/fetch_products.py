from product_catalogue import init_list

products_list, products_dict,_ = init_list()

def fetch_products(shopping_selection=None):
    # split the selections that have been stringed together from input
    # for accessibility of each selected product
    if shopping_selection == None:
        shopping_selection = []
    else:
        shopping_selection = shopping_selection

    # initiate an empty list to collect the names of the selected products
    products_selection = []

    # print(products_selection)

    # loop through the shopping selection to fetch the corresponding product names
    # and append to the products_selection list
    for selection in shopping_selection: #[0][0].split(",")

        # check if the selection is a digit and exists in the products_dict
        try:
            product_name = products_dict.get(int(selection))
        except ValueError:
            print(f"You have have typed in an invalid product code but the other valid product codes, if any have been processed.")
            continue
        products_selection.append(product_name)

    return products_selection
