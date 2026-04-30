#write a program to findout whether person is eligible to apply for the job or not from given age. if person's age is above 18 and less then 58, he is eligible to apply for the job otherwise not eligible to apply for job 

age = int(input("Enter your age"))
if age>18 and age<58:
    print("you are eligible to apply for the job")
else:
    print("you are not eligible to apply for the job")

print("Good bye")