# Import tabulate module
from tabulate import tabulate

#========The beginning of the class==========
class Shoe:

    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    # Define some class's methods as requested
    def get_cost(self):
        return self.cost
        
    def get_quantity(self):
        return self.quantity

    def __str__(self):
        return f"""Product : {self.product}
Country : {self.country}
Code    : {self.code}
Cost    : {self.cost}
Quantity: {self.quantity}\n"""

#=============Shoe list===========

shoe_list = []

#==========Functions outside the class==============

# Define the funtion that cast elements of a list in to int data type 
def cast_int(list):
    list_casted = [int(i) for i in list]
    return list_casted

# Define the function that print the content of shoe list in a table
def print_content_in_table():
    # Read again the data from shoe list
    country_list = [i.country for i in shoe_list]
    code_list = [i.code for i in shoe_list]
    product_list = [i.product for i in shoe_list]
    cost_list = [i.cost for i in shoe_list]
    quantity_list = [i.quantity for i in shoe_list]
    # Create a list of data in the shhoe list
    table_content_list = [(product_list[i],code_list[i],country_list[i],cost_list[i],quantity_list[i]) for i in range(len(country_list))]

    # Print the table using tabulate module. Looked at the website https://analyticsindiamag.com/beginners-guide-to-tabulate-python-tool-for-creating-nicely-formatted-tables/
    print("\nBelow are all of the products in the inventory:\n")
    print(tabulate(table_content_list, headers=["Product","Code","Country","Cost","Quantity"], showindex='always', tablefmt='fancy_grid')) 

# Define the function to read data from inventory.txt file and add the data to shoe list
def read_shoes_data():   
    # Anticipate the error that the inventory.txt file used for the function read_shoes_data doesn't exist
    try:
        content_inventory = ""
        with open("inventory.txt","r") as file:
            for i in file:
                content_inventory += i
    except FileNotFoundError:
        print("\nThe file having the name 'inventory.txt' does not exist. Please double-check and try again!")
        exit()

    # Filter the content and create a list of element
    content_inventory = content_inventory.replace("\n", ",")
    inventory_list = content_inventory.split(",")
    # Create lists of data 
    country_list = inventory_list[5:len(inventory_list):5]
    code_list = inventory_list[6:len(inventory_list):5]
    product_list = inventory_list[7:len(inventory_list):5]
    cost_list = inventory_list[8:len(inventory_list):5]
    quantity_list = inventory_list[9:len(inventory_list):5]

    # Create the Shoe object using the data and append the object into shoe list 
    for i in range(len(country_list)):
        shoe_list.append(Shoe(country_list[i], code_list[i], product_list[i], cost_list[i], quantity_list[i]))

# Function that can be used to append a new shoe object using passed parameters
def capture_shoes(country, code, product, cost, quantity):

    # Append to the shoe list a Shoe object with passed parameters
    shoe_list.append(Shoe(country, code, product, cost, quantity))
    # Append on the inventory.txt file the data about the new shoe object
    with open("inventory.txt","a") as file:
        file.write(f"\n{country},{code},{product},{cost},{quantity}")

    print("\nThanks! The data about the new product has been recorded\n")


# Function that shows the data about the products
def view_all():
    print("\nBelow are all of the products in the inventory:\n")
    for i in shoe_list:
        print(i)

# Function about re-stocking
def re_stock(): 
    print("\n***************\n")
    # Read and get again the data from the shoe list because it may have changed adready, also to have the lists of contents serving re-writing purpose later  
    country_list = [i.country for i in shoe_list]
    code_list = [i.code for i in shoe_list]
    product_list = [i.product for i in shoe_list]
    cost_list = [i.cost for i in shoe_list]
    quantity_list = [i.quantity for i in shoe_list]
        
    # Cast the quantity list into int, to find out the min value
    quantity_list_int = cast_int(quantity_list)

    # Check the condition and print the product with min stock
    print("Below is the product having the lowest stock:\n")
    for i in shoe_list:
        if int(i.quantity) == min(quantity_list_int):
            print(i)
    
    # Get input about user's choice about re-stocking
    restock_choice = input("Do you want to add more quantity for this product? (yes/no) ").lower()
    # Yes option
    if restock_choice == "yes" or restock_choice == "y":
        while True:                     # Defense input about re-stock quantity
            try:
                restock_quantity = int(input("\nHow many shoes of this product do you want to add? "))
                break
            except ValueError:
                print("\nYou have put an invalid number. Try again.\n")
        
        # Update the new stock on the shoe list
        for i in shoe_list:
            if int(i.quantity) == min(quantity_list_int):
                i.quantity = int(i.quantity)
                i.quantity += restock_quantity

        # Update the new stock on the local quantityList
        for i in range(len(quantity_list)):
            if int(quantity_list[i]) == min(quantity_list_int):
                quantity_list[i] = int(quantity_list[i])
                quantity_list[i] += restock_quantity

        # Update the new stock on inventory.txt file
        with open("inventory.txt","w") as file:
            file.write("Country,Code,Product,Cost,Quantity")
            for i in range(len(country_list)):   
                file.write(f"\n{country_list[i]},{code_list[i]},{product_list[i]},{cost_list[i]},{quantity_list[i]}")

        print("\nThanks! The stock of selected product has been updated.")   
    # "No" option
    elif restock_choice == "no" or restock_choice == "n":
        print("\nGood bye!")
    # "Wrong" option
    else:
        print("\nSorry, you had a wrong choice! Try again later.")
    print("\n***************\n")
        
# Searching function
def seach_shoe(code_check):
    # Create a list of code by reading again data from the shoe list
    code_list = [i.code for i in shoe_list]  

    # Checking the conditions and print out the result
    if code_check not in code_list:
        print("\nSorry! The product with the code you put is not in the inventory. Try again later.")

    else:
        print(f"\nBelow is the product with the code: {code_check}\n")
        for i in shoe_list:
            if i.code == code_check:
                print(i)

# Function that calculate and print the value of all the products
def value_per_item(): 
    print("\n***************\n")
    # Using class's methods to get the data about product's cost and quantity from the shoe list 
    cost_list = [i.get_cost() for i in shoe_list]
    quantity_list = [i.get_quantity() for i in shoe_list]

    # Casting the list's element into int data type
    cost_list_int = cast_int(cost_list)
    quantity_list_int = cast_int(quantity_list)

    # Calculate the value and put the value into the value List
    value_list = [cost_list_int[i]*quantity_list_int[i] for i in range(len(cost_list_int))]

    # Get input about user's choice about view mode
    view_option = input("""What view mode do you want to have about the data?
1 - Normal view
2 - View product data in a table
Your choice: (Please enter the choice's index) """)

    while view_option != "1" and view_option != "2":  # Defense the input view option
        print("\nSorry! You had a wrong input. Try again.")
        view_option = input("\nPlease enter '1' or '2' this time: ")

    # Depend on the input view option, showing the result
    if view_option == "1":
        print("\nBelow are data about products with their value.\n")
        for i in range(len(shoe_list)):
            print(f"{shoe_list[i]}Value   : {value_list[i]}\n")

    # Option to view data in the table
    elif view_option == "2":
        # Read again the data and create the list of content for the table
        country_list = [i.country for i in shoe_list]
        code_list = [i.code for i in shoe_list]
        product_list = [i.product for i in shoe_list]

        table_value_content_list = [(product_list[i],code_list[i],country_list[i],cost_list[i],quantity_list[i],value_list[i]) for i in range(len(country_list))]

        # Print out the table
        print("\nBelow are data about products with their value.\n")
        print(tabulate(table_value_content_list, headers=["Product","Code","Country","Cost","Quantity","Value"], showindex='always', tablefmt='fancy_grid'))

    print("\n***************\n")

# Finding the product having the highest quantity
def highest_qty():
    print("\n***************\n")
    # Read and get again the data about quantity from shoe list because it may have changed adready, also to have the lists of contents serving re-writing purpose later  
    quantity_list = [i.quantity for i in shoe_list]
        
    # Cast the quantity list into int, to find out the min value
    quantity_list_int = cast_int(quantity_list)

    # Check the condition and print the product with min stock
    print("Below is the product having the highest stock and needs selling:\n")
    for i in shoe_list:
        if int(i.quantity) == max(quantity_list_int):
            print(i)

    print("\n***************\n")
#==========Main Menu=============
# Call the read shoes data function
read_shoes_data()
print("Hello! Welcome to stock tracking system.\n")
# Ask for the user's choice
user_choice = ""
while user_choice != "7":
    user_choice = input("""What would you like to do?
1 - View data about all the products
2 - Add data about a new product
3 - Search data about a product
4 - Check the product having the lowest quantity and re-stock
5 - Check the product having the highest quantity
6 - See the value of all the products
7 - Quit
Your choice: (Please enter option's index) """)
    # Option 1: View all the product's data
    if user_choice == "1":
        print("\n***************\n")
        # Get the input about view option
        view_option = input("""What view mode do you want to have about the data?
1 - Normal view
2 - View product data in a table
Your choice: (Please enter the choice's index) """)
        # Defense the view option input
        while view_option != "1" and view_option != "2":
            print("\nSorry! You had a wrong input. Try again.")
            view_option = input("\nPlease enter '1' or '2' this time: ")
        # Depend on user's choice to print out the result
        if view_option == "1":
            view_all()
        elif view_option == "2":
            print_content_in_table()   
        
        print("\n***************\n")
    # Option 2: Add a new product
    elif user_choice == "2":       
        print("\n***************\n")
        print("You are adding a new product to the inventory.")
        # Get the input about the new product
        new_country = input("\nWhat is the country of the product? ")
        new_code = input("\nWhat is the code of the product? ")
        new_product = input("\nWhat is the name of this product? ")

        while True:                     # Defense input about the new cost
            try:
                new_cost = int(input("\nWhat is the cost of one product? "))
                break
            except ValueError:
                print("\nYou have put an invalid number. Try again.\n")

        while True:                     # Defense input about the new quantity
            try:
                new_quantity = int(input("\nWhat is the quantity of this product? "))
                break
            except ValueError:
                print("\nYou have put an invalid number. Try again.\n")
        # Add the new product using capture shoes function
        capture_shoes(new_country,new_code,new_product,new_cost,new_quantity)
        print("\n***************\n")
    # Option 3: Search info a bout a product
    elif user_choice == "3":
        print("\n***************\n")
        search_code = input("Please enter the product code: ")
        seach_shoe(search_code)
        print("\n***************\n")

    # Option 4: show the product having the min stock and re-stocking option
    elif user_choice == "4":
        re_stock()

    # Option 5: show the product having the highest quantity
    elif user_choice == "5":
        highest_qty()

    # Option 6: View the value of all products 
    elif user_choice == "6":
        value_per_item()

    # Last options
    elif user_choice == "7":
        print("Bye bye!")
    else:
        print("You had a wrong choice. Try again!")