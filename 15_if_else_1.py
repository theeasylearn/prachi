#write a program to findout & display how many days given calender month has 
# 1 3 5 7 8 10 12 this month has 31 days 
# 4 6 9 11  this month has 30 days 
# 2 month has 28/29 days 

month = int(input("Enter month"))
if month==2: # == != < > <= >=
    print("this month has 28/29 days")
    #stop program 
    exit(0) 

if month==4 or month==6 or month==9 or month==11:
    print("this month has 30 days")
else:
    print("this month has 31 days")

