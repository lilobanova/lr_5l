
x1 = int(input("Price of one roll of wallpaper = "))
x2 = int(input("The price of one can of paint = "))

price = float(8 * x1 + 2 * x2)

if 200 <= price <= 500:
    price *= 0.97
elif 500 < price <= 800:
    price *= 0.95
elif 800 < price <= 1000:
    price *= 0.93
elif price > 1000:
    price *= 0.91

print("Discount price = %.2f" % price)
