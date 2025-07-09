from tkinter import *
from tkinter import messagebox
import random, os, tempfile, smtplib

from datetime import datetime


root = Tk()
billnumber = random.randint(1000, 9999)  #   Generate a random bill numberd

#send emai# clear button:
# l function
def clear():
    # Cosmetic section
    product1_1_entry.delete(0, END)
    product1_1_entry.insert(0, "0")

    facecreamEntry.delete(0, END)
    facecreamEntry.insert(0, "0")

    facewashEntry.delete(0, END)
    facewashEntry.insert(0, "0")

    hairgelEntry.delete(0, END)
    hairgelEntry.insert(0, "0")

    hairsprayEntry.delete(0, END)
    hairsprayEntry.insert(0, "0")

    bodylotionEntry.delete(0, END)
    bodylotionEntry.insert(0, "0")

    # Grocery section
    ricesEntry.delete(0, END)
    ricesEntry.insert(0, "0")

    oilEntry.delete(0, END)
    oilEntry.insert(0, "0")

    daalEntry.delete(0, END)
    daalEntry.insert(0, "0")

    wheatEntry.delete(0, END)
    wheatEntry.insert(0, "0")

    sugarEntry.delete(0, END)
    sugarEntry.insert(0, "0")

    teaEntry.delete(0, END)
    teaEntry.insert(0, "0")

    # Cold drink section
    cokeEntry.delete(0, END)
    cokeEntry.insert(0, "0")

    pepsiEntry.delete(0, END)
    pepsiEntry.insert(0, "0")

    fantaEntry.delete(0, END)
    fantaEntry.insert(0, "0")

    spriteEntry.delete(0, END)
    spriteEntry.insert(0, "0")

    mozzaEntry.delete(0, END)
    mozzaEntry.insert(0, "0")

    lemonTwistEntry.delete(0, END)
    lemonTwistEntry.insert(0, "0")

    # Price and Tax fields
    cosmeticpriceEntry.delete(0, END)
    grocerypriceEntry.delete(0, END)
    coldrinkpriceEntry.delete(0, END)

    cosmeticstaxEntry.delete(0, END)
    grocerytaxEntry.delete(0, END)
    coldrinktaxEntry.delete(0, END)

    # Customer details
    nameEntry.delete(0, END)
    phoneEntry.delete(0, END)
    BillNumberEntry.delete(0, END)

    # Bill area
    textarea.delete(1.0, END)



#send email 


def send_email():

    def send_gmail():
       try:
           ob = smtplib.SMTP('smtp.gmail.com',587)
           ob.starttls()
           ob.login(senderEntry.get(), passwordrEntry.get())
           message = email_textarea.get(1.0,END)
           ob.sendmail(senderEntry.get(), recieverEntry.get(),message)
           ob.quit()
           messagebox.showinfo('Success', 'Bill is successful', parent=root1)
           root1.destroy()

       except:
           messagebox.showerror('Error', "Something went wrong , Please try again", parent =root1)

           
    if textarea.get(1.0,END)=='\n':
        messagebox.showerror('Error', 'No Bill Found')
    else:
        root1 = Toplevel()
        root1.grab_set()
        root1.title('send gmail')
        root1.config(bg= "lightblue")
        root1.resizable(0,0)
        

        senderFrame= LabelFrame(root1,
                                text= 'SENDER',
                                font=('arial', 16, 'bold'),
                                fg= 'white',
                                bg = 'blue',
                                padx=40,
                                pady=20,

                              )
        senderFrame.grid(row=0, column=0)


        senderLable =Label(senderFrame,text ="Sender's Email", 
                            font = ('arial', 14, 'bold'),
                            fg= 'white',
                            bg = 'blue',
                            pady=8,
                            padx=10,
                            )
        
        senderLable.grid(row =0, column=0)

        senderEntry =Entry(senderFrame,
                           font=('arial',14,'bold'),
                           bd=2,
                           width=23,
                           relief=RIDGE)
                            
        senderEntry.grid(row=0, column=1)
            
        passwordLable =Label(senderFrame,text ="Password", 
                            font = ('arial', 14, 'bold'),
                            fg= 'white',
                            bg = 'blue',
                            pady=8,
                            padx=10,
                            )
        
        passwordLable.grid(row =1, column=0)

        passwordrEntry =Entry(senderFrame,
                           font=('arial',14,'bold'),
                           bd=2,
                           width=23,
                           relief=RIDGE,
                           show='*')
                            
        passwordrEntry.grid(row=1, column=1)

        # recipinent 
        recipientFrame= LabelFrame(root1,
                                text= 'RECIPIENT',
                                font=('arial', 16, 'bold'),
                                fg= 'white',
                                bg = 'blue',
                                padx=40,
                                pady=20,
                                

                              )
        recipientFrame.grid(row=1, column=0, padx =10, pady=20)



        recieverLable =Label(recipientFrame,text ="Email Address", 
                            font = ('arial', 14, 'bold'),
                            fg= 'white',
                            bg = 'blue',
                            pady=8,
                            padx=10,
                            )
        
        recieverLable.grid(row =0, column=0)

        recieverEntry =Entry(recipientFrame,
                           font=('arial',14,'bold'),
                           bd=2,
                           width=23,
                           relief=RIDGE)
                     
        recieverEntry.grid(row=0, column=1)
            
        messageLabel = Label(recipientFrame,
                             text ='Message',
                             font=('arial',14,'bold'),
                             bg='lightblue',
                             fg="blue"
                             )
        
        messageLabel.grid(row=1, column=0, padx=10, pady=8)
            
        
        email_textarea = Text(recipientFrame,
                              font=('arial', 14, 'bold'),
                              bd=2,
                              relief=SUNKEN,
                              width=42,
                              height=11

                              )
        
        email_textarea.grid(row=2,column=0 , columnspan=2)
        email_textarea.delete(1.0, END)
        email_textarea.insert(END,textarea.get(1.0, END).replace('-',""))



        sendButton=Button(root1,
                          text='SEND',
                          font=('arial', 16, 'bold'),
                          command=send_gmail,
                          )
        sendButton.grid(row=2, column=0, pady=20)
        

        root1.mainloop()

# Function to print the bill

def print_bill():
    """Print the bill content from the textarea."""
    if textarea.get(1.0, END) == "\n":
        messagebox.showerror("Error", "No bill to print")
    else:
        try:
            with tempfile.NamedTemporaryFile(delete=False, suffix=".txt", mode='w', encoding='utf-8') as temp_file:
                temp_file.write(textarea.get(1.0, END))
                temp_file_path = temp_file.name

            os.startfile(temp_file_path, "print")
            messagebox.showinfo("Success", "Bill sent to printer")

        except Exception as e:
            messagebox.showerror("Print Error", str(e))


         

# Function for searching and printing a bill

def search_bill():
     global billnumber
     for i in os.listdir('bills'):
            if i.split('_')[1].split('.')[0] == BillNumberEntry.get():
              f = open(f'bills/{i}', 'r')
              textarea.delete(1.0, END)
              for data in f:
                   textarea.insert(END, data)
              f.close()
              break
     else:
            messagebox.showerror("Error", "Bill not found")


def save_bill():
    """Save the bill content to a text file inside the 'bills' folder."""
    global billnumber
    result = messagebox.askyesno("Save Bill", "Do you want to save the bill?")
    if result:
        # Ensure the 'bills' folder exists
        if not os.path.exists("bills"):
            os.makedirs("bills")

        bill_content = textarea.get(1.0, END)
        filename = f"bills/bill_{billnumber}.txt"
        with open(filename, "w") as file:
            file.write(bill_content)

        messagebox.showinfo("Success", f"Bill saved as {filename}")
        billnumber = random.randint(1000, 9999)  # Reset bill number for next bill





# Function to calculate total
def total():
    global bathvalue, facecreamvalue, facewashvalue, hairsprayvalue, hairgelvalue, bodylotionvalue
    global ricevalue, daalvalue, oilvalue, wheatvalue, sugarvalue
    global cokevalue, pepsivalue, spritevalue, fantavalue, lemontwistvalue
    bathvalue = int(bathsoapEntry.get()) * 10
    facecreamvalue = int(facecreamEntry.get()) * 25
    facewashvalue = int(facewashEntry.get()) * 15
    hairsprayvalue = int(hairsprayEntry.get()) * 20
    hairgelvalue = int(hairgelEntry.get()) * 20
    bodylotionvalue = int(bodylotionEntry.get()) * 28
    
    totalcosmetic = (bathvalue + facecreamvalue + facewashvalue +
                     hairsprayvalue + hairgelvalue + bodylotionvalue)
    cosmeticpriceEntry.delete(0, END)  # Clear previous entry
    cosmeticpriceEntry.insert(0, f"R {totalcosmetic}")
    

    #grocery price calcuate

    ricevalue = int(ricesEntry.get()) * 40
    daalvalue = int(daalEntry.get()) * 50
    oilvalue = int(oilEntry.get()) * 80
    wheatvalue = int(wheatEntry.get()) * 30
    sugarvalue = int(sugarEntry.get()) * 20

    totalgrocery = (ricevalue + daalvalue + oilvalue + wheatvalue + sugarvalue)
    grocerypriceEntry.delete(0, END)  # Clear previous entry
    grocerypriceEntry.insert(0, f"R {totalgrocery}")

    
   #cold drink price calculate
    cokevalue = int(cokeEntry.get()) * 15
    pepsivalue = int(pepsiEntry.get()) * 15
    spritevalue = int(spriteEntry.get()) * 15
    fantavalue = int(fantaEntry.get()) * 15
    lemontwistvalue = int(lemonTwistEntry.get()) * 15

    totalcoldrink = (cokevalue + pepsivalue + spritevalue + fantavalue + lemontwistvalue)
    coldrinkpriceEntry.delete(0, END)  # Clear previous entry
    coldrinkpriceEntry.insert(0, f"R {totalcoldrink}")
      # Calculate taxes
    global cosmeticstax
    cosmeticstax = totalcosmetic * 0.15  # 15% tax
    global grocerytax
    grocerytax = totalgrocery * 0.15  # 15% tax
    global coldrinktax
    coldrinktax = totalcoldrink * 0.15  # 15% tax

    # Display taxes
    cosmeticstaxEntry.delete(0, END)
    cosmeticstaxEntry.insert(0, f"R {cosmeticstax}")
      # Update grocery tax 

    grocerytaxEntry.delete(0, END)
    grocerytaxEntry.insert(0, f"R {grocerytax}")
      # Update cold drink tax

    coldrinktaxEntry.delete(0, END)
    coldrinktaxEntry.insert(0, f"R {coldrinktax}")





def bill_area():
    if nameEntry.get() == "" or phoneEntry.get() == "":
        messagebox.showerror("Error", "Customer details are required")
        return

    if (cosmeticpriceEntry.get() == "" or
        grocerypriceEntry.get() == "" or
        coldrinkpriceEntry.get() == ""):
        messagebox.showerror("Error", "No product selected")
        return

    if (cosmeticpriceEntry.get() == "R 0" and
        grocerypriceEntry.get() == "R 0" and
        coldrinkpriceEntry.get() == "R 0"):
        messagebox.showerror("Error", "No product selected")
        return

    now = datetime.now()
    date_str = now.strftime("%Y-%m-%d %H:%M:%S")

    textarea.delete(1.0, END)
    textarea.insert(END, f"{'Welcome ' + nameEntry.get():^85}\n")
    textarea.insert(END, f"{'Date: ' + date_str:^85}\n")
    textarea.insert(END, "-" * 85 + "\n")
    textarea.insert(END, f"Bill Number: {billnumber}\n")
    textarea.insert(END, f"Customer Name: {nameEntry.get()}\n")
    textarea.insert(END, f"Phone Number: {phoneEntry.get()}\n")
    textarea.insert(END, "-" * 85 + "\n")
    textarea.insert(END, f"{'Product':<50}{'Qty':>10}{'Price':>25}\n")
    textarea.insert(END, "-" * 85 + "\n")

    # Products and their entries
    items = [
        ("Bath Soap", bathsoapEntry, 10),
        ("Face Cream", facecreamEntry, 25),
        ("Face Wash", facewashEntry, 15),
        ("Hairspray", hairsprayEntry, 30),
        ("Hair Gel", hairgelEntry, 25),
        ("Body Lotion", bodylotionEntry, 20),
        ("Rice", ricesEntry, 40),
        ("Daal", daalEntry, 50),
        ("Oil", oilEntry, 80),
        ("Wheat", wheatEntry, 30),
        ("Sugar", sugarEntry, 20),
        ("Coke", cokeEntry, 25),
        ("Pepsi", pepsiEntry, 25),
        ("Sprite", spriteEntry, 20),
        ("Fanta", fantaEntry, 20),
        ("Mountain Dew", lemonTwistEntry, 30)
    ]

    for name, entry, unit_price in items:
        qty = int(entry.get())
        if qty > 0:
            total_price = qty * unit_price
            textarea.insert(END, f"{name:50}{qty:>10}{('R ' + str(total_price)):>25}\n")

    textarea.insert(END, "-" * 85 + "\n")

    total = (
        bathvalue + facecreamvalue + facewashvalue + hairsprayvalue +
        hairgelvalue + bodylotionvalue + ricevalue + daalvalue +
        oilvalue + wheatvalue + sugarvalue + cokevalue + pepsivalue +
        spritevalue + fantavalue + lemontwistvalue
    )

    # Tax and totals
    total_tax = cosmeticstax + grocerytax + coldrinktax
    totalbill = total + total_tax

    textarea.insert(END, f"{'Total Price:':<60}{'R ' + format(total, '.2f'):>25}\n")
    textarea.insert(END, f"{'Total Tax:':<60}{'R ' + format(total_tax, '.2f'):>25}\n")
    textarea.insert(END, f"{'Total Bill + Tax:':<60}{'R ' + format(totalbill, '.2f'):>25}\n")
    textarea.insert(END, "-" * 85 + "\n")

    save_bill()





root.title("Grocery Cart")
root.geometry("1270x685")
root.iconbitmap("billing.ico")

headingLabel = Label(root, 
                     text="Grocery Billing System",
                     font=("times new roman", 30, "bold"),
                     bg="lightblue", 
                     fg="black",
                     bd=12,
                     relief=RIDGE,
                     )
headingLabel.pack(fill=X, pady=10)

customer_details_frame = LabelFrame(root,
                                    text="Customer Details",
                                    font=("times new roman", 15, "bold"),
                                    fg="black",
                                    bg="lightblue",
                                    bd=8,
                                    relief=RIDGE)

# Filled row and added padding
customer_details_frame.pack(fill=X, padx=10, pady=5)

# Make columns expand evenly
#for i in range(7):
 #   customer_details_frame.grid_columnconfigure(i, weight=1)

nameLabel = Label(customer_details_frame,
                  text="Name",
                  font=("times new roman", 15, "bold"),
                  fg="blue",
                  bg="lightblue",
                  )
nameLabel.grid(row=0, column=0, padx=20, pady=8)

nameEntry = Entry(customer_details_frame,
                  font=("arial", 15),
                  bd=5,
                  width=18)
nameEntry.grid(row=0, column=1, padx=8, sticky="we")

phoneLabel = Label(customer_details_frame,
                   text="Phone",
                   font=("times new roman", 15, "bold"),
                   fg="blue",
                   bg="lightblue",
                   )
phoneLabel.grid(row=0, column=2, padx=20, pady=8)

phoneEntry = Entry(customer_details_frame,
                   font=("arial", 15),
                   bd=5,
                   width=18)
phoneEntry.grid(row=0, column=3, padx=8, sticky="we")

BillNumberLabel = Label(customer_details_frame,
                        text="Bill Number",
                        font=("times new roman", 15, "bold"),
                        fg="blue",
                        bg="lightblue",
                        )
BillNumberLabel.grid(row=0, column=4, padx=20, pady=8)

BillNumberEntry = Entry(customer_details_frame,
                        font=("arial", 15),
                        bd=5,
                        width=18)
BillNumberEntry.grid(row=0, column=5, padx=8, sticky="we")

searchButton = Button(customer_details_frame,
                      text="SEARCH",
                      font=("arial", 12, "bold"),
                      bd=5,
                      relief=RAISED,
                      padx=20,
                      command=search_bill,
                      )

searchButton.grid(row=0, column=6, padx=20, pady=2)



# Product frame
productsFrame = Frame(root)
productsFrame.pack(pady=10)

cosmeticsFrame = LabelFrame(productsFrame,
                            text='Cosmetics',
                            font=("times new roman", 15, "bold"),
                            fg='black',
                            bg='lightblue',
                            bd=8,
                            relief=RIDGE)
cosmeticsFrame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

# Bath Soap Label
bathsoapLabel = Label(cosmeticsFrame,
                      text="Bath Soap",
                      font=("times new roman", 15, "bold"),
                      fg="blue",
                      bg="lightblue")
bathsoapLabel.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

# Bath Soap Entry
bathsoapEntry = Entry(cosmeticsFrame,
                      font=("arial", 15, "bold"),
                      bd=5,
                      width=10)
bathsoapEntry.grid(row=0, column=1)
bathsoapEntry.insert(0, "0")  # Default value

facecreamLabel = Label(cosmeticsFrame,
                       text="Face Cream",
                       font=("times new roman", 15, "bold"),
                       fg="blue",
                       bg="lightblue")
facecreamLabel.grid(row=1, column=0, pady=10, sticky="nsew")

facecreamEntry = Entry(cosmeticsFrame,
                       font=("arial", 15, "bold"),
                       bd=5,
                       width=10)
facecreamEntry.grid(row=1, column=1)
facecreamEntry.insert(0, "0")  # Default value

facewashLabel = Label(cosmeticsFrame,
                      text="Face Wash",
                      font=("times new roman", 15, "bold"),
                      fg="blue",
                      bg="lightblue")
facewashLabel.grid(row=2, column=0, pady=10, sticky="nsew")

facewashEntry = Entry(cosmeticsFrame,
                      font=("arial", 15, "bold"),
                      bd=5,
                      width=10)
facewashEntry.grid(row=2, column=1)
facewashEntry.insert(0, "0")  # Default value

hairsprayLabel = Label(cosmeticsFrame,
                       text="Hair Spray",
                       font=("times new roman", 15, "bold"),
                       fg="blue",
                       bg="lightblue")
hairsprayLabel.grid(row=3, column=0, pady=10, sticky="nsew")

hairsprayEntry = Entry(cosmeticsFrame,
                       font=("arial", 15, "bold"),
                       bd=5,
                       width=10)
hairsprayEntry.grid(row=3, column=1)
hairsprayEntry.insert(0, "0")  # Default value

hairgelLabel = Label(cosmeticsFrame,
                     text="Hair Gel",
                     font=("times new roman", 15, "bold"),
                     fg="blue",
                     bg="lightblue")
hairgelLabel.grid(row=4, column=0, pady=10, sticky="nsew")

hairgelEntry = Entry(cosmeticsFrame,
                     font=("arial", 15, "bold"),
                     bd=5,
                     width=10)
hairgelEntry.grid(row=4, column=1)
hairgelEntry.insert(0, "0")  # Default value


bodylotionLabel = Label(cosmeticsFrame,
                        text="Body Lotion",
                        font=("times new roman", 15, "bold"),
                        fg="blue",
                        bg="lightblue")
bodylotionLabel.grid(row=5, column=0, pady=10, sticky="nsew")

bodylotionEntry = Entry(cosmeticsFrame,
                        font=("arial", 15, "bold"),
                        bd=5,
                        width=10)
bodylotionEntry.grid(row=5, column=1)
bodylotionEntry.insert(0, "0")  # Default value

# Grocery Frame
groceryFrame = LabelFrame(productsFrame,
                          text='Grocery',
                          font=("times new roman", 15, "bold"),
                          fg='black',
                          bg='lightblue',
                          bd=8,
                          relief=RIDGE)
groceryFrame.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

ricesLabel = Label(groceryFrame,
                   text="Rice",
                   font=("times new roman", 15, "bold"),
                   fg="blue",
                   bg="lightblue")
ricesLabel.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

ricesEntry = Entry(groceryFrame,
                   font=("arial", 15, "bold"),
                   bd=5,
                   width=10)
ricesEntry.grid(row=0, column=1)
ricesEntry.insert(0, "0")  # Default value

oilLabel = Label(groceryFrame,
                 text="Oil",
                 font=("times new roman", 15, "bold"),
                 fg="blue",
                 bg="lightblue")
oilLabel.grid(row=1, column=0, pady=10, sticky="nsew")

oilEntry = Entry(groceryFrame,
                 font=("arial", 15, "bold"),
                 bd=5,
                 width=10)
oilEntry.grid(row=1, column=1,)
oilEntry.insert(0, "0")  # Default value

daalLabel = Label(groceryFrame,
                  text="Daal",
                  font=("times new roman", 15, "bold"),
                  fg="blue",
                  bg="lightblue")
daalLabel.grid(row=2, column=0, pady=10, sticky="nsew")

daalEntry = Entry(groceryFrame,
                  font=("arial", 15, "bold"),
                  bd=5,
                  width=10)
daalEntry.grid(row=2, column=1,)
daalEntry.insert(0, "0")  # Default value

wheatLabel = Label(groceryFrame,
                   text="Wheat",
                   font=("times new roman", 15, "bold"),
                   fg="blue",
                   bg="lightblue")
wheatLabel.grid(row=3, column=0, pady=10, sticky="nsew")

wheatEntry = Entry(groceryFrame,
                   font=("arial", 15, "bold"),
                   bd=5,
                   width=10)
wheatEntry.grid(row=3, column=1,)
wheatEntry.insert(0, "0")  # Default value

sugarLabel = Label(groceryFrame,
                   text="Sugar",
                   font=("times new roman", 15, "bold"),
                   fg="blue",
                   bg="lightblue")
sugarLabel.grid(row=4, column=0, pady=10, sticky="nsew")

sugarEntry = Entry(groceryFrame,
                   font=("arial", 15, "bold"),
                   bd=5,
                   width=10)
sugarEntry.grid(row=4, column=1,)
sugarEntry.insert(0, "0")  # Default value

teaLabel = Label(groceryFrame,
                 text="Tea",
                 font=("times new roman", 15, "bold"),
                 fg="blue",
                 bg="lightblue")
teaLabel.grid(row=5, column=0, pady=10, sticky="nsew")

teaEntry = Entry(groceryFrame,
                 font=("arial", 15, "bold"),
                 bd=5,
                 width=10)
teaEntry.grid(row=5, column=1,)
teaEntry.insert(0, "0")  # Default value

# Drinks Frame
drinksFrame = LabelFrame(productsFrame,
                         text='Drinks',
                         font=("times new roman", 15, "bold"),
                         fg='black',
                         bg='lightblue',
                         bd=10,
                         relief=RIDGE)
drinksFrame.grid(row=0, column=2, padx=10, pady=10, sticky="nsew")

cokeLabel = Label(drinksFrame,
                  text="Coke",
                  font=("times new roman", 15, "bold"),
                  fg="blue",
                  bg="lightblue")
cokeLabel.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

cokeEntry = Entry(drinksFrame,
                  font=("arial", 15, "bold"),
                  bd=5,
                  width=10)
cokeEntry.grid(row=0, column=1,)
cokeEntry.insert(0, "0")  # Default value

pepsiLabel = Label(drinksFrame,
                   text="Pepsi",
                   font=("times new roman", 15, "bold"),
                   fg="blue",
                   bg="lightblue")
pepsiLabel.grid(row=1, column=0,pady=10, sticky="nsew")

pepsiEntry = Entry(drinksFrame,
                   font=("arial", 15, "bold"),
                   bd=5,
                   width=10)
pepsiEntry.grid(row=1, column=1,)
pepsiEntry.insert(0, "0")  # Default value

spriteLabel = Label(drinksFrame,
                    text="Sprite",
                    font=("times new roman", 15, "bold"),
                    fg="blue",
                    bg="lightblue")
spriteLabel.grid(row=2, column=0, pady=10, sticky="nsew")

spriteEntry = Entry(drinksFrame,
                    font=("arial", 15, "bold"),
                    bd=5,
                    width=10)
spriteEntry.grid(row=2, column=1,)
spriteEntry.insert(0, "0")  # Default value

fantaLabel = Label(drinksFrame,
                   text="Fanta",
                   font=("times new roman", 15, "bold"),
                   fg="blue",
                   bg="lightblue")
fantaLabel.grid(row=3, column=0, pady=10,sticky="nsew")

fantaEntry = Entry(drinksFrame,
                   font=("arial", 15, "bold"),
                   bd=5,
                   width=10)
fantaEntry.grid(row=3, column=1,)
fantaEntry.insert(0, "0")  # Default value

mozzaLabel = Label(drinksFrame,
                   text="Mooza",
                   font=("times new roman", 15, "bold"),
                   fg="blue",
                   bg="lightblue")
mozzaLabel.grid(row=4, column=0, pady=10,sticky="nsew")

mozzaEntry = Entry(drinksFrame,
                   font=("arial", 15, "bold"),
                   bd=5,
                   width=10
                )
mozzaEntry.grid(row=4, column=1, )
mozzaEntry.insert(0, "0")  # Default value

lemonTwistLabel = Label(drinksFrame,
                        text="Lemon Twist",
                        font=("times new roman", 15, "bold"),
                        fg="blue",
                        bg="lightblue")
lemonTwistLabel.grid(row=5, column=0,pady=10, sticky="nsew")

lemonTwistEntry = Entry(drinksFrame,
                        font=("arial", 15, "bold"),
                        bd=5,
                        width=10)
lemonTwistEntry.grid(row=5, column=1,)
lemonTwistEntry.insert(0, "0")  # Default value

# Bill Frame
billframe = Frame(productsFrame)
billframe.grid(row=0, column=3, padx=10, pady=10, sticky="nsew")

billareaLabel = Label(billframe,
                      text="Bill Area",
                      font=("times new roman", 15, "bold"),
                      fg="black",
                      bg="lightblue",
                      bd=8,
                      relief=RIDGE,
                      pady=5)
billareaLabel.pack(fill=X)

Scrollbar= Scrollbar(billframe,orient=VERTICAL)
Scrollbar.pack(side=RIGHT, fill=Y)

textarea = Text(billframe,
                font=("arial", 15),
                width=55,
                height=12,
                pady=5)
textarea.pack()

Scrollbar.config(command=textarea.yview)
textarea.config(yscrollcommand=Scrollbar.set)



#billmenue
billmenuFrame = LabelFrame(root,
                          text="Bill Menu", 
                            font=("times new roman", 15, "bold"),
                            fg="black",
                            bg="lightblue",
                            bd=8,
                            relief=RIDGE,
                            pady=5)
billmenuFrame.pack(fill=X)

#cosmetic price 

cosmeticpriceLabel = Label(billmenuFrame,
                     text="Cosmetic Price",
                     font=("times new roman", 12, "bold"),
                     fg="blue",
                     bg="lightblue")
cosmeticpriceLabel.grid(row=0, column=0, padx=9, pady=10, sticky="w")

cosmeticpriceEntry = Entry(billmenuFrame,
                     font=("arial", 12, "bold"),
                     bd=5,
                     width=10)
cosmeticpriceEntry.grid(row=0, column=1, padx=9, pady=10)

#grocery price
grocerypriceLabel = Label(billmenuFrame,
                          text="Grocery Price",
                          font=("times new roman", 12, "bold"),
                          fg="blue",
                          bg="lightblue")

grocerypriceLabel.grid(row=1, column=0, padx=9, pady=10, sticky="w")

grocerypriceEntry = Entry(billmenuFrame,
                          font=("arial", 12, "bold"),
                          bd=5,
                          width=10)

grocerypriceEntry.grid(row=1, column=1, padx=9, pady=10)

#colddrink price

coldrinkpriceLabel = Label(billmenuFrame,
                          text="Cold Drink Price",
                          font=("times new roman", 12, "bold"),
                          fg="blue",
                          bg="lightblue")

coldrinkpriceLabel.grid(row=2, column=0, padx=9, pady=10, sticky="w")

coldrinkpriceEntry = Entry(billmenuFrame,
                          font=("arial", 12, "bold"),
                          bd=5,
                          width=10)

coldrinkpriceEntry.grid(row=2, column=1, padx=9, pady=10)

#tax  price

cosmeticstax = Label(billmenuFrame,
                     text="Cosmetic Tax",
                     font=("times new roman", 12, "bold"),
                     fg="blue",
                     bg="lightblue")

cosmeticstax.grid(row=0, column=3, padx=9, pady=10, sticky="w")

cosmeticstaxEntry = Entry(billmenuFrame,
                          font=("arial", 12, "bold"),
                          bd=5,
                          width=10)

cosmeticstaxEntry.grid(row=0, column=4, padx=9, pady=10)



#grocery tax

grocerytaxLabel = Label(billmenuFrame,
                        text="Grocery Tax",
                        font=("times new roman", 12, "bold"),
                        fg="blue",
                        bg="lightblue")
grocerytaxLabel.grid(row=1, column=3, padx=9, pady=10, sticky="w")

grocerytaxEntry = Entry(billmenuFrame,
                        font=("arial", 12, "bold"),
                        bd=5,
                        width=10)
grocerytaxEntry.grid(row=1, column=4, padx=9, pady=10)



#coldrink tax


coldrinktaxLabel = Label(billmenuFrame,
                         text="Cold Drink Tax",
                            font=("times new roman", 12, "bold"),
                            fg="blue",
                            bg="lightblue")
coldrinktaxLabel.grid(row=2, column=3, padx=9, pady=10, sticky="w")

coldrinktaxEntry = Entry(billmenuFrame,
                         font=("arial", 12, "bold"),
                         bd=5,
                         width=10)

coldrinktaxEntry.grid(row=2, column=4, padx=9, pady=10)


# === Button Frame for Total and Bill ===
buttonFrame = LabelFrame(billmenuFrame,
                         bd=8,
                         relief=RIDGE,)
buttonFrame.grid(row=0, column=5, columnspan=3)

# Total Button
totalButton = Button(buttonFrame,
                     text="Total",
                     font=("arial", 16, "bold"),
                     bd=5,
                     relief=RAISED,
                     padx=20,
                     pady=5,
                     width=8, 
                     command=total)
totalButton.grid(row=0, column=0, padx=20, pady=5)

# Bill Button
billButton = Button(buttonFrame,
                    text="Bill",
                    font=("arial", 16, "bold"),
                    bd=5,
                    padx=10,
                    width=8,
                    command=bill_area,
                    )
billButton.grid(row=0, column=1, padx=20, pady=5)


#email button 

emailButton = Button(buttonFrame,
                     text="Email",
                        font=("arial", 16, "bold"),
                        bd=5,
                        padx=10,
                        width=8, command=send_email)
emailButton.grid(row=0, column=2, padx=20, pady=5)



# print button


printButton = Button(buttonFrame,
                     text="Print",
                        font=("arial", 16, "bold"),
                        bd=5,                   
                        padx=10,
                        width=8, 
                        command=print_bill)
printButton.grid(row=0, column=3, padx=20, pady=5)

# clear button

clearbutton = Button(buttonFrame,
                     text="Clear",
                        font=("arial", 16, "bold"),
                        bd=5,
                        padx=10,
                        width=8,
                        command= clear )

clearbutton.grid(row=0, column=4, padx=20, pady=5)
