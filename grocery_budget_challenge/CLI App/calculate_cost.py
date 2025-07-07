from fetch_products import fetch_products
from user_selection_menu import shopping_menu
from product_catalogue import init_list


def calculate_cost(selected_items=None):
    """This function calculates the total cost of selected products"""

    if selected_items == None:
        selected_items = []
    else:
        selected_items = selected_items
    
    # get names selected products
    products_price = init_list()[2]

    cost_list = []
    # get the cost each selected item and sum
    cost_list = [products_price.get(p) for p in selected_items]

    total_cost = sum(cost_list)

    return total_cost

# cost = calculate_cost(['detergent', 'biscuits'])

# print(f"The total cost for your items is {cost} Naira only")
