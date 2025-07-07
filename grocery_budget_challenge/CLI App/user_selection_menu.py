from product_catalogue import init_list
from fetch_products import fetch_products

def display_menu():
    print("Shopping List Manager")
    print("1. Select Items", "\t", "2. Remove Items")
    #print("2. Remove Items")
    print("3. View List", "\t", "\t", "4. Checkout")
    #print("4. Exit")

def shopping_menu(shopping_list=None):
    """This function displays the shopping menu and allows the user to interact with their shopping list."""
    
    #Initialize the shopping list if not provided.
    if shopping_list == None:
        shopping_list = []
    else:
        shopping_list = shopping_list
    

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            # display available products
            products_list, products_dict,_ = init_list()
            print(products_list)

            # Prompt to select items from available products
            items = input("Please type the numbers corresponding to your products e.g. 1,6,19: ").replace(" ","").split(",")


            if items:
                shopping_list.extend(items)
                print(shopping_list)
                # print(f"'{item}' has been added to your shopping list.")
        elif choice == '2':
            # Prompt for and remove an item
            item = input("Enter the item to remove: ").strip()
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"'{item}' has been removed from your shopping list.")
            else:
                print(f"'{item}' not found in the shopping list.")
        elif choice == '3':
            # Display the shopping list
            if shopping_list:
                print("You have selected {} items on the shopping list:".format(len(shopping_list)))
                #fetch_products(shopping_list)
                # print("\n".join(f"- {item}" for item in shopping_list))
                # for idx, item in enumerate(shopping_list, start=1):
                #     print(f"{idx}. {item}")
            else:
                print("Your shopping list is empty. Please add items")

        elif choice == '4':
            if not shopping_list:
                print("Your shopping list is empty. Please add items before checking out.")
                continue
            print("...staging your items for checkout...")
            break
        else:
            print("Invalid choice. Please try again.")

    return shopping_list
    #print(shopping_list)

# if __name__ == "__main__":
#     shopping_menu()