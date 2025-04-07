menu={
    
    'Pasta': 59,
    'Pizza':119,
    'Salad': 69,
    'Sandwich': 89,
    'Coffee': 49,
}
print("Welcome to python restraunt")
print("Pasta:59\n Pizza:119\n Salad:69\n Sandwich:89\n Coffee:49")

order_total=0

item_1=input("Please enter your order:")

if item_1 in menu:
    order_total += menu[item_1]
    print(f"your item {item_1} has been added to the cart")


else:
    print("Orderd item is not available")

another_item = input("Do you want to order something else:")  
if another_item == "yes":
     item_2 =input("Please enter your order:")
     if item_2 in menu:
         order_total += menu[item_2]
         print(f" Item {item_2} has been added to the cart")
else:
        print(f"ordered item {item_2} not available")

print(f" The total amount to be paid is {order_total}")  