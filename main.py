num1 = [1,2,3]
num2 = [4,5,6]
res = map(lambda x,y:x+y, num1, num2)
print(list(res))

#map
num = [1,2,3,4,5]
def square(n):
    return n*n
aq= list(map(square, num))
print(aq)