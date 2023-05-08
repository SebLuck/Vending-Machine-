import socket
import pickle
import csv

# Create server socket.

Host = '127.0.0.1'
Port = 65432

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((Host, Port))
server.listen(1)
print('Waiting for connection...')

client, (host, port) = server.accept()
print("Connection established")

receive = client.recv(1024)

# This if statement will check if the user exits the vending machine.
# If the user exits the vending machine without making a transaction, it will print a message telling that the user has
# exit.
if receive:
    # Take the data that the user has purchased.
    # This data is a list which is called add_list on the client side.
    # This list contains the products that the customer has bought
    receive_data = pickle.loads(receive)
    # Taking data from the csv file stock.
    with open('stock.csv', 'r') as file:
        stock = file.readlines()
        c = 0
        stock_list = []
        # Make the stock_list become a 2D list.
        for a in stock:
            list1 = stock[c].split(",")

            stock_list.append(list1)
            c = c + 1

        for g in range(len(stock_list)):
            stock_list[g][3] = stock_list[g][3].replace('\n', "")  # Removing all the \n in list.

        p = 0
        # This for loop will delete the products in the stock_list list. For example, if the user has bought 1
        # Sprite, it will delete one index from the stock_list that contain the name Sprite.
        for e in range(len(receive_data)):
            p = 0
            for f in range(len(stock_list)):
                # Check if the product name in stock_list list is equal to the product name of the receive_data list.
                if stock_list[f][1] == receive_data[e][0]:
                    # For example, if fanta has 2 quantity it will delete the 2 index from stock_list that contain the
                    # name fanta.
                    for o in range(int(receive_data[e][2])):
                        del stock_list[p]
                    break  # Using the break statement so that it does not delete wrong products.
                else:
                    p = p + 1
        # Each for loop will found the quantity of a product.
        quantity_num1 = 0
        for n in range(len(stock_list)):
            if stock_list[n][1] in "Coca Cola":
                quantity_num1 = quantity_num1 + 1

        quantity_num2 = 0
        for n in range(len(stock_list)):
            if stock_list[n][1] in "Fanta":
                quantity_num2 = quantity_num2 + 1

        quantity_num3 = 0
        for n in range(len(stock_list)):
            if stock_list[n][1] in "Pepsi":
                quantity_num3 = quantity_num3 + 1

        quantity_num4 = 0
        for n in range(len(stock_list)):
            if stock_list[n][1] in "Sprite":
                quantity_num4 = quantity_num4 + 1

        quantity_num5 = 0
        for n in range(len(stock_list)):
            if stock_list[n][1] in "Water":
                quantity_num5 = quantity_num5 + 1

        quantity_num6 = 0
        for n in range(len(stock_list)):
            if stock_list[n][1] in "Doritos Chili":
                quantity_num6 = quantity_num6 + 1

        quantity_num7 = 0
        for n in range(len(stock_list)):
            if stock_list[n][1] in "Doritos Salted":
                quantity_num7 = quantity_num7 + 1

        quantity_num8 = 0
        for n in range(len(stock_list)):
            if stock_list[n][1] in "Doritos Cheese":
                quantity_num8 = quantity_num8 + 1

        quantity_num9 = 0
        for n in range(len(stock_list)):
            if stock_list[n][1] in "Lays Classic":
                quantity_num9 = quantity_num9 + 1

        quantity_num10 = 0
        for n in range(len(stock_list)):
            if stock_list[n][1] in "Lays Barbecue":
                quantity_num10 = quantity_num10 + 1

        quantity_num11 = 0
        for n in range(len(stock_list)):
            if stock_list[n][1] in "Lays Masala":
                quantity_num11 = quantity_num11 + 1

        quantity_num12 = 0
        for n in range(len(stock_list)):
            if stock_list[n][1] in "Kit Kat":
                quantity_num12 = quantity_num12 + 1
        # This for loop will update the quantity of the stock_list list.
        for d in range(len(stock_list)):
            if stock_list[d][1] in "Coca Cola":
                stock_list[d][3] = quantity_num1

            if stock_list[d][1] in "Fanta":
                stock_list[d][3] = quantity_num2

            if stock_list[d][1] in "Pepsi":
                stock_list[d][3] = quantity_num3

            if stock_list[d][1] in "Sprite":
                stock_list[d][3] = quantity_num4

            if stock_list[d][1] in "Water":
                stock_list[d][3] = quantity_num5

            if stock_list[d][1] in "Doritos Chili":
                stock_list[d][3] = quantity_num6

            if stock_list[d][1] in "Doritos Salted":
                stock_list[d][3] = quantity_num7

            if stock_list[d][1] in "Doritos Cheese":
                stock_list[d][3] = quantity_num8

            if stock_list[d][1] in "Lays Classic":
                stock_list[d][3] = quantity_num9

            if stock_list[d][1] in "Lays Barbecue":
                stock_list[d][3] = quantity_num10

            if stock_list[d][1] in "Lays Masala":
                stock_list[d][3] = quantity_num11

            if stock_list[d][1] in "Kit Kat":
                stock_list[d][3] = quantity_num12
    # Rewrite the csv file stock.csv.
    # With this, the csv file will be updated.
    with open('stock.csv', 'w', newline="") as file1:
        content_write = csv.writer(file1)
        content_write.writerows(stock_list)

    print("Transaction done")

else:
    print("The user has exit the client.")

client.close()
