#keyword argument
def my_function(child1,child2,child3):
    print("The younger child is :" + child1[1])
my_function(child1 ='raj',child2 = 'ronit', child3 = 'daulat')
#Variable lengh keword arument
def fun(**kid):
    print("this is my good child :" + kid["fname"])
fun(fname = 'ravina',lname ='patil')

#default parameter
def my_function(country = "India"):
    print("this is my country:" + country)
my_function("sweadon")
my_function("china")
my_function()