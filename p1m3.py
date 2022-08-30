# [ ] create, call and test 
def cheese_Order(order_amount):
    maximum_order = 100
    minimum_order = 1
    price = 7.99
    
    if order_amount > maximum_order:
        print(order_amount, "is more than currently available stock")
    elif order_amount < minimum_order:
        print(order_amount, "is below minimum order amount")
    else:
        print(float(order_amount), "costs" , "$" , int(order_amount) * price)
        

order_a = float(input("Enter cheese order weight (numeric value)"))
cheese_Order(order_a)