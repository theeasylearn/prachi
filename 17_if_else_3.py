'''write a program to find out whether person is eligible to apply for Govt. of Gujarat clerk post or not based upon below criteria.
if candidate has general cast and age below 25 and Graduate he is eligible 
if candidate has OBC cast and age below 27 and Graduate he is eligible 
if candidate has sc cast and age below 28 and Graduate he is eligible 
if candidate has st cast and age below 30 and Graduate he is eligible 
decide what is input 
    input: caste, age, education 
check is there any common criteria
Yes candidate must be graduate
'''
'''
write a program to find out whether person is eligible to apply for Govt. of Gujarat clerk post or not based upon below criteria.
if candidate has general cast and age below 25 and Graduate he is eligible 
if candidate has OBC cast and age below 27 and Graduate he is eligible 
if candidate has sc cast and age below 28 and Graduate he is eligible 
if candidate has st cast and age below 30 and Graduate he is eligible 
decide what is input 
    input: caste, age, education 
check is there any common criteria
Yes candidate must be graduate
'''
caste = input('Enter your caste')
age = int(input('Enter your age'))
education = input('enter your education')

if education == 'graduate' and age<25 and caste=='general':
    print("you are eligible to apply for the job")

if education == 'graduate' and age<27 and caste=='obc':
    print("you are eligible to apply for the job")

if education == 'graduate' and age<28 and caste=='sc':
    print("you are eligible to apply for the job")

if education == 'graduate' and age<30 and caste=='st':
    print("you are eligible to apply for the job")


