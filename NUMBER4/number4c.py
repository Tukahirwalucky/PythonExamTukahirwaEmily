#calculate the value of d
#x1= 60
#x2 = 30
#y1 = 160.5,
#y2 =97.7


#importing modules
import math
x1 = int(input('Enter the value of x1:\t'))  # int() to typecast string input to integer
x2 = int(input('Enter the value of x2:\t'))
y1 = float(input('Enter the value of y1:\t'))  # float() to typecast string input to float
y2 = float(input('Enter the value of y2:\t'))


simple_expression = (x1-x2) + (y1-y2)
d = math.sqrt((x1-x2) + (y1-y2))

#displaying the result
print(f'the value of d is: {d}')