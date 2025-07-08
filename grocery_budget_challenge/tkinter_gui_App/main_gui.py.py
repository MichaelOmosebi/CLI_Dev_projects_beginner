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
import customtkinter as ctk
from tkcalendar import Calendar
import pandas as pd
from tkcalendar import DateEntry
from tkinter import messagebox

import ttkbootstrap as ttk
from ttkbootstrap.constants import *

# importing in-built packages
# >>>>>>>
# >>>>>>>
# >>>>>>>

# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
root = ttk.Window(themename="solar")
root.title("LAGOS MEGA MART 🛒") #App Title/Name
# root.iconbitmap(default='grocery_bag.ico')

logo_image = tk.PhotoImage(file = 'grocery_bag.png')
root.iconphoto(False, logo_image)

# setting window width and height
root.geometry('1400x800')
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
customer_details_label.grid(row=0, column=0, padx=4, pady=2)

# 2.1.1 Create entry field for shopper name
customernameEntry = tk.Entry(customer_details_frame, text='', font=('arial', 10), width=22, bd=5, relief='sunken')
#usernameEntry.insert(tk.END, 'xxxxx@mail.com')
customernameEntry.grid(row=0, column=1, pady=9, padx=4, columnspan=1)

# 2.2.0 Create a Label for shopper email
shopperName_label = tk.Label(customer_details_frame, text='Email: ', font=('times new roman', 12, 'bold'), background='gray30', foreground='white')
shopperName_label.grid(row=0, column=2, padx=4, pady=2)

# 2.2.1 Create entry field for shopper email
shopperNameEntry = tk.Entry(customer_details_frame, font=('arial', 10), width=26, bd=5)
shopperNameEntry.grid(row=0, column=3, pady=9, padx=6, columnspan=1)

# 2.2.2 Create a Label for shopper phone
shopperPhone_label = tk.Label(customer_details_frame, text='Mobile No.: ', font=('times new roman', 10, 'bold'), background='gray30', foreground='white')
shopperPhone_label.grid(row=0, column=4, padx=4, pady=2)

# 2.2.3 Create entry field for shopper phone
shopperPhone_Entry = tk.Entry(customer_details_frame, font=('arial', 10), width=16, bd=5)
shopperPhone_Entry.grid(row=0, column=5, pady=9, padx=6, columnspan=1)

# 2.2.4 Create a Label to search for tickets
ticketSearch_label = tk.Label(customer_details_frame, text='Voucher Number: ', font=('times new roman', 10, 'bold'), background='gray30', foreground='white')
ticketSearch_label.grid(row=0, column=6, padx=6, pady=2)

# 2.2.5 Create a button to activate the search for tickets
ticketSearch_button = tk.Button(customer_details_frame, text='Search', font=('arial', 10, 'bold'), width=8, bd=5, relief='ridge', bg='steelblue', fg='white')
ticketSearch_button.grid(row=0, column=8, pady=9, padx=4, columnspan=1) 

# 2.2.5 Create entry field to search for tickets
ticketSearch_Entry = tk.Entry(customer_details_frame, font=('arial', 10), width=16, bd=5, relief='sunken', bg='white')
ticketSearch_Entry.grid(row=0, column=7, pady=9, padx=2, columnspan=1)

#3.0 Create a Frame that houses the Product Catalogue inside the App root
shoppingDetails = tk.Frame(root, bd=8, relief='flat', width=35, background='white')
shoppingDetails.pack(fill=tk.X)
# product_catalogue_frame.grid(row=1, column=0, padx=6, pady=6, sticky='w')

# # 3.1 Create a section for the product catalogue/shopping selection --- PRODUCTS CATALOGUE
productSelection_frame = tk.LabelFrame(shoppingDetails, text='', font=('times new roman', 12, 'bold'), background='gray30', foreground='white', relief='flat')
productSelection_frame.grid(row=0, column=0, padx=6, pady=2)

# 3.1.0 Create a Frame for the product sections
productionSection_frame = tk.Frame(productSelection_frame, bd=8, relief='raised', width=35, background='gray30')
productionSection_frame.pack(fill=tk.X)#.grid(row=0, column=0, padx=6, pady=2)

# 3.1.1 Create a Label for the first product section
productSection1_label = tk.LabelFrame(productionSection_frame, text='Drinks', font=('times new roman', 13, 'bold'), width=18, bd=7, relief='groove')
productSection1_label.grid(row=0, column=0, padx=6, pady=2, sticky='n')

# 3.1.2 Create a Label and entry field for the first product
product1_1_label = tk.Label(productSection1_label, text='Coca Cola ', font=('times new roman', 12, 'bold'), background='gray30', fg='white')
product1_1_label.grid(row=0, column=0, padx=6, pady=4, sticky='w')

product1_1_entry = tk.Entry(productSection1_label, font=('arial', 10), width=5, bd=5)
product1_1_entry.grid(row=0, column=1, padx=10, pady=8)

# 3.1.3 Create a Label and entry field for the second product
product2_1_label = tk.Label(productSection1_label, text='Fanta ', font=('times new roman', 12, 'bold'), background='gray30', foreground='white')
product2_1_label.grid(row=1, column=0, padx=6, pady=4, sticky='w')

product2_1_entry = tk.Entry(productSection1_label, font=('arial', 10), width=5, bd=5)
product2_1_entry.grid(row=1, column=1, padx=10, pady=8)

# 3.1.4 Create a Label and entry field for the third product
product3_1_label = tk.Label(productSection1_label, text='Pepsi ', font=('times new roman', 12, 'bold'), background='gray30', foreground='white')
product3_1_label.grid(row=2, column=0, padx=6, pady=4, sticky='w')

product3_1_entry = tk.Entry(productSection1_label, font=('arial', 10), width=5, bd=5)
product3_1_entry.grid(row=2, column=1, padx=10, pady=8)

# 3.1.5 Create a Label and entry field for the fourth product
product4_1_label = tk.Label(productSection1_label, text='Mountain Dew ', font=('times new roman', 12, 'bold'), background='gray30', foreground='white')
product4_1_label.grid(row=3, column=0, padx=6, pady=4, sticky='w')

product4_1_entry = tk.Entry(productSection1_label, font=('arial', 10), width=5, bd=5)
product4_1_entry.grid(row=3, column=1, padx=10, pady=8)

# 3.1.6 Create a Label and entry field for the fifth product
product5_1_label = tk.Label(productSection1_label, text='Sprite ', font=('times new roman', 12, 'bold'), background='gray30', foreground='white')
product5_1_label.grid(row=4, column=0, padx=6, pady=4, sticky='w')

product5_1_entry = tk.Entry(productSection1_label, font=('arial', 10), width=5, bd=5)
product5_1_entry.grid(row=4, column=1, padx=10, pady=8)

# 3.1.7 Create a Label and entry field for the sixth product
product6_1_label = tk.Label(productSection1_label, text='Dúdú ', font=('times new roman', 12, 'bold'), background='gray30', foreground='white')
product6_1_label.grid(row=5, column=0, padx=6, pady=4, sticky='w')

product6_1_entry = tk.Entry(productSection1_label, font=('arial', 10), width=5, bd=5)
product6_1_entry.grid(row=5, column=1, padx=10, pady=8)

# 3.1.8 Create a Label and entry field for the seventh product
product7_1_label = tk.Label(productSection1_label, text='Zobo ', font=('times new roman', 12, 'bold'), background='gray30', foreground='white')
product7_1_label.grid(row=6, column=0, padx=6, pady=4, sticky='w')

product7_1_entry = tk.Entry(productSection1_label, font=('arial', 10), width=5, bd=5)
product7_1_entry.grid(row=6, column=1, padx=10, pady=8)

# 3.1.9 Create a Label and entry field for the eighth product
product8_1_label = tk.Label(productSection1_label, text='Tigernut Drink ', font=('times new roman', 12, 'bold'), background='gray30', foreground='white')
product8_1_label.grid(row=7, column=0, padx=6, pady=4, sticky='w')

product8_1_entry = tk.Entry(productSection1_label, font=('arial', 10), width=5, bd=5)
product8_1_entry.grid(row=7, column=1, padx=10, pady=8)

# 3.2.0 Create a Label for the second product section
productSection2_label = tk.LabelFrame(productionSection_frame, text='Fruits', font=('times new roman', 13, 'bold'), width=18, bd=7, relief='groove')
productSection2_label.grid(row=0, column=1, padx=6, pady=2, sticky='n')

# 3.2.1 Create a Label and entry field for the first product
product1_2_label = tk.Label(productSection2_label, text='Apples ', font=('times new roman', 12, 'bold'), background='gray30', foreground='white')
product1_2_label.grid(row=0, column=0, padx=6, pady=4, sticky='w')
product1_2_entry = tk.Entry(productSection2_label, font=('arial', 10), width=5, bd=5)
product1_2_entry.grid(row=0, column=1, padx=10, pady=8)

# 3.2.2 Create a Label and entry field for the second product
product2_2_label = tk.Label(productSection2_label, text='Apricots ', font=('times new roman', 12, 'bold'), background='gray30', foreground='white')
product2_2_label.grid(row=1, column=0, padx=6, pady=4, sticky='w')
product2_2_entry = tk.Entry(productSection2_label, font=('arial', 10), width=5, bd=5)
product2_2_entry.grid(row=1, column=1, padx=10, pady=8)

# 3.2.3 Create a Label and entry field for the third product
product3_2_label = tk.Label(productSection2_label, text='Avocados ', font=('times new roman', 12, 'bold'), background='gray30', foreground='white')
product3_2_label.grid(row=2, column=0, padx=6, pady=4, sticky='w')
product3_2_entry = tk.Entry(productSection2_label, font=('arial', 10), width=5, bd=5)
product3_2_entry.grid(row=2, column=1, padx=10, pady=8)

# 3.2.4 Create a Label and entry field for the fourth product
product4_2_label = tk.Label(productSection2_label, text='Water Melon ', font=('times new roman', 12, 'bold'), background='gray30', foreground='white')
product4_2_label.grid(row=3, column=0, padx=6, pady=4, sticky='w')
product4_2_entry = tk.Entry(productSection2_label, font=('arial', 10), width=5, bd=5)
product4_2_entry.grid(row=3, column=1, padx=10, pady=8)

# 3.2.5 Create a Label and entry field for the fifth product
product5_2_label = tk.Label(productSection2_label, text='Oranges ', font=('times new roman', 12, 'bold'), background='gray30', foreground='white')
product5_2_label.grid(row=4, column=0, padx=6, pady=4, sticky='w')
product5_2_entry = tk.Entry(productSection2_label, font=('arial', 10), width=5, bd=5)
product5_2_entry.grid(row=4, column=1, padx=10, pady=8)

# 3.2.6 Create a Label and entry field for the sixth product
product6_2_label = tk.Label(productSection2_label, text='Bananas ', font=('times new roman', 12, 'bold'), background='gray30', foreground='white')
product6_2_label.grid(row=5, column=0, padx=6, pady=4, sticky='w')
product6_2_entry = tk.Entry(productSection2_label, font=('arial', 10), width=5, bd=5)
product6_2_entry.grid(row=5, column=1, padx=10, pady=8)

# 3.2.7 Create a Label and entry field for the seventh product
product7_2_label = tk.Label(productSection2_label, text='Pineapples ', font=('times new roman', 12, 'bold'), background='gray30', foreground='white')
product7_2_label.grid(row=6, column=0, padx=6, pady=4, sticky='w')
product7_2_entry = tk.Entry(productSection2_label, font=('arial', 10), width=5, bd=5)
product7_2_entry.grid(row=6, column=1, padx=10, pady=8)

# 3.2.8 Create a Label and entry field for the eighth product
product8_2_label = tk.Label(productSection2_label, text='Carrots ', font=('times new roman', 12, 'bold'), background='gray30', foreground='white')
product8_2_label.grid(row=7, column=0, padx=6, pady=4, sticky='w')
product8_2_entry = tk.Entry(productSection2_label, font=('arial', 10), width=5, bd=5)
product8_2_entry.grid(row=7, column=1, padx=10, pady=8)

# 3.3.0 Create a Label for the third product section
productSection3_label = tk.LabelFrame(productionSection_frame, text='Snacks', font=('times new roman', 13, 'bold'), width=18, bd=7, relief='groove')
productSection3_label.grid(row=0, column=2, padx=6, pady=2, sticky='n')

# 3.3.1 Create a Label and entry field for the first product in section 3
product1_3_label = tk.Label(productSection3_label, text='Crackers ', font=('times new roman', 12, 'bold'), background='gray30', foreground='white')
product1_3_label.grid(row=0, column=0, padx=6, pady=4, sticky='w')
product1_3_entry = tk.Entry(productSection3_label, font=('arial', 10), width=5, bd=5)
product1_3_entry.grid(row=0, column=1, padx=10, pady=8)

# 3.3.2 Create a Label and entry field for the second product in section 3
product2_3_label = tk.Label(productSection3_label, text='Kúlí Kúlí ', font=('times new roman', 12, 'bold'), background='gray30', foreground='white')
product2_3_label.grid(row=1, column=0, padx=6, pady=4, sticky='w')
product2_3_entry = tk.Entry(productSection3_label, font=('arial', 10), width=5, bd=5)
product2_3_entry.grid(row=1, column=1, padx=10, pady=8)

# 3.3.3 Create a Label and entry field for the third product in section 3
product3_3_label = tk.Label(productSection3_label, text='Pop Corn ', font=('times new roman', 12, 'bold'), background='gray30', foreground='white')
product3_3_label.grid(row=2, column=0, padx=6, pady=4, sticky='w')
product3_3_entry = tk.Entry(productSection3_label, font=('arial', 10), width=5, bd=5)
product3_3_entry.grid(row=2, column=1, padx=10, pady=8)

# 3.3.4 Create a Label and entry field for the fourth product in section 3
product4_3_label = tk.Label(productSection3_label, text='Crackers ', font=('times new roman', 12, 'bold'), background='gray30', foreground='white')
product4_3_label.grid(row=3, column=0, padx=6, pady=4, sticky='w')
product4_3_entry = tk.Entry(productSection3_label, font=('arial', 10), width=5, bd=5)
product4_3_entry.grid(row=3, column=1, padx=10, pady=8)

# 3.3.5 Create a Label and entry field for the fifth product in section 3
product5_3_label = tk.Label(productSection3_label, text='Wafers ', font=('times new roman', 12, 'bold'), background='gray30', foreground='white')
product5_3_label.grid(row=4, column=0, padx=6, pady=4, sticky='w')
product5_3_entry = tk.Entry(productSection3_label, font=('arial', 10), width=5, bd=5)
product5_3_entry.grid(row=4, column=1, padx=10, pady=8)

# 3.3.6 Create a Label and entry field for the sixth product in section 3
product6_3_label = tk.Label(productSection3_label, text='Chin-chin ', font=('times new roman', 12, 'bold'), background='gray30', foreground='white')
product6_3_label.grid(row=5, column=0, padx=6, pady=4, sticky='w')
product6_3_entry = tk.Entry(productSection3_label, font=('arial', 10), width=5, bd=5)
product6_3_entry.grid(row=5, column=1, padx=10, pady=8)

# 3.3.7 Create a Label and entry field for the seventh product in section 3
product7_3_label = tk.Label(productSection3_label, text='Peanut ', font=('times new roman', 12, 'bold'), background='gray30', foreground='white')
product7_3_label.grid(row=6, column=0, padx=6, pady=4, sticky='w')
product7_3_entry = tk.Entry(productSection3_label, font=('arial', 10), width=5, bd=5)
product7_3_entry.grid(row=6, column=1, padx=10, pady=8)

# 3.3.7 Create a Label and entry field for the eighth product in section 3
product8_3_label = tk.Label(productSection3_label, text='Pringles ', font=('times new roman', 12, 'bold'), background='gray30', foreground='white')
product8_3_label.grid(row=7, column=0, padx=6, pady=4, sticky='w')
product8_3_entry = tk.Entry(productSection3_label, font=('arial', 10), width=5, bd=5)
product8_3_entry.grid(row=7, column=1, padx=10, pady=8)

# # 3.4.1 Create a Label for the fourth product section
# productSection4_label = tk.LabelFrame(productionSection_frame, text='House Keeping', font=('times new roman', 13, 'bold'), width=15, bd=7, relief='groove')
# productSection4_label.grid(row=0, column=3, padx=6, pady=2, columnspan=2, sticky='n')

# # 3.4.2 Create a Label and entry field for the first product in section 4
# product1_4_label = tk.Label(productSection4_label, text='Mop Bucket: ', font=('times new roman', 12, 'bold'), background='gray30', foreground='white')
# product1_4_label.grid(row=1, column=0, padx=6, pady=4, sticky='w')
# product1_4_entry = tk.Entry(productSection4_label, font=('arial', 10), width=5, bd=5)
# product1_4_entry.grid(row=1, column=1, padx=10, pady=8)

# # 3.4.3 Create a Label and entry field for the second product in section 4
# product2_4_label = tk.Label(productSection4_label, text='Mop Stick: ', font=('times new roman', 12, 'bold'), background='gray30', foreground='white')
# product2_4_label.grid(row=2, column=0, padx=6, pady=4, sticky='w')
# product2_4_entry = tk.Entry(productSection4_label, font=('arial', 10), width=5, bd=5)
# product2_4_entry.grid(row=2, column=1, padx=10, pady=8)

# # 3.4.4 Create a Label and entry field for the third product in section 4
# product3_4_label = tk.Label(productSection4_label, text='Brooms: ', font=('times new roman', 12, 'bold'), background='gray30', foreground='white')
# product3_4_label.grid(row=3, column=0, padx=6, pady=4, sticky='w')
# product3_4_entry = tk.Entry(productSection4_label, font=('arial', 10), width=5, bd=5)
# product3_4_entry.grid(row=3, column=1, padx=10, pady=8)

# # 3.4.5 Create a Label and entry field for the fourth product in section 4
# product4_4_label = tk.Label(productSection4_label, text='Detergent: ', font=('times new roman', 12, 'bold'), background='gray30', foreground='white')
# product4_4_label.grid(row=4, column=0, padx=6, pady=4, sticky='w')
# product4_4_entry = tk.Entry(productSection4_label, font=('arial', 10), width=5, bd=5)
# product4_4_entry.grid(row=4, column=1, padx=10, pady=8)

# # 3.4.6 Create a Label and entry field for the fifth product in section 4
# product5_4_label = tk.Label(productSection4_label, text='Antiseptic: ', font=('times new roman', 12, 'bold'), background='gray30', foreground='white')
# product5_4_label.grid(row=5, column=0, padx=6, pady=4, sticky='w')
# product5_4_entry = tk.Entry(productSection4_label, font=('arial', 10), width=5, bd=5)
# product5_4_entry.grid(row=5, column=1, padx=10, pady=8)

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

# 5.0 Create Section for a Smart Graphic of a strolling Cart
customerCheckout_frame = tk.LabelFrame(root, text='', font=('times new roman', 13, 'bold'), fg='steelblue', background='gray30', border=8, relief='sunken')
customerCheckout_frame.configure(height=50)
customerCheckout_frame.pack(fill=tk.X)

customerCheckout_Label = tk.Label(customerCheckout_frame, text='🛒 \t 🛒 \t 🛒 \t 🛒 \t 🛒 \t 🛒 \t 🛒 \t 🛒 \t 🛒 \t 🛒 \t 🛒 \t 🛒 \t 🛒 \t 🛒 \t 🛒 \t 🛒',
                                  font=('calibri', 15), bd=10, justify='center')
customerCheckout_Label.pack(fill=tk.X)

# 6.0 Create a Frame that houses the buttons for the shopping cart
buttons_frame = tk.Frame(root, bd=8, relief='flat', width=35, background='gray30', highlightbackground='gray30', highlightthickness=4)
buttons_frame.pack(fill=tk.X)

# 6.0.1 Create a Label for the buttons section
buttonsDescription = tk.LabelFrame(buttons_frame, text='Checkout Details / Actions', font=('arial', 13, 'bold'), width=48, bd=7)
buttonsDescription.grid(row=0, column=0, padx=6, pady=2)

# 6.1.0 Create Labels and entry fields for the checkout actions
itemsCost_Label = tk.Label(buttonsDescription, text='Items Cost', font=('arial', 10, 'bold'), width=14)
itemsCost_Label.grid(row=0, column=0, padx=6, pady=2, sticky='w')

itemsCost_Entry = tk.Entry(buttonsDescription, font=('arial', 10), width=10)
itemsCost_Entry.grid(row=0, column=1, padx=6, pady=2, sticky='w')

# 6.1.1 Create Labels and entry fields for the discount
discount_Label = tk.Label(buttonsDescription, text='Discount', font=('arial', 10, 'bold'), width=14)
discount_Label.grid(row=1, column=0, padx=6, pady=2, sticky='w')

discount_Entry = tk.Entry(buttonsDescription, font=('arial', 10), width=10)
discount_Entry.grid(row=1, column=1, padx=6, pady=2, sticky='w')

# # 6.1.2 Create Labels and entry fields for the tax
tax_Label = tk.Label(buttonsDescription, text='Tax', font=('arial', 10, 'bold'), width=14)
tax_Label.grid(row=0, column=2, padx=6, pady=2, sticky='w')

tax_Entry = tk.Entry(buttonsDescription, font=('arial', 10), width=10)
tax_Entry.grid(row=0, column=3, padx=6, pady=2, sticky='w')

# 6.1.3 Create Labels and entry fields for the delivery cost
deliveryCost_Label = tk.Label(buttonsDescription, text='Delivery Cost', font=('arial', 10, 'bold'), width=14)
deliveryCost_Label.grid(row=1, column=2, padx=6, pady=2, sticky='w')

deliveryCost_Entry = tk.Entry(buttonsDescription, font=('arial', 10), width=10)
deliveryCost_Entry.grid(row=1, column=3, padx=6, pady=2, sticky='w')

# 6.2 Create a Frame to hold the buttons for the checkout actions
checkoutActions = tk.Frame(buttonsDescription, bd=8, relief='sunken', width=35, height=10, background='gray30', highlightbackground='gray30', highlightthickness=4)
checkoutActions.grid(row=0, column=4, columnspan=4, rowspan=2, padx=6, pady=2)

# 6.2.1 Add buttons to checkout actions frame
btn_total = tk.Button(checkoutActions, text='Total', font=('arial', 12, 'bold'), command=lambda: print("Total"), width=10)
btn_total.grid(row=0, column=0, padx=13, pady=9)

btn_bill = tk.Button(checkoutActions, text='Bill', font=('arial', 12, 'bold'), command=lambda: print("Bill"), width=10)
btn_bill.grid(row=0, column=1, padx=13, pady=9)

btn_email = tk.Button(checkoutActions, text='Email', font=('arial', 12, 'bold'), command=lambda: print("Email"), width=10)
btn_email.grid(row=0, column=2, padx=13, pady=9)

btn_print = tk.Button(checkoutActions, text='Print', font=('arial', 12, 'bold'), command=lambda: print("Print"), width=10)
btn_print.grid(row=0, column=3, padx=13, pady=9)

btn_clear = tk.Button(checkoutActions, text='Clear', font=('arial', 12, 'bold'), command=lambda: print("Clear"), width=10)
btn_clear.grid(row=0, column=4, padx=13, pady=9)


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