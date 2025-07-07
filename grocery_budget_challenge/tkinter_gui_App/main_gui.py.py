# importing in-built packages
import time
import requests
import json
import ast
import csv, os
import pandas as pd
import threading
import datetime as dt
from calendar import monthrange
from pandas.tseries.offsets import DateOffset

import tkinter as tk
from tkcalendar import Calendar
import pandas as pd
from tkcalendar import DateEntry
from tkinter import messagebox

import ttkbootstrap as ttk
from ttkbootstrap.constants import *

# importing in-built packages
from product_catalogue import init_list
from user_selection_menu import display_menu, shopping_menu
from fetch_products import fetch_products
from calculate_cost import calculate_cost

# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
root = ttk.Window(themename="solar")
root.title("LAGOS MEGA MART 🛒") #App Title/Name
root.iconbitmap(default='grocery_bag.ico')

logo_image = tk.PhotoImage(file = 'grocery_bag.png')
root.iconphoto(False, logo_image)

# setting window width and height
root.geometry('1620x800')
# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------

#Create Label for the Window/App
headingLabel = tk.Label(root, text='LAGOS MEGA MART', font=('times new roman', 20, 'bold'), 
                        bg='gray20', fg='steelblue', bd=10, relief='groove')
headingLabel.pack(fill=tk.X)
# headingLabel.grid(row=0, column=0, padx=6, pady=2)

#2.0 Create a Frame that houses Customer Details inside the App root
customer_details_frame = tk.LabelFrame(root, text='', font=('times new roman', 13, 'bold'), fg='steelblue', background='gray30', border=8, relief='sunken')
customer_details_frame.configure(height=30)
customer_details_frame.pack(fill=tk.X)

# 2.1.0 Create a Label for shopper
customer_details_label = tk.Label(customer_details_frame, text='Shopper Name: ', font=('times new roman', 12, 'bold'), background='gray30', foreground='white')
customer_details_label.grid(row=0, column=0, padx=6, pady=2)

# 2.1.1 Create entry field for shopper name
customernameEntry = tk.Entry(customer_details_frame, font=('arial', 10), width=22, bd=5, relief='sunken')
#usernameEntry.insert(tk.END, 'xxxxx@mail.com')
customernameEntry.grid(row=0, column=1, pady=9, padx=6, columnspan=1)

# 2.2.0 Create a Label for shopper email
shopperName_label = tk.Label(customer_details_frame, text='Email: ', font=('times new roman', 12, 'bold'), background='gray30', foreground='white')
shopperName_label.grid(row=0, column=2, padx=6, pady=2)

# 2.2.1 Create entry field for shopper email
shopperNameEntry = tk.Entry(customer_details_frame, font=('arial', 10), width=26, bd=5)
shopperNameEntry.grid(row=0, column=3, pady=9, padx=6, columnspan=1)

# 2.2.2 Create a Label for shopper phone
shopperPhone_label = tk.Label(customer_details_frame, text='Mobile No.: ', font=('times new roman', 10, 'bold'), background='gray30', foreground='white')
shopperPhone_label.grid(row=0, column=4, padx=6, pady=2)

# 2.2.3 Create entry field for shopper phone
shopperPhone_Entry = tk.Entry(customer_details_frame, font=('arial', 10), width=16, bd=5)
shopperPhone_Entry.grid(row=0, column=5, pady=9, padx=6, columnspan=1)

# 2.2.4 Create a Label to search for tickets
ticketSearch_label = tk.Label(customer_details_frame, text='Voucher Number: ', font=('times new roman', 10, 'bold'), background='gray30', foreground='white')
ticketSearch_label.grid(row=0, column=6, padx=6, pady=2)

# 2.2.5 Create a button to activate the search for tickets
ticketSearch_button = tk.Button(customer_details_frame, text='Search', font=('arial', 10, 'bold'), width=15, bd=5, relief='sunken', bg='steelblue', fg='white')
ticketSearch_button.grid(row=0, column=8, pady=9, padx=6, columnspan=1) 

# 2.2.5 Create entry field to search for tickets
ticketSearch_Entry = tk.Entry(customer_details_frame, font=('arial', 10), width=16, bd=5, relief='sunken', bg='white')
ticketSearch_Entry.grid(row=0, column=7, pady=9, padx=6, columnspan=1)

#3.0 Create a Frame that houses the Product Catalogue inside the App root
shoppingDetails = tk.Frame(root, bd=8, relief='groove', width=35, background='gray30')
shoppingDetails.pack(fill=tk.X)
# product_catalogue_frame.grid(row=1, column=0, padx=6, pady=6, sticky='w')

# # 3.1 Create a section for the product catalogue/shopping selection --- PRODUCTS CATALOGUE
productSelection_frame = tk.LabelFrame(shoppingDetails, text='', font=('times new roman', 12, 'bold'), background='gray30', foreground='white')
productSelection_frame.grid(row=0, column=0, padx=6, pady=2)

# 3.1.0 Create a Frame for the product sections
productionSection_frame = tk.Frame(productSelection_frame, bd=8, relief='groove', width=35, background='gray30')
productionSection_frame.pack(fill=tk.X)#.grid(row=0, column=0, padx=6, pady=2)

# 3.1.1 Create a Label for the first product section
productSection1_label = tk.LabelFrame(productionSection_frame, text='Section 1', font=('times new roman', 13, 'bold'), width=15, bd=7, relief='groove')
productSection1_label.grid(row=0, column=0, padx=6, pady=2, sticky='n')

# 3.1.2 Create a Label and entry field for the first product
product1_1_label = tk.Label(productSection1_label, text='Product 1: ', font=('times new roman', 12, 'bold'), background='gray30', fg='white')
product1_1_label.grid(row=0, column=0, padx=6, pady=4)

product1_1_entry = tk.Entry(productSection1_label, font=('arial', 10), width=5, bd=5)
product1_1_entry.grid(row=0, column=1, padx=10, pady=8)

# 3.1.3 Create a Label and entry field for the second product
product2_1_label = tk.Label(productSection1_label, text='Product 2: ', font=('times new roman', 12, 'bold'), background='gray30', foreground='white')
product2_1_label.grid(row=1, column=0, padx=6, pady=4)

product2_1_entry = tk.Entry(productSection1_label, font=('arial', 10), width=5, bd=5)
product2_1_entry.grid(row=1, column=1, padx=10, pady=8)

# 3.1.4 Create a Label and entry field for the third product
product3_1_label = tk.Label(productSection1_label, text='Product 3: ', font=('times new roman', 12, 'bold'), background='gray30', foreground='white')
product3_1_label.grid(row=2, column=0, padx=6, pady=4)

product3_1_entry = tk.Entry(productSection1_label, font=('arial', 10), width=5, bd=5)
product3_1_entry.grid(row=2, column=1, padx=10, pady=8)

# 3.1.5 Create a Label and entry field for the fourth product
product4_1_label = tk.Label(productSection1_label, text='Product 4: ', font=('times new roman', 12, 'bold'), background='gray30', foreground='white')
product4_1_label.grid(row=3, column=0, padx=6, pady=4)

product4_1_entry = tk.Entry(productSection1_label, font=('arial', 10), width=5, bd=5)
product4_1_entry.grid(row=3, column=1, padx=10, pady=8)

# 3.1.6 Create a Label and entry field for the fifth product
product5_1_label = tk.Label(productSection1_label, text='Product 5: ', font=('times new roman', 12, 'bold'), background='gray30', foreground='white')
product5_1_label.grid(row=4, column=0, padx=6, pady=4)

product5_1_entry = tk.Entry(productSection1_label, font=('arial', 10), width=5, bd=5)
product5_1_entry.grid(row=4, column=1, padx=10, pady=8)

# 3.2.1 Create a Label for the second product section
productSection2_label = tk.LabelFrame(productionSection_frame, text='Section 2', font=('times new roman', 13, 'bold'), width=15, bd=7, relief='groove')
productSection2_label.grid(row=0, column=1, padx=6, pady=2, sticky='n')

# 3.2.2 Create a Label and entry field for the first product
product1_2_label = tk.Label(productSection2_label, text='Product 1: ', font=('times new roman', 12, 'bold'), background='gray30', foreground='white')
product1_2_label.grid(row=0, column=0, padx=6, pady=4)
product1_2_entry = tk.Entry(productSection2_label, font=('arial', 10), width=5, bd=5)
product1_2_entry.grid(row=0, column=1, padx=10, pady=8)

# 3.2.3 Create a Label and entry field for the second product
product2_2_label = tk.Label(productSection2_label, text='Product 2: ', font=('times new roman', 12, 'bold'), background='gray30', foreground='white')
product2_2_label.grid(row=1, column=0, padx=6, pady=4)
product2_2_entry = tk.Entry(productSection2_label, font=('arial', 10), width=5, bd=5)
product2_2_entry.grid(row=1, column=1, padx=10, pady=8)

# 3.2.4 Create a Label and entry field for the third product
product3_2_label = tk.Label(productSection2_label, text='Product 3: ', font=('times new roman', 12, 'bold'), background='gray30', foreground='white')
product3_2_label.grid(row=2, column=0, padx=6, pady=4)
product3_2_entry = tk.Entry(productSection2_label, font=('arial', 10), width=5, bd=5)
product3_2_entry.grid(row=2, column=1, padx=10, pady=8)

# 3.2.5 Create a Label and entry field for the fourth product
product4_2_label = tk.Label(productSection2_label, text='Product 4: ', font=('times new roman', 12, 'bold'), background='gray30', foreground='white')
product4_2_label.grid(row=3, column=0, padx=6, pady=4)
product4_2_entry = tk.Entry(productSection2_label, font=('arial', 10), width=5, bd=5)
product4_2_entry.grid(row=3, column=1, padx=10, pady=8)

# 3.2.6 Create a Label and entry field for the fifth product
product5_2_label = tk.Label(productSection2_label, text='Product 5: ', font=('times new roman', 12, 'bold'), background='gray30', foreground='white')
product5_2_label.grid(row=4, column=0, padx=6, pady=4)
product5_2_entry = tk.Entry(productSection2_label, font=('arial', 10), width=5, bd=5)
product5_2_entry.grid(row=4, column=1, padx=10, pady=8)

# 3.3.1 Create a Label for the third product section
productSection3_label = tk.LabelFrame(productionSection_frame, text='Section 3', font=('times new roman', 13, 'bold'), width=15, bd=7, relief='groove')
productSection3_label.grid(row=0, column=2, padx=6, pady=2, sticky='n')

# 3.3.2 Create a Label and entry field for the first product in section 3
product1_3_label = tk.Label(productSection3_label, text='Product 1: ', font=('times new roman', 12, 'bold'), background='gray30', foreground='white')
product1_3_label.grid(row=0, column=0, padx=6, pady=4)
product1_3_entry = tk.Entry(productSection3_label, font=('arial', 10), width=5, bd=5)
product1_3_entry.grid(row=0, column=1, padx=10, pady=8)

# 3.3.3 Create a Label and entry field for the second product in section 3
product2_3_label = tk.Label(productSection3_label, text='Product 2: ', font=('times new roman', 12, 'bold'), background='gray30', foreground='white')
product2_3_label.grid(row=1, column=0, padx=6, pady=4)
product2_3_entry = tk.Entry(productSection3_label, font=('arial', 10), width=5, bd=5)
product2_3_entry.grid(row=1, column=1, padx=10, pady=8)

# 3.3.4 Create a Label and entry field for the third product in section 3
product3_3_label = tk.Label(productSection3_label, text='Product 3: ', font=('times new roman', 12, 'bold'), background='gray30', foreground='white')
product3_3_label.grid(row=2, column=0, padx=6, pady=4)
product3_3_entry = tk.Entry(productSection3_label, font=('arial', 10), width=5, bd=5)
product3_3_entry.grid(row=2, column=1, padx=10, pady=8)

# 3.3.5 Create a Label and entry field for the fourth product in section 3
product4_3_label = tk.Label(productSection3_label, text='Product 4: ', font=('times new roman', 12, 'bold'), background='gray30', foreground='white')
product4_3_label.grid(row=3, column=0, padx=6, pady=4)
product4_3_entry = tk.Entry(productSection3_label, font=('arial', 10), width=5, bd=5)
product4_3_entry.grid(row=3, column=1, padx=10, pady=8)

# 3.3.6 Create a Label and entry field for the fifth product in section 3
product5_3_label = tk.Label(productSection3_label, text='Product 5: ', font=('times new roman', 12, 'bold'), background='gray30', foreground='white')
product5_3_label.grid(row=4, column=0, padx=6, pady=4)
product5_3_entry = tk.Entry(productSection3_label, font=('arial', 10), width=5, bd=5)
product5_3_entry.grid(row=4, column=1, padx=10, pady=8)

# 3.4.1 Create a Label for the fourth product section
productSection4_label = tk.LabelFrame(productionSection_frame, text='Section 4', font=('times new roman', 13, 'bold'), width=15, bd=7, relief='groove')
productSection4_label.grid(row=0, column=3, padx=6, pady=2, columnspan=2, sticky='n')

# 3.4.2 Create a Label and entry field for the first product in section 4
product1_4_label = tk.Label(productSection4_label, text='Product 1: ', font=('times new roman', 12, 'bold'), background='gray30', foreground='white')
product1_4_label.grid(row=1, column=0, padx=6, pady=4)
product1_4_entry = tk.Entry(productSection4_label, font=('arial', 10), width=5, bd=5)
product1_4_entry.grid(row=1, column=1, padx=10, pady=8)

# 3.4.3 Create a Label and entry field for the second product in section 4
product2_4_label = tk.Label(productSection4_label, text='Product 2: ', font=('times new roman', 12, 'bold'), background='gray30', foreground='white')
product2_4_label.grid(row=2, column=0, padx=6, pady=4)
product2_4_entry = tk.Entry(productSection4_label, font=('arial', 10), width=5, bd=5)
product2_4_entry.grid(row=2, column=1, padx=10, pady=8)

# 3.4.4 Create a Label and entry field for the third product in section 4
product3_4_label = tk.Label(productSection4_label, text='Product 3: ', font=('times new roman', 12, 'bold'), background='gray30', foreground='white')
product3_4_label.grid(row=3, column=0, padx=6, pady=4)
product3_4_entry = tk.Entry(productSection4_label, font=('arial', 10), width=5, bd=5)
product3_4_entry.grid(row=3, column=1, padx=10, pady=8)

# 3.4.5 Create a Label and entry field for the fourth product in section 4
product4_4_label = tk.Label(productSection4_label, text='Product 4: ', font=('times new roman', 12, 'bold'), background='gray30', foreground='white')
product4_4_label.grid(row=4, column=0, padx=6, pady=4)
product4_4_entry = tk.Entry(productSection4_label, font=('arial', 10), width=5, bd=5)
product4_4_entry.grid(row=4, column=1, padx=10, pady=8)

# 3.4.6 Create a Label and entry field for the fifth product in section 4
product5_4_label = tk.Label(productSection4_label, text='Product 5: ', font=('times new roman', 12, 'bold'), background='gray30', foreground='white')
product5_4_label.grid(row=5, column=0, padx=6, pady=4)
product5_4_entry = tk.Entry(productSection4_label, font=('arial', 10), width=5, bd=5)
product5_4_entry.grid(row=5, column=1, padx=10, pady=8)

# 4.0 Create a Frame that houses the text frame which shows the progress text
shoppingCart_frame = tk.Frame(shoppingDetails, bd=8, relief='groove', width=35, background='gray30')
shoppingCart_frame.grid(row=0, column=1, padx=6, pady=2)

# 4.1 Create a Frame that houses the text frame which shows the shopping cart
shoppingCart_frame = tk.Frame(shoppingDetails, bd=8, relief='flat', width=35, background='gray30')
shoppingCart_frame.grid(row=0, column=1, padx=6, pady=2)

# 4.1.1 Create a Label for the shopping cart
shoppingDescription = tk.Label(shoppingCart_frame, text='Shopping Cart', font=('times new roman', 13, 'bold'), width=48, bd=7, relief='groove')
shoppingDescription.pack(fill='x')

# 4.1.2 Create a text area to display the shopping cart items
shoppingCartText = tk.Text(shoppingCart_frame, height=18, width=75, bd=5, relief='sunken', font=('arial', 10), wrap='word')
shoppingCartText.pack(padx=6, pady=6)

# 4.1.3 Create a scrollbar for the shopping cart text area
scrollbar = tk.Scrollbar(shoppingCartText, orient='vertical')
scrollbar.pack(side='right', fill='y')

# 4.1.4 Create the text area
textarea = tk.Text(shoppingCartText, height=18, width=75, yscrollcommand=scrollbar.set)
textarea.pack()

# =========================================================================================///
# Buttons = Items cost, Discount, Tax, Delivery Cost, Total Cost, Bill, Email, Print, Clear.
# =========================================================================================\\\


# # Insert buttons in the 
# btn2 = tk.Button(root, text="<<<<<<<<<< RUN SESSION >>>>>>>>>>",
#                  font=('arial', '12', 'bold'), command=lambda: threading.Thread(target=run_session).start()) #threading.Thread(target=run_session).start
# btn2.grid(row=5, pady=12, column=0, columnspan=4)

# 4.1.5 Configure scrollbar to respond to textarea vertical view/action
scrollbar.config(command=textarea.yview)





root.mainloop()