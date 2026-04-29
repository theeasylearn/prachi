#example of if statement 
#write a program to calculate and display cube of given positive number 
number = int(input("Enter number to calculate qube"))
if number<0: # == != < > <= >=
    #convert negative number into positive 
    number = 0 - number
    print("negative number is converted into positive number")
    
cube = number * number * number 
print(f"cube = {cube}")

