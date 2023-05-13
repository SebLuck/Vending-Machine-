# Vending-Machine
This project was on a vending machine application coded in Python using the Tkinter, Matplotlib, and Socket libraries.
Interaction with the user was used on the client-side, and the data storage was processed on the server-side by interacting with the current stock of a product and updating the stock based on the orders made by the client.
A bar chart was implemented in the vending machine. You can view the stock available through this bar chart. It could be useful if you want to know which product is out of stock or not. 

# Features
- The client program has a user interface to view all the items and prices.
- The client can create an order by clicking on the "Shop Now" button.
- You can add a product to your cart after typing the code of the product and confirming to add it to your chart.
- You can cancel an order.
- You can select the quantity of the product you want to purchase.
- You can purchase if you have chosen the option "Finish and Pay" in the order process and input the amount equal to the total price.
- You can input money by clicking on the image button for notes and coins.
- You can view the current stock by clicking the "Current Stock" button.
- You can clear your input in case you made a mistake in the process.

# Limitation
One of the major problems with this program is that you cannot remove a product from your cart. For example, if you have already added a product to your cart, you will not be able to delete it. 

## Getting Started

- To run the project, you will need to install tkinter, matplotlib, and socket libraries. 
- Then, unzip the file in a directory.
- You will have to open two command prompts in the path where you added all the files.
- In one of the command prompts, you will have to run the file Server_machine.py first: python Server_machine.py
- Then you run the other Python file at the second command prompt: python Client_machine.py
- After this, you will normally get a welcome message.

