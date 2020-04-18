import math

line1 = input().split(" ")
line2 = input().split(" ")

x1,y1 = l1
x2,y2 = l2

dist = math.sqrt(((float(x2) - float(x1))*(float(x2) - float(x1))) + ((float(y2)-float(y1)) *(float(y2)-float(y1))))
 
print( "%0.4f" %dist )