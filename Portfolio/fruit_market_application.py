import os
import platform
import re
from tabulate import tabulate

def clear_terminal():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")
clear_terminal()

fruit_list = [
    ["Apple", 20, 10],
    ["Orange", 15, 15],
    ["Grapes", 25, 20]
]

def display_fruits():
    if not fruit_list:
        print("\nNo fruits available.")
        return
    
    print("\nAvailable Fruits:")
    fruitsTable = tabulate(fruit_list,
                     headers=["Name", "Stock", "Price"],
                     showindex=True, tablefmt= 'plain',
                     colalign=('center', 'center', 'center', 'center'))
    print(fruitsTable)

def get_valid_int(prompt, min_val=0, max_val=10000):
    while True:
        try:
            value = input(prompt)
            if value.isdigit() and int(value) >= min_val and int(value) <= max_val:
                return int(value)
            else:
                print(f"Please enter a valid integer between {min_val} and {max_val}.")
        except ValueError:
            print("Invalid input! Please enter a valid integer.")

def get_valid_fruit_name():
    while True:
        name = input("Enter fruit name: ").strip().title()
        if len(name) > 20:
            print("Fruit name is too long. Please keep it under 20 characters.")
        elif not re.match("^[A-Za-z]+$", name):
            print("Invalid name! Fruit name can only contain letters.")
        else:
            return name

def add_fruit():
    name = get_valid_fruit_name()
    stock = get_valid_int("Enter stock quantity: ", 1)
    price = get_valid_int("Enter price: ", 1)
    
    for fruit in fruit_list:
        if fruit[0] == name:
            fruit[1] += stock
            print(f"Updated {name}'s stock to {fruit[1]}!\n")
            return
    
    fruit_list.append([name, stock, price])
    print(f"{name} has been added!\n")

def remove_fruit():
    if not fruit_list:
        print("No fruits available to remove!\n")
        return
    display_fruits()
    index = get_valid_int("Enter the index of the fruit to remove: ", 0)
    if 0 <= index < len(fruit_list):
        removed_fruit = fruit_list.pop(index)
        print(f"{removed_fruit[0]} has been removed.\n")
    else:
        print("Invalid index!\n")

def buy_fruit():
    cart = []
    
    while True:
        display_fruits()
        if not fruit_list:
            print("No fruits available for purchase!\n")
            return
        
        index = get_valid_int("Enter the index of the fruit to buy: ", 0)
        if index < len(fruit_list):
            quantity = get_valid_int("Enter quantity to buy: ", 1)
            name, stock, price = fruit_list[index]
            
            if quantity > stock:
                print("Not enough stock!\n")
                continue
            
            fruit_list[index][1] -= quantity
            
            fruit_in_cart = False
            for item in cart:
                if item[0] == name:
                    item[1] += quantity
                    fruit_in_cart = True
                    break
            
            if not fruit_in_cart:
                cart.append([name, quantity, price])
            
            print(f"{name} x{quantity} has been added to your cart.\n")
            
            add_more = input("Do you want to add another fruit to your cart? (y/n): ").strip().lower()
            if add_more != 'y':
                break
        else:
            print("Invalid index!\n")
    
    print("\nYour Cart:")
    cart_table = tabulate(cart, headers=["Name", "Quantity", "Price"], showindex=True, colalign=('center', 'center', 'center'))
    print(cart_table)
    
    total_price = sum([quantity * price for _, quantity, price in cart])
    print(f"\nTotal amount: {total_price}")
    
    while True:
        payment = get_valid_int("Enter payment amount: ", total_price)
        if payment >= total_price:
            print(f"Purchase successful! Change: {payment - total_price}\n")
            break
        else:
            print("Insufficient payment! Please enter the correct amount.\n")



while True:
    print("\nWelcome to the Fruit Market")
    print("1. Display Fruits")
    print("2. Add Fruit")
    print("3. Remove Fruit")
    print("4. Buy Fruit")
    print("5. Exit")
    
    choice = input("Select an option (1-5): ")
    
    if choice == "1":
        display_fruits()
    elif choice == "2":
        add_fruit()
    elif choice == "3":
        remove_fruit()
    elif choice == "4":
        buy_fruit()
    elif choice == "5":
        print("Thank you for visiting the Fruit Market!")
        break
    else:
        print("Invalid choice, please try again!\n")
