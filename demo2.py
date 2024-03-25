#passing a list in fun
def fun(fruit):
    print(type(fruit))
    print(fruit)
fruit = ['apple','mango','cherry']
fun(fruit)
#print a even number from list using function
def even(lis):
    for i in lis:
        if i % 2 ==0:
            print(i)
lis = [1,2,3,4,5,6,7,8,9,10]
even(lis)

#return keyword
def my_function(x):
    return 5 * x
print("15 : ",my_function(3))
print(my_function(4))
print(my_function(5))