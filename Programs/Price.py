def totalprice(price,tax):
    total=price+tax
    print('The price is $',price)
    print('The tax is $',tax)
    print('The total is $',total)
    return total
print('What is the price of your drone?')
price=float(input())
tax=(8.5/100)*price
totalprice(price,tax)
