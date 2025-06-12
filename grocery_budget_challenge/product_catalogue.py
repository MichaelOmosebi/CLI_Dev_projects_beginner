
def init_list():
    product_list = ['bread', 'soda', 'peanut butter', 'margarine', 'mayonnaise',
                    'fruit juice', 'detergent', 'biscuits', 'energy drink', 'yoghourt',
                    'spice', 'sauce', 'ketchup', 'cheese', 'groundnut oil',
                    'rice', 'noodles', 'spaghetti', 'body cream', 'bathroom soap'
                    ]
    price_list = [1000, 600, 2500, 3000, 2100,
                1500, 800, 1100, 800, 1300,
                500, 600, 900, 1100, 2900,
                20000, 7000, 1300, 2600, 3100
                ]

    product_price = dict(zip(product_list, price_list))

    products_map_list = [f"{idx}. {item}" for idx, item in enumerate(product_list, start=1)]
    products_map_dict = {k:v for k,v in enumerate(product_list, start=1)}

    # print(products_map_dict)
    return products_map_list, products_map_dict, product_price
    #print(products_map)


if __name__ == "__main__":
    init_list ()

