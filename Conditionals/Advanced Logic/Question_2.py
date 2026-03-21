'''Take product price and customer type (regular/premium) and calculate discount.'''

product_price=float(input("Enter product price:"))

customer_type=input("Enter customer type:")

if customer_type=="regular":
    print("product_price=",product_price)
    print("discouunt=18%")
    dis=product_price*.18
    print("discount=",dis)
    print("final price=",product_price-dis)
elif customer_type=="premium":
        print("product_price=",product_price)
        print("discouunt=25%")
        dis=product_price*.25
        print("discount=",dis)
        print("final price=",product_price-dis)
