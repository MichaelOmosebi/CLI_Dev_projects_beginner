
from product_catalogue import init_list
from user_selection_menu import display_menu, shopping_menu
from fetch_products import fetch_products
from calculate_cost import calculate_cost
from time import sleep

SHOPPER_BUDGET = input("What is your budget for this shopping: ")

while True:

    #show shopping menu and allow shopper to interact with cart
    shopping_list = shopping_menu()

    # if shopping list is empty, prompt shopper to add items

    selected_items = fetch_products(shopping_list)

    print(f"You have selected the following items: {selected_items}")
    print(f"You have {(len(selected_items))} items in your cart.")

    total_cost = calculate_cost(selected_items)
    print(f"Total cost of your selected items is {total_cost} Naira only")

    while total_cost > float(SHOPPER_BUDGET):
        print("You have exceeded your budget. Please remove some items from your cart.")
        shopping_list = shopping_menu(shopping_list)
        selected_items = fetch_products(shopping_list)
        print(f"You have selected the following items: {selected_items}")
        print(f"You have {(len(selected_items))} items in your cart.")
        total_cost = calculate_cost(selected_items)
        print(f"Total cost of your selected items is {total_cost} Naira only")
        if total_cost <= float(SHOPPER_BUDGET):
            break
        else:
            print("You have exceeded your budget again! Please remove some items from your cart.")
        continue
    sleep(1)  # Simulate a brief pause before proceeding
    print("You are within your budget. Proceeding to checkout...")

    sleep(2)  # Simulate processing time
    debit_confirmation = input(f"Enter 'YES' to confirm that the total cost {total_cost} Naira should be debited from your account: ")

    match debit_confirmation.lower():
        case 'yes':
            print("Thank you for your confirmation. Proceeding with the payment...")
            sleep(2)  # Simulate payment processing time
            # Process the payment here
            SHOPPER_BUDGET = float(SHOPPER_BUDGET) - total_cost

            print(f"Payment was successful. Your balance is now {SHOPPER_BUDGET} Naira.")
            sleep(1)  # Simulate a brief pause before final message
            print("Thank you for shopping with us!\nHave a great day!")

        case 'no':
            print("Payment cancelled. Please review your cart and try again.")
            continue

        case _:
            print("Invalid input. Please enter 'YES' or 'NO'.")
            continue
    # Exit the loop after successful checkout

    break