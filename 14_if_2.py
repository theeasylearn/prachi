#write a program to calculate profit or loss amount from user given purchase & sale price of the product 
purchase_amount = float(input("Enter purchase amount"))
sales_amount = float(input("Enter sales amount"))

difference = sales_amount - purchase_amount
if difference>0: # == != < <= > >= 
    print(f"your profit is {difference}")

if difference<0: # == != < <= > >= 
    print(f"your loss is {difference}")

print("good bye")
