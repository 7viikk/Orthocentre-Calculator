try:
    x1=float(input("Enter the x-cordinate of 1st vertex"))#a
    y1=float(input("Enter the y-cordinate of 1st vertex"))#a
    x2=float(input("Enter the x-cordinate of 2nd vertex"))#b
    y2=float(input("Enter the y-cordinate of 2nd vertex"))#b
    x3=float(input("Enter the x-cordinate of 3rd vertex"))#c
    y3=float(input("Enter the y-cordinate of 3rd vertex"))#c
except ValueError:
    print("The input value is not a numerical value. Please input a valid number")
    exit()
if x1==x2 and y1==y2 or x1==x3 and y1==y3 or x2==x3 and y2==y3:
    print("Two co-ordinates are identical and hence do not form a triangle. Therefore finding orthocentre is not possible")
    exit()
elif (y2-y1)*(x3-x2)==(y3-y2)*(x2-x1):
    print("The given coordinates are co-linear and do not form a triangle, hence finding orthocntre is not possible")
    exit()
mAB=(y2-y1)/(x2-x1)
mCE=-1/mAB

mBC=(y3-y2)/(x3-x2)
mAD=-1/mBC
mAC=(y3-y1)/(x3-x1)

x=(mCE*x3-y3+y1-mAD*x1)/(mCE-mAD)
y=mCE*x-mCE*x3+y3
print("The orthocentre of the triangle is", "(", round(x, 2) , ",", round(y, 2) ,")")
