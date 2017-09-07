#Max Low
#9-7-17
#ItATriangle.py - can you make a triangle

A = float(input('Side A'))
B = float(input('Side B'))
C = float(input('Side C'))

print(A+B+C-max(A,B,C) - min(A,B,C) >= A+B+C-max(A,B,C))




