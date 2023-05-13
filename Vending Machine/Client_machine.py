from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import pickle
import matplotlib.pyplot as plt
import socket

# Create client socket.

Host = '127.0.0.1'
Port = 65432

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


client.connect((Host, Port))


#  This function will quit the welcome window.
def menu_():
    window.destroy()


# This function will disable the exit button.
def not_close():
    pass


# Welcome window.

window = Tk()
window.geometry("700x400")
window.title("Welcome")
window.protocol('WM_DELETE_WINDOW', not_close)  # Disable exit button.
bg_image1 = Image.open("Images/welcome.jpg")  # Adding background image.
bg_image1 = bg_image1.resize((700, 400))
bg_image1 = ImageTk.PhotoImage(bg_image1)
label_bg_image = Label(window, image=bg_image1)
label_bg_image.place(x=0, y=0)
window.configure(bg="black")

# Welcome message.

message = Label(window, text="WELCOME", bg="black", fg="lightblue", font=('Times New Roman', 20, 'bold'))
message.place(x=60, y=5)
message1 = Label(window, text="This vending machine", bg="black", fg="lightblue",
                 font=('Times New Roman', 20, 'italic'))
message1.place(x=20, y=55)
message2 = Label(window, text="will provide you with", bg="black", fg="lightblue",
                 font=('Times New Roman', 20, 'italic'))
message2.place(x=20, y=105)
message3 = Label(window, text="some snacks and drinks.", bg="black", fg="lightblue",
                 font=('Times New Roman', 20, 'italic'))
message3.place(x=10, y=155)
message4 = Label(window, text="Hope the products", bg="black", fg="lightblue", font=('Times New Roman', 20, 'italic'))
message4.place(x=30, y=205)
message5 = Label(window, text="will be good for you.", bg="black", fg="lightblue",
                 font=('Times New Roman', 20, 'italic'))
message5.place(x=30, y=255)
# Button which will make the user access the vending machine.
menu_button = Button(window, text="Go to menu", width=30, height=2, bg="black", fg="lightblue",
                     font=('Times New Roman', 11, 'bold'), command=menu_)
menu_button.place(x=25, y=330)
window.mainloop()

# Taking data from the csv file stock.

with open('stock.csv', 'r') as file:
    stock = file.readlines()  # Read all the data from the file.
    c = 0
    stock_list = []  # Creating a list which will store all the information about each product.

    # Make the stock_list become a 2D list.
    for a in stock:
        list1 = stock[c].split(",")
        stock_list.append(list1)
        c = c + 1

    for h in range(len(stock_list)):
        stock_list[h][3] = stock_list[h][3].replace('\n', "")  # Removing all the \n in the list.

    # Creating 4 different lists.
    id_list = []
    name_list = []
    price_list = []
    # Taking data from the stock_list and add them to the 3 list.
    # For example all the productID from the stock_list will be added to the id_list.
    # This will be used for the receipt of the user.
    for i in range(len(stock_list)):
        id_list.append(stock_list[i][0])
        name_list.append(stock_list[i][1])
        price_list.append(stock_list[i][2])

    # Creating a list which will have the quantity of each product.
    # This list will be used for the spin box widget.
    quantity_list = []
    # Declaring 12 different variables which will based on the quantity of a product.
    # For example, quantity_num1 will represent the number of Coca Cola left.
    quantity_num1 = 0
    # This for loop will get the quantity of the product Coca Cola.
    for n in range(len(name_list)):
        if name_list[n] in "Coca Cola":
            quantity_num1 = quantity_num1 + 1
    # This one will add the quantity of the product different times.
    # For example, if the quantity of Coca Cola is 10, it will add it 10 times in order to represent the 10 products.
    # with his right quantity.
    for v in range(quantity_num1):
        quantity_list.append(quantity_num1)

    # The same thing will be applicable for the remaining products.

    quantity_num2 = 0
    for n in range(len(name_list)):
        if name_list[n] in "Fanta":
            quantity_num2 = quantity_num2 + 1
    for v in range(quantity_num2):
        quantity_list.append(quantity_num2)

    quantity_num3 = 0
    for n in range(len(name_list)):
        if name_list[n] in "Pepsi":
            quantity_num3 = quantity_num3 + 1
    for v in range(quantity_num3):
        quantity_list.append(quantity_num3)

    quantity_num4 = 0
    for n in range(len(name_list)):
        if name_list[n] in "Sprite":
            quantity_num4 = quantity_num4 + 1
    for v in range(quantity_num4):
        quantity_list.append(quantity_num4)

    quantity_num5 = 0
    for n in range(len(name_list)):
        if name_list[n] in "Water":
            quantity_num5 = quantity_num5 + 1
    for v in range(quantity_num5):
        quantity_list.append(quantity_num5)

    quantity_num6 = 0
    for n in range(len(name_list)):
        if name_list[n] in "Doritos Chili":
            quantity_num6 = quantity_num6 + 1
    for v in range(quantity_num6):
        quantity_list.append(quantity_num6)

    quantity_num7 = 0
    for n in range(len(name_list)):
        if name_list[n] in "Doritos Salted":
            quantity_num7 = quantity_num7 + 1
    for v in range(quantity_num7):
        quantity_list.append(quantity_num7)

    quantity_num8 = 0
    for n in range(len(name_list)):
        if name_list[n] in "Doritos Cheese":
            quantity_num8 = quantity_num8 + 1
    for v in range(quantity_num8):
        quantity_list.append(quantity_num8)

    quantity_num9 = 0
    for n in range(len(name_list)):
        if name_list[n] in "Lays Classic":
            quantity_num9 = quantity_num9 + 1
    for v in range(quantity_num9):
        quantity_list.append(quantity_num9)

    quantity_num10 = 0
    for n in range(len(name_list)):
        if name_list[n] in "Lays Barbecue":
            quantity_num10 = quantity_num10 + 1
    for v in range(quantity_num10):
        quantity_list.append(quantity_num10)

    quantity_num11 = 0
    for n in range(len(name_list)):
        if name_list[n] in "Lays Masala":
            quantity_num11 = quantity_num11 + 1
    for v in range(quantity_num11):
        quantity_list.append(quantity_num11)

    quantity_num12 = 0
    for n in range(len(name_list)):
        if name_list[n] in "Kit Kat":
            quantity_num12 = quantity_num12 + 1
    for v in range(quantity_num12):
        quantity_list.append(quantity_num12)

    # Add the name of each product in a list.
    product = ["Coca Cola", "Fanta", "Pepsi", "Sprite", "Water", "Doritos Chili", "Doritos Salted", "Doritos Cheese",
               "Lays Classic", "Lays Barbecue", "Lays Masala", "Kitkat"]
    # Add the quantity of each product in a list as well.
    productnum_available = [quantity_num1, quantity_num2, quantity_num3, quantity_num4, quantity_num5, quantity_num6,
                            quantity_num7, quantity_num8, quantity_num9, quantity_num10, quantity_num11, quantity_num12]
    # These 2 lists above will be used for the bar chart.

    product_num = -1
    coca_num = -1
    fanta_num = -1
    pepsi_num = -1
    sprite_num = -1
    water_num = -1
    D_cheese_num = -1
    D_chili_num = -1
    D_salted_num = -1
    L_barbecue_num = -1
    L_masala_num = -1
    L_classic_num = -1
    kitkat_num = -1

    for d in range(len(name_list)):
        if name_list[d] in "Coca Cola":
            product_num = product_num + 1
            coca_num = product_num

        if name_list[d] in "Fanta":
            product_num = product_num + 1
            fanta_num = product_num

        if name_list[d] in "Pepsi":
            product_num = product_num + 1
            pepsi_num = product_num

        if name_list[d] in "Sprite":
            product_num = product_num + 1
            sprite_num = product_num

        if name_list[d] in "Water":
            product_num = product_num + 1
            water_num = product_num

        if name_list[d] in "Doritos Chili":
            product_num = product_num + 1
            D_chili_num = product_num

        if name_list[d] in "Doritos Salted":
            product_num = product_num + 1
            D_salted_num = product_num

        if name_list[d] in "Doritos Cheese":
            product_num = product_num + 1
            D_cheese_num = product_num

        if name_list[d] in "Lays Classic":
            product_num = product_num + 1
            L_classic_num = product_num

        if name_list[d] in "Lays Barbecue":
            product_num = product_num + 1
            L_barbecue_num = product_num

        if name_list[d] in "Lays Masala":
            product_num = product_num + 1
            L_masala_num = product_num

        if name_list[d] in "Kit Kat":
            product_num = product_num + 1
            kitkat_num = product_num

    # This list will have the name, price and quantity of the product which will be used for the receipt.
    add_list = []
    # This one will be used to found the total price.
    total_list = []
    # Declaring the variable total_price.
    total_price = -1
    b = 0
    j = 0


# This function will be call whenever the user click on the exit button.
def exit_():
    # It will ask the user if want to exit or not.
    # If the user click on yes the variable answer1 will be equal to "yes".
    answer1 = messagebox.askquestion("Exit", "Are you sure you want to exit?")
    # It will quit the menu interface and another interface will pop with a goodbye message.
    if answer1 == "yes":
        window1.destroy()
        window7 = Tk()
        window7.title("Exit")
        window7.geometry("700x400")
        window7.resizable(width=False, height=False)
        bg_image3 = Image.open("Images/blueblock.jpg")
        bg_image3 = bg_image3.resize((700, 400))
        bg_image3 = ImageTk.PhotoImage(bg_image3)
        label_bg_image2 = Label(window7, image=bg_image3)
        label_bg_image2.place(x=0, y=0)
        message12 = Label(window7, text="Sorry", bg="black", fg="lightblue",
                          font=('Times New Roman', 20, 'italic'))
        message12.place(x=120, y=20)
        message13 = Label(window7, text="we could not provide", bg="black", fg="lightblue",
                          font=('Times New Roman', 20, 'italic'))
        message13.place(x=40, y=70)
        message14 = Label(window7, text="you with your choice today.", bg="black", fg="lightblue",
                          font=('Times New Roman', 20, 'italic'))
        message14.place(x=10, y=120)
        message15 = Label(window7, text="We hope to", bg="black", fg="lightblue",
                          font=('Times New Roman', 20, 'italic'))
        message15.place(x=100, y=170)
        message16 = Label(window7, text="see you soon again.", bg="black", fg="lightblue",
                          font=('Times New Roman', 20, 'italic'))
        message16.place(x=60, y=220)
        message17 = Label(window7, text="Have a good day!", bg="black", fg="lightblue",
                          font=('Times New Roman', 20, 'italic'))
        message17.place(x=70, y=270)
        message18 = Label(window7, text="All the best.", bg="black", fg="lightblue",
                          font=('Times New Roman', 20, 'italic'))
        message18.place(x=100, y=320)

        gb_photo2 = Image.open('Images/goodbye.jpg')
        gb_photo2 = gb_photo2.resize((300, 300))
        gb_photo2 = ImageTk.PhotoImage(gb_photo2)
        label_photo_gb2 = Label(image=gb_photo2)
        label_photo_gb2.place(x=350, y=50)

        window7.mainloop()


# This function will be call whenever the user click on the shop now button.
# It will give the user an entry to enter the code of the product he/she want to purchase.
def shop():
    # The function display will contain the code entered by the user in the argument entry.
    # It will be used to call an interface which will contain the information about the chosen product.
    def display(entry):
        # This function will be call if the right code is entered and also if the product code entered is not out of
        # stock.
        def product_():
            # It will quit the interface where to enter the code.
            window2.destroy()

            # This function will be call whenever the user click on the add to cart button.
            def add():
                global j
                # This if statement will make sure that the user do not leave the spin box as 0.
                if spin_box.get() == "0":
                    messagebox.showerror("Error", "You have to select the quantity that you want to buy.")
                else:
                    answer3 = messagebox.askquestion("Exit", "Are you sure you want to add this product to your cart? "
                                                             "You will not be able to delete it")
                    if answer3 == "yes":
                        # This will update the quantity of the spin box.
                        quantity_list[b] = quantity_list[b] - int(spin_box.get())
                        # Then it will add the name, price and quantity of the product to the 2D list add_list
                        # This list will be used in the buy function and also for the transaction.
                        add_list.append([])
                        add_list[j].append(name_list[b])
                        add_list[j].append(price_list[b])
                        add_list[j].append(spin_box.get())
                        j = j + 1
                        # It will tell the user that his/her product has been added to the cart and it will quit the
                        # interface.
                        messagebox.showinfo("", "The product you have selected has been added to the cart")
                        window3.destroy()

            # This function will be call whenever the user click on the cancel button.
            # It will simply quit the interface.
            def cancel():
                window3.destroy()

            # This function will be call whenever the user click on the buy button.
            def buy():
                # This function will be call whenever the user click on the go purchase button.
                def payment():
                    global total_price
                    # It will place the total price in the menu interface.
                    Label_total_price = Label(window1, text=f"Rs {sum(total_list)}", bg="white")
                    Label_total_price.place(x=600, y=550)
                    # assigning the total price to a variable call total_price so that the user can now make the
                    # transaction
                    total_price = sum(total_list)
                    window4.destroy()
                    window3.destroy()

                # This if statement will make sure that the user do not leave the spin box as 0.
                if spin_box.get() == "0":
                    messagebox.showerror("Error", "You have to select how much you want to buy.")
                else:
                    # It will ask the user for a confirmation in case he/she want to keep adding product in his/her
                    # cart.
                    answer2 = messagebox.askquestion("Exit", "Are you sure you want to proceed to the payment? You "
                                                             "will not be able to add another product")
                    # If the user click on yes it will show him/her the receipt of what he/she want to buy.
                    if answer2 == "yes":
                        # It will first update the quantity of the spin box and add the chosen product to the add_list.
                        quantity_list[b] = quantity_list[b] - int(spin_box.get())
                        add_list.append([])
                        add_list[j].append(name_list[b])
                        add_list[j].append(price_list[b])
                        add_list[j].append(spin_box.get())
                        # The interface of the final receipt.
                        window4 = Tk()
                        window4.title("Final Receipt")
                        window4.protocol('WM_DELETE_WINDOW', not_close)
                        receipt_text = Label(window4, text="---------------Receipt---------------")
                        receipt_text.pack()
                        heads = Label(window4, text="Name\t\tPrice\tQuantity")
                        heads.pack()
                        # This for loop will put the name, price and quantity of each product he/she add to the cart.
                        for g in range(len(add_list)):
                            item = Label(window4, text=f'{add_list[g][0]}\t\t{add_list[g][1]}\t{add_list[g][2]}\t')
                            # Put all the price in a list.
                            total_list.append(add_list[g][1])
                            # Multiply each price by his quantity.
                            # Replace the price of each product.
                            total_list[g] = int(total_list[g]) * int(add_list[g][2])
                            item.pack()
                        # Make the sum of all the price in the list to get the total price.
                        total_price_ = Label(window4, text=f'Total Price: {sum(total_list)}')
                        total_price_.pack()
                        paid_button = Button(window4, text="Go Purchase", width=50, bg="black", fg="white",
                                             command=lambda: payment())
                        paid_button.pack()
                        window4.mainloop()

            # This interface will make the user make 3 options.
            window3 = Tk()
            window3.geometry("300x160")
            window3.configure(bg='black')
            window3.title("Product")
            window3.resizable(width=False, height=False)
            # Place the productID of the chosen product.
            item_code = Label(window3, text="Item Code")
            item_code.place(x=30, y=10)
            item_code.configure(bg='black', fg="white")
            item_code_label = Label(window3, text=f"{id_list[b]}")
            item_code_label.place(x=120, y=10, width=135)
            # Place the product name of the chosen product.
            product_name = Label(window3, text="Product Name")
            product_name.place(x=30, y=40)
            product_name.configure(bg='black', fg="white")
            product_name_label = Label(window3, text=f"{name_list[b]}")
            product_name_label.place(x=120, y=40, width=135)
            # Place the product price of the chosen product.
            price = Label(window3, text="Price")
            price.place(x=30, y=70)
            price.configure(bg='black', fg="white")
            product_name_label = Label(window3, text=f"Rs{price_list[b]}")
            product_name_label.place(x=120, y=70, width=135)
            # Place the product quantity of the chosen product.
            quantity = Label(window3, text="Quantity")
            quantity.place(x=30, y=100)
            quantity.configure(bg='black', fg="white")
            spin_box = Spinbox(window3, from_=0, to=quantity_list[b])
            spin_box.place(x=120, y=100)
            # The first option finish and pay.
            finish_button = Button(window3, text="Finish and pay", command=lambda: buy())
            finish_button.place(x=2, y=130, width=100)
            # The second option Add to cart.
            cart_button = Button(window3, text="Add to Cart", command=lambda: add())
            cart_button.place(x=100, y=130, width=100)
            # The third option cancel.
            cancel_button = Button(window3, text="Cancel", command=lambda: cancel())
            cancel_button.place(x=200, y=130, width=100)
            window3.mainloop()

        # The global variable b will be used to check if the product is out of stock and also to get the information of
        # the chosen product.
        global b
        # This if statement will be used to call the function product in which it will show the interface that contain
        # the information of the chosen product. It will also give the user 3 options.
        if entry == "P010":
            b = coca_num
            if b == -1:
                messagebox.showerror("Error", "Sorry, this product is out of stock")
            elif quantity_list[b] == 0:
                messagebox.showerror("Error", "Sorry, this product is out of stock")
            else:
                product_()
        elif entry == "P020":
            b = fanta_num
            if b == -1:
                messagebox.showerror("Error", "Sorry, this product is out of stock")
            elif quantity_list[b] == 0:
                messagebox.showerror("Error", "Sorry, this product is out of stock")
            else:
                product_()
        elif entry == "P030":
            b = pepsi_num
            if b == -1:
                messagebox.showerror("Error", "Sorry, this product is out of stock")
            elif quantity_list[b] == 0:
                messagebox.showerror("Error", "Sorry, this product is out of stock")
            else:
                product_()
        elif entry == "P040":
            b = sprite_num
            if b == -1:
                messagebox.showerror("Error", "Sorry, this product is out of stock")
            elif quantity_list[b] == 0:
                messagebox.showerror("Error", "Sorry, this product is out of stock")
            else:
                product_()
        elif entry == "P050":
            b = water_num
            if b == -1:
                messagebox.showerror("Error", "Sorry, this product is out of stock")
            elif quantity_list[b] == 0:
                messagebox.showerror("Error", "Sorry, this product is out of stock")
            else:
                product_()
        elif entry == "P055":
            b = D_chili_num
            if b == -1:
                messagebox.showerror("Error", "Sorry, this product is out of stock")
            elif quantity_list[b] == 0:
                messagebox.showerror("Error", "Sorry, this product is out of stock")
            else:
                product_()
        elif entry == "P060":
            b = D_salted_num
            if b == -1:
                messagebox.showerror("Error", "Sorry, this product is out of stock")
            elif quantity_list[b] == 0:
                messagebox.showerror("Error", "Sorry, this product is out of stock")
            else:
                product_()
        elif entry == "P065":
            b = D_cheese_num
            if b == -1:
                messagebox.showerror("Error", "Sorry, this product is out of stock")
            elif quantity_list[b] == 0:
                messagebox.showerror("Error", "Sorry, this product is out of stock")
            else:
                product_()
        elif entry == "P075":
            b = L_classic_num
            if b == -1:
                messagebox.showerror("Error", "Sorry, this product is out of stock")
            elif quantity_list[b] == 0:
                messagebox.showerror("Error", "Sorry, this product is out of stock")
            else:
                product_()
        elif entry == "P080":
            b = L_barbecue_num
            if b == -1:
                messagebox.showerror("Error", "Sorry, this product is out of stock")
            elif quantity_list[b] == 0:
                messagebox.showerror("Error", "Sorry, this product is out of stock")
            else:
                product_()
        elif entry == "P085":
            b = L_masala_num
            if b == -1:
                messagebox.showerror("Error", "Sorry, this product is out of stock")
            elif quantity_list[b] == 0:
                messagebox.showerror("Error", "Sorry, this product is out of stock")
            else:
                product_()
        elif entry == "P095":
            b = kitkat_num
            if b == -1:
                messagebox.showerror("Error", "Sorry, this product is out of stock")
            elif quantity_list[b] == 0:
                messagebox.showerror("Error", "Sorry, this product is out of stock")
            else:
                product_()
        else:
            messagebox.showerror("Error", "You have to enter the right code of the product.")

    # If the user has already got his/her total price, he/she will not be able to add another product to his/her cart.
    if total_price > 0:
        messagebox.showerror("Error", "You can't shop again as you have already chosen all the products that you will buy.")
    # If the user has not received his/her total price, he/she can continue to add products to the cart.
    else:
        window2 = Tk()
        window2.title("Enter Code")
        window2.configure(bg="black")
        window2.resizable(width=False, height=False)  # Disable maximise
        # Place entry
        code_entry_text = Label(window2, text="Please enter the code of the product you want to buy ",
                                bg="black", fg="white", font="11")
        code_entry_text.pack()
        code_entry_text1 = Label(window2, text="(You can see the code of each product on the menu interface)",
                                 bg="black", fg="white", font="11")
        code_entry_text1.pack()
        code_entry = Entry(window2, width=59)
        code_entry.pack()
        # code_entry.get() will be the code entered by the user.
        enter_button = Button(window2, text="Enter", width=50, command=lambda: display(code_entry.get()))
        enter_button.pack()
        enter_button.configure(bg="gold")
        window2.mainloop()


# Declaring the variable input_price which will represent the number of money that the user will input.
input_price = 0


# This function will be call whenever the user will click on the purchase button.
def purchase_():
    # It will confirm if the user purchases or not
    answer = messagebox.askquestion("Confirm", "Are you sure you want to purchase?")
    # If the user clicks on yes, the program will try to make the transaction.
    if answer == "yes":

        # if the user input price is equal to his/her total price, it will perform the transaction.
        if input_price == total_price:
            # This will convert the data into a byte stream so that it can be sent to the server.
            data_send = pickle.dumps(add_list)
            client.send(data_send)  # This will send the products that the user purchases to the server
            window1.destroy()  # This will quit the menu.
            # This interface is the goodbye and thank you message to the user.
            window6 = Tk()
            window6.title("Purchase Completed")
            window6.geometry("700x400")
            window6.resizable(width=False, height=False)
            bg_image2 = Image.open("Images/blueblock.jpg")
            bg_image2 = bg_image2.resize((700, 400))
            bg_image2 = ImageTk.PhotoImage(bg_image2)
            label_bg_image1 = Label(window6, image=bg_image2)
            label_bg_image1.place(x=0, y=0)
            message6 = Label(window6, text="Thank you", bg="black", fg="lightblue",
                             font=('Times New Roman', 30, 'italic'))
            message6.place(x=60, y=20)
            message7 = Label(window6, text="for you purchase.", bg="black", fg="lightblue",
                             font=('Times New Roman', 30, 'italic'))
            message7.place(x=10, y=80)
            message8 = Label(window6, text="Hope to see you", bg="black", fg="lightblue",
                             font=('Times New Roman', 30, 'italic'))
            message8.place(x=30, y=140)
            message9 = Label(window6, text="again.", bg="black", fg="lightblue",
                             font=('Times New Roman', 30, 'italic'))
            message9.place(x=100, y=200)
            message10 = Label(window6, text="Goodbye.", bg="black", fg="lightblue",
                              font=('Times New Roman', 30, 'italic'))
            message10.place(x=80, y=260)
            message11 = Label(window6, text="All the best.", bg="black", fg="lightblue",
                              font=('Times New Roman', 30, 'italic'))
            message11.place(x=70, y=320)

            gb_photo = Image.open('Images/goodbye.jpg')
            gb_photo = gb_photo.resize((300, 300))
            gb_photo = ImageTk.PhotoImage(gb_photo)
            label_photo_gb = Label(image=gb_photo)
            label_photo_gb.place(x=350, y=50)
            window6.mainloop()
        # check if the user has got his/her total price.
        elif total_price == -1:
            messagebox.showerror("Error",
                                 "You have to click on the Shop Now button to choose all the products you want "
                                 "to purchase and then you will receive a total price which will appear in the "
                                 "menu. After receiving this total price you will have to input your money."
                                 "Your input price must equal to the total price in order to complete your "
                                 "payment and receive your product(s)")
        # Check if the user input price is equal to/her total price.
        else:
            messagebox.showinfo("Error", "Your input must equal to the total input")


# This function is for the input process.
# It will be called if the user clicks on the note and coin images on the menu.
def money(price):
    global input_price  # Put input_price as global so that it can be changed.

    # This if/elif statement will be used so that the user can input his/her money.
    # For example, if the user clicks on the coin of Rs1, his/her input price will be Rs1, and if he/she clicks another
    # time on the Rs1 coin, his/her input price will be Rs2.

    if price == 1:
        # This label will place the input price on the menu.
        Label_input_price = Label(window1, text=f"Rs {price + input_price}", bg="white", width=8)
        Label_input_price.place(x=600, y=500)
        input_price = input_price + price
    elif price == 5:
        Label_input_price = Label(window1, text=f"Rs {price + input_price}", bg="white", width=8)
        Label_input_price.place(x=600, y=500)
        input_price = input_price + price
    elif price == 10:
        Label_input_price = Label(window1, text=f"Rs {price + input_price}", bg="white", width=8)
        Label_input_price.place(x=600, y=500)
        input_price = input_price + price
    elif price == 20:
        Label_input_price = Label(window1, text=f"Rs {price + input_price}", bg="white", width=8)
        Label_input_price.place(x=600, y=500)
        input_price = input_price + price
    elif price == 25:
        Label_input_price = Label(window1, text=f"Rs {price + input_price}", bg="white", width=8)
        Label_input_price.place(x=600, y=500)
        input_price = input_price + price
    elif price == 50:
        Label_input_price = Label(window1, text=f"Rs {price + input_price}", bg="white", width=8)
        Label_input_price.place(x=600, y=500)
        input_price = input_price + price
    elif price == 100:
        Label_input_price = Label(window1, text=f"Rs {price + input_price}", bg="white", width=8)
        Label_input_price.place(x=600, y=500)
        input_price = input_price + price
    elif price == 200:
        Label_input_price = Label(window1, text=f"Rs {price + input_price}", bg="white", width=8)
        Label_input_price.place(x=600, y=500)
        input_price = input_price + price
    elif price == 500:
        Label_input_price = Label(window1, text=f"Rs {price + input_price}", bg="white", width=8)
        Label_input_price.place(x=600, y=500)
        input_price = input_price + price
    elif price == 1000:
        Label_input_price = Label(window1, text=f"Rs {price + input_price}", bg="white", width=8)
        Label_input_price.place(x=600, y=500)
        input_price = input_price + price
    # This will be perform if the user click on the clear input button.
    # The input price will be set as 0.
    elif price == 0:
        Label_input_price = Label(window1, bg="white", width=8)
        Label_input_price.place(x=600, y=500)
        input_price = 0


# This function will be call if the user clicks on the current stock button.
# It will give the current stock available to the user in the form of a bar chart.
def stock():
    plt.figure(figsize=(20, 8))
    # Creating the bar plot.
    # The list product contains all the names of the products and the list productnum_available contains all
    # the quantity.
    # of each product.
    plt.bar(product[0], productnum_available[0], label='Coca Cola', color='Darkred')
    plt.bar(product[1], productnum_available[1], label='Fanta', color='orange')
    plt.bar(product[2], productnum_available[2], label='Pepsi', color='navy')
    plt.bar(product[3], productnum_available[3], label='Sprite', color='limegreen')
    plt.bar(product[4], productnum_available[4], label='Water', color='silver')
    plt.bar(product[5], productnum_available[5], label='Doritos Chili', color='blue')
    plt.bar(product[6], productnum_available[6], label='Doritos Salted', color='green')
    plt.bar(product[7], productnum_available[7], label='Doritos Cheese', color='coral')
    plt.bar(product[8], productnum_available[8], label='Lays Classic', color='gold')
    plt.bar(product[9], productnum_available[9], label='Lays Barbecue', color='k')
    plt.bar(product[10], productnum_available[10], label='Lays Masala', color='royalblue')
    plt.bar(product[11], productnum_available[11], label='Kitkat', color='red')

    plt.xlabel("Products", fontsize=20)
    plt.ylabel("Quantity", fontsize=20)
    plt.title("Stock Available", fontsize=30)
    # Implement the color scale
    plt.legend()
    plt.show()


# This will be the interface of the menu.
window1 = Tk()
window1.geometry("1175x650")
window1.title("Menu")
window1.protocol('WM_DELETE_WINDOW', not_close)  # Disable close button.
window1.resizable(width=False, height=False)

bg_image = Image.open("Images/Snack drinks.jpg")  # Background image.
bg_image = bg_image.resize((1250, 650))
bg_image = ImageTk.PhotoImage(bg_image)
label1 = Label(window1, image=bg_image)
label1.place(x=0, y=0)

Title = Label(window1, text="Snacks & Drinks", fg="gold", bg="black",
              font=('Times New Roman', 30, 'bold'))
Title.place(x=445, y=10)

# Placing different images, price and name of the products.

text1 = Label(window1, text="Coca Cola", fg="gold", bg="black", width=9,
              font=('Times New Roman', 12))
text13 = Label(window1, text="Rs25", fg="black", bg="gold", width=4,
               font=('Times New Roman', 12))
text1.place(x=30, y=75)
text13.place(x=111, y=75)
photo1 = Image.open('Images/coca.jpeg')
photo1 = photo1.resize((119, 120))
photo1 = ImageTk.PhotoImage(photo1)
label_photo1 = Label(image=photo1)
label_photo1.place(x=30, y=100)
Label2 = Label(window1, text="Code: P010")
Label2.place(width=125, x=30, y=224)
Label2.configure(bg="black", fg="white")

text2 = Label(window1, text="Fanta", fg="gold", bg="black", width=9,
              font=('Times New Roman', 12))
text14 = Label(window1, text="Rs25", fg="black", bg="gold", width=4,
               font=('Times New Roman', 12))
text2.place(x=230, y=75)
text14.place(x=316, y=75)
photo2 = Image.open('Images/Fanta.jpg')
photo2 = photo2.resize((124, 120))
photo2 = ImageTk.PhotoImage(photo2)
label_photo2 = Label(image=photo2)
label_photo2.place(x=230, y=100)
Label3 = Label(window1, text="Code: P020")
Label3.place(width=129, x=230, y=224)
Label3.configure(bg="black", fg="white")

text3 = Label(window1, text="Pepsi", fg="gold", bg="black", width=9,
              font=('Times New Roman', 12))
text15 = Label(window1, text="Rs25", fg="black", bg="gold", width=4,
               font=('Times New Roman', 12))
text3.place(x=430, y=75)
text15.place(x=511, y=75)
photo3 = Image.open('Images/Pepsi.jpg')
photo3 = photo3.resize((119, 120))
photo3 = ImageTk.PhotoImage(photo3)
label_photo3 = Label(image=photo3)
label_photo3.place(x=430, y=100)
Label4 = Label(window1, text="Code: P030")
Label4.place(width=125, x=430, y=224)
Label4.configure(bg="black", fg="white")

text4 = Label(window1, text="Sprite", fg="gold", bg="black", width=9,
              font=('Times New Roman', 12))
text16 = Label(window1, text="Rs25", fg="black", bg="gold", width=4,
               font=('Times New Roman', 12))
text4.place(x=630, y=75)
text16.place(x=715, y=75)
photo4 = Image.open('Images/Sprite.jpg')
photo4 = photo4.resize((123, 120))
photo4 = ImageTk.PhotoImage(photo4)
label_photo4 = Label(image=photo4)
label_photo4.place(x=630, y=100)
Label5 = Label(window1, text="Code: P040")
Label5.place(width=128, x=630, y=224)
Label5.configure(bg="black", fg="white")

text5 = Label(window1, text="Water", fg="gold", bg="black", width=9,
              font=('Times New Roman', 12))
text17 = Label(window1, text="Rs20", fg="black", bg="gold", width=4,
               font=('Times New Roman', 12))
text5.place(x=830, y=75)
text17.place(x=911, y=75)
photo5 = Image.open('Images/Water.jpg')
photo5 = photo5.resize((119, 120))
photo5 = ImageTk.PhotoImage(photo5)
label_photo5 = Label(image=photo5)
label_photo5.place(x=830, y=100)
Label6 = Label(window1, text="Code: P050")
Label6.place(width=125, x=830, y=224)
Label6.configure(bg="black", fg="white")

text6 = Label(window1, text="Doritos Chili", fg="gold", bg="black", width=8,
              font=('Times New Roman', 12))
text18 = Label(window1, text="Rs15", fg="black", bg="gold", width=4,
               font=('Times New Roman', 12))
text6.place(x=1030, y=75)
text18.place(x=1111, y=75)
photo6 = Image.open('Images/Doritos Blue.jpg')
photo6 = photo6.resize((119, 120))
photo6 = ImageTk.PhotoImage(photo6)
label_photo6 = Label(image=photo6)
label_photo6.place(x=1030, y=100)
Label7 = Label(window1, text="Code: P055")
Label7.place(width=125, x=1030, y=224)
Label7.configure(bg="black", fg="white")

text7 = Label(window1, text="Doritos Salted", fg="gold", bg="black", width=9,
              font=('Times New Roman', 12))
text19 = Label(window1, text="Rs15", fg="black", bg="gold", width=3,
               font=('Times New Roman', 12))
text7.place(x=30, y=285)
text19.place(x=120, y=285)
photo7 = Image.open('Images/Doritos Green.jpg')
photo7 = photo7.resize((119, 120))
photo7 = ImageTk.PhotoImage(photo7)
label_photo7 = Label(image=photo7)
label_photo7.place(x=30, y=310)
Label8 = Label(window1, text="Code: P060")
Label8.place(width=125, x=30, y=434)
Label8.configure(bg="black", fg="white")

text8 = Label(window1, text="Doritos Cheese", fg="gold", bg="black", width=10,
              font=('Times New Roman', 12))
text20 = Label(window1, text="Rs15", fg="black", bg="gold", width=3,
               font=('Times New Roman', 12))
text8.place(x=230, y=285)
text20.place(x=326, y=285)
photo8 = Image.open('Images/Doritos Orange.jpg')
photo8 = photo8.resize((125, 120))
photo8 = ImageTk.PhotoImage(photo8)
label_photo8 = Label(image=photo8)
label_photo8.place(x=230, y=310)
Label9 = Label(window1, text="Code: P065")
Label9.place(width=129, x=230, y=434)
Label9.configure(bg="black", fg="white")

text9 = Label(window1, text="Lays Classic", fg="gold", bg="black", width=10,
              font=('Times New Roman', 12))
text21 = Label(window1, text="Rs12", fg="black", bg="gold", width=3,
               font=('Times New Roman', 12))
text9.place(x=430, y=285)
text21.place(x=520, y=285)
photo9 = Image.open('Images/Lays Yellow.png')
photo9 = photo9.resize((119, 120))
photo9 = ImageTk.PhotoImage(photo9)
label_photo9 = Label(image=photo9)
label_photo9.place(x=430, y=310)
Label10 = Label(window1, text="Code: P075")
Label10.place(width=125, x=430, y=434)
Label10.configure(bg="black", fg="white")

text10 = Label(window1, text="Lays Barbecue", fg="gold", bg="black", width=10,
               font=('Times New Roman', 12))
text22 = Label(window1, text="Rs12", fg="black", bg="gold", width=3,
               font=('Times New Roman', 12))
text10.place(x=630, y=285)
text22.place(x=725, y=285)
photo10 = Image.open('Images/Lays Black.jpg')
photo10 = photo10.resize((124, 120))
photo10 = ImageTk.PhotoImage(photo10)
label_photo10 = Label(image=photo10)
label_photo10.place(x=630, y=310)
Label11 = Label(window1, text="Code: P080")
Label11.place(width=128, x=630, y=434)
Label11.configure(bg="black", fg="white")

text11 = Label(window1, text="Lays Masala", fg="gold", bg="black", width=10,
               font=('Times New Roman', 12))
text23 = Label(window1, text="Rs12", fg="black", bg="gold", width=3,
               font=('Times New Roman', 12))
text11.place(x=830, y=285)
text23.place(x=920, y=285)
photo11 = Image.open('Images/Lays Blue.png')
photo11 = photo11.resize((119, 120))
photo11 = ImageTk.PhotoImage(photo11)
label_photo11 = Label(image=photo11)
label_photo11.place(x=830, y=310)
Label12 = Label(window1, text="Code: P085")
Label12.place(width=125, x=830, y=434)
Label12.configure(bg="black", fg="white")

text12 = Label(window1, text="Kit Kat", fg="gold", bg="black", width=9,
               font=('Times New Roman', 12))
text24 = Label(window1, text="Rs35", fg="black", bg="gold", width=4,
               font=('Times New Roman', 12))
text12.place(x=1030, y=285)
text24.place(x=1111, y=285)
photo12 = Image.open('Images/Kit Kat.jpg')
photo12 = photo12.resize((119, 120))
photo12 = ImageTk.PhotoImage(photo12)
label_photo12 = Label(image=photo12)
label_photo12.place(x=1030, y=310)
Label13 = Label(window1, text="Code: P095")
Label13.place(width=125, x=1030, y=434)
Label13.configure(bg="black", fg="white")

bg_payment = Label(window1, width=1250, height=20, bg="black")
bg_payment.place(x=3, y=487)

text_input_money = Label(window1, text="Please input your money:", bg="black", fg="white",
                         font=('Times New Roman', 20, 'bold'))
text_input_money.place(x=4, y=490)

# Placing button images of coins and notes.

photo_1 = Image.open('Images/1.jpg')
photo_1 = photo_1.resize((50, 50))
photo_1 = ImageTk.PhotoImage(photo_1)
label_photo_1 = Label(image=photo_1)
button_1 = Button(window1, image=photo_1, command=lambda: money(1))
button_1.place(x=3, y=535)

photo_5 = Image.open('Images/5.jpg')
photo_5 = photo_5.resize((50, 50))
photo_5 = ImageTk.PhotoImage(photo_5)
label_photo_5 = Label(image=photo_5)
button_5 = Button(window1, image=photo_5, command=lambda: money(5))
button_5.place(x=55, y=535)

photo_10 = Image.open('Images/10.jpg')
photo_10 = photo_10.resize((50, 50))
photo_10 = ImageTk.PhotoImage(photo_10)
label_photo_10 = Label(image=photo_10)
button_10 = Button(window1, image=photo_10, command=lambda: money(10))
button_10.place(x=107, y=535)

photo_20 = Image.open('Images/20.jpg')
photo_20 = photo_20.resize((50, 50))
photo_20 = ImageTk.PhotoImage(photo_20)
label_photo_20 = Label(image=photo_20)
button_20 = Button(window1, image=photo_20, command=lambda: money(20))
button_20.place(x=159, y=535)

photo_25 = Image.open('Images/25.jpg')
photo_25 = photo_25.resize((100, 50))
photo_25 = ImageTk.PhotoImage(photo_25)
label_photo_25 = Label(image=photo_25)
button_25 = Button(window1, image=photo_25, command=lambda: money(25))
button_25.place(x=215, y=535)

photo_50 = Image.open('Images/50.jpg')
photo_50 = photo_50.resize((100, 50))
photo_50 = ImageTk.PhotoImage(photo_50)
label_photo_50 = Label(image=photo_50)
button_50 = Button(window1, image=photo_50, command=lambda: money(50))
button_50.place(x=318, y=535)

photo_100 = Image.open('Images/100.jpg')
photo_100 = photo_100.resize((100, 50))
photo_100 = ImageTk.PhotoImage(photo_100)
label_photo_100 = Label(image=photo_100)
button_100 = Button(window1, image=photo_100, command=lambda: money(100))
button_100.place(x=3, y=592)

photo_200 = Image.open('Images/200.jpg')
photo_200 = photo_200.resize((100, 50))
photo_200 = ImageTk.PhotoImage(photo_200)
label_photo_200 = Label(image=photo_200)
button_200 = Button(window1, image=photo_200, command=lambda: money(200))
button_200.place(x=103, y=592)

photo_500 = Image.open('Images/500.jpg')
photo_500 = photo_500.resize((100, 50))
photo_500 = ImageTk.PhotoImage(photo_500)
label_photo_500 = Label(image=photo_500)
button_500 = Button(window1, image=photo_500, command=lambda: money(500))
button_500.place(x=210, y=592)

photo_1000 = Image.open('Images/1000.jpg')
photo_1000 = photo_1000.resize((100, 50))
photo_1000 = ImageTk.PhotoImage(photo_1000)
label_photo_1000 = Label(image=photo_1000)
button_1000 = Button(window1, image=photo_1000, command=lambda: money(1000))
button_1000.place(x=316, y=592)

total_price_text = Label(window1, text="Total Price:", fg="white", bg="black", font=('Times New Roman', 20, 'bold'))
total_price_text.place(x=450, y=540)
total_price_fill = Label(window1, bg="white", width=8)
total_price_fill.place(x=600, y=550)

input_price_text = Label(window1, text="Your Input:", fg="white", bg="black", font=('Times New Roman', 20, 'bold'))
input_price_text.place(x=450, y=490)
input_price_fill = Label(window1, width=8, height=1, bg="white")
input_price_fill.place(x=600, y=500)

# Placing the clear input button.

clear_button = Button(window1, text="Clear Input", fg="black", bg="white", height=0, command=lambda: money(0))
clear_button.place(x=705, y=498)

# Placing the image button purchase.

photo_purchase = Image.open('Images/purchase.png')
photo_purchase = photo_purchase.resize((300, 50))
photo_purchase = ImageTk.PhotoImage(photo_purchase)
purchase_label = Button(window1, image=photo_purchase, command=lambda: purchase_())
purchase_label.place(x=470, y=585)

# Placing the current stock button.

stock_button = Button(window1, text="Current Stock", command=stock)
stock_button.place(x=692, y=545)

# Placing the Shop Now image button.

photo_shop = Image.open('Images/shop.png')
photo_shop = photo_shop.resize((120, 120))
photo_shop = ImageTk.PhotoImage(photo_shop)
buy_button = Button(window1, image=photo_shop, command=lambda: shop())
buy_button.place(x=850, y=505)

# Placing the exit image button.

photo_exit = Image.open('Images/exit.jpg')
photo_exit = photo_exit.resize((120, 120))
photo_exit = ImageTk.PhotoImage(photo_exit)
exit_button = Button(window1, image=photo_exit, command=exit_)
exit_button.place(x=1030, y=505)
window1.mainloop()

client.close()
