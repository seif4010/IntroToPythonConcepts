# write a program that displays the Hello World Message
print("Hello world!!")

# write a program the takes input from a user and finds the highest
x = float(input("Kindly enter an Integer x ... "))
y = float(input("Kindly enter an Integery ... "))

if (x > y):
    print ("{0} WAS THE GREATEST NUMBER {1}". format(x,y))
elif(y > x):
    print("{1} WAS THE HIGHEST NUMBER {0}".format(y,x))
else:
    print("Both values are equal!!!")

# asks the users 10 numbers and finds the highest
# store them in a list
# option 1
# function for calculating the highest number
def find_max( list ):
    max = list[ 0 ]
    for a in list:
        if a > max:
            max = a
    return max
 
 
num = int(input('How many numbers: '))
 
lst = []
 
for n in range(num):
    numbers = int(input('Enter number '))
    lst.append(numbers)
     
print("Maximum element in the list is :", find_max(lst))

# option 2
lst = []
 
num = int(input('How many numbers to work with: '))
 
for n in range(num):
    numbers = int(input('Enter number '))
    lst.append(numbers)
     
print("The highest element in the list is :", max(lst))