print("Enter the price of the item: ")
price = float(input())
print("Enter Quantity: ")
quant = int(input())
total = price * quant
if total > 500 and total <= 1000:
    total *= 0.9
elif total > 1000:
    total *= 0.85

total *= 1.07

print("Please pay $"+str(total))