##cafe management system
##define manu
menu={
    'Pizza':40,
    'Pasta':50,
    'Burger':70,
    'Salad':20,
    'Coffee':80,
}

#greet
print("welcome to our restaurant")
print("Pizza: rs40\nPasta: rs50\nBurger: rs70\nSalad: rs20\nCoffee: rs80") 

order_total=0

item_1=input("enter the name of item you want to order =")
if item_1 in menu:
    order_total+=menu[item_1]
    print(f"your item {item_1} has been added to your order")
else:
    print(f"order item{item_1} is not available ")

another_order=input("Do you want to add another item?(Yes or No)")
if another_order=="Yes":
    item_2 =input("enter the name of second item=")
    if item_2 in menu:
        order_total+=menu[item_2]
        print(f"item {item_2} has been added to order")
    else:
        print(f"order item{item_2} is not avaiable")
print(f"the total amount of item to pay is {order_total}")