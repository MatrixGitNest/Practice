#  Variables
'''   
   1)Variables can only start with _ or letters.
   
   Example:_name,na_me,Name_,name__Name_,_name_-All are considered as different variables.
   
   2))Variables can only have alpha-numeric characters.(A-Z,0-9 and _)
   3)Variables cannot have space in it. 
   4)Python reserved keywords cannot be used as a variable
   5)Variables are case sensitive. Name,name-Both are considered as different variables.


   6)camel case - use upppercase for first letter in each word except for first word ---- kmPerHour  -
   7)Pascal case- use uppercase  for first letter in each word ---- PricePerLitre 
   8)snake case -  use undercore after every word ---- km_per_hour
------------------------------------------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------------------------------------   
'''    
#     Variables contains Identifier and Objects.
   
'''
   1)Identifier: Imagine there is a container. This containers have to be stored in a place.
                 In computer these conatiners are stored in a place called memory(address/location).
                 Memory or address/location are usually in binary form.Ex:14073331576120.Binary language is understood by computer.
                 It means one container is stored in a memory 14073331576120.
                 Similarly each container will have different memory.
                 This is how everything is stored in a computer.
                 
                 To make it easy to identify the container we use identifier.
                 Identifier is nothing but a name we give to the container.   
                 Identifier is a reference point that direct towards the memory (address/location)
                 where the object is stored.
     
                 Example:  x = 5. x is the name of the container.
                                  = means assigning.
                                  5 is the value stored in the object.
   
   2)Objects:Imagine there is a container that holds a value in it.
             Objects are stored in memory (address/location) that is allocated randomly when they are created.
             Object is an instance of a class ,which can contain data and functions.
    
            Example: x = 5. 5 is the value that is stored in the object. 

            when we create a variable something called Pyobject gets created which is stored in the heap memory.
            This contains the data about the value.

            In the below example 5 is the value.

            Example: x = 5.
            
            PyObject:

            datatype - Int               
            reference count(identifier)-1       
            size(number/count of data)-1
      
   3) Whenever we call the container the value in the object is returned.'''
x=5
print(x) #output:5


'''
   4)Everything in python is an object including variables,keywords,functions.
    Object is an instance of a class ,which can contain data and functions.'''

'''In the below Example:
   x is an identifier and 5 is the object i.e, 5 is the value stored in object memory ,
   and x is a reference point that directs towards that object memory(address/location).''' 

x=5
print(id(x)) #output:14073331576120 

#x is the Name of the container i.e, identifier.
#5 is the value  stored in the object.
#14073331576120 is the container i.e, memory(address/location) where the object is stored.
# Use keyword id() to get memory(address/location)).


'''In the below example:
   Like x,y is also a reference point that directs towards the object memory(address/location) where 5 is located.
   Initially,the container that is holding the object which has stored the value 5 is given the name x.
   Now that we have assigned y = x.
   This means the same container can also be called as y.This is called interning.
   
   Initially we saw when a variable is created python allocates a new memory (address/location).
   In this case python is not allocating a new memory(address/location).
   It is using the existing memory(address/location) i.e, 14073331576120 (Refer with the output).
   But creates a new reference point to the existing memory.This saves memory  space.
   Like another name to the same container.
   '''
x=5
y=x
print(id(x)) #output:14073331576120 
print(id(y)) #output:14073331576120 


'''1)when given a new value to y, python overwrites the existing value.
   2)Now it allocates a new memory(address/location) to store the object that is holding the  value 45, 
     and y becomes the reference point to the memory(address/location) of the object holding the value 45. )
   3)Refer to the output of above example for recognizing the difference of memory(address/location) '''


y= 45
print(y)     #output:45
print(id(y)) #output:140733831577400 


#   Function

'''
In Python, indentation is used to define blocks of code.
 It tells the Python interpreter that a group of statements belongs to a specific block.
All statements with the same level of indentation are considered part of the same block. 
Indentation is achieved using whitespace (spaces or tabs) at the beginning of each line.'''

'''
    Functions are reusable code.A function is nothing but a set of tasks we want to perform.
    In the below example we will see how addition is performed when written  as a function.
    Once a function is created we can use it anywhere in the program.
             we use def keyword to define function.
             keywords are in-built functions.We will learn more about it soon.
'''


def add(x,y):    #    In this line we are defining the add function.
    sum=x+y      #    This line belongs to the add functon.
    return sum   #    This line belongs to the add functon.

t=add(6,5)       #    Creating a varible t and assigning the add function to do the addition by giving values in the parameters.
print(t)         #    Getting the output of the variable t.
      
# def - It is a keyword in python.
#     - def keyword is used for defining a function.
# 
# add - Name of the function.

#():  - This is called a parameter.Inside the parameter we call varibles as arguements.

# (x,y): - x and y are called arguements inside a parameter.
#        - x and y are like holder.It holds whatever value we give it and perform the task with that value.Addition is the task here.
#        - WhiteSpace  in line 105,106 is called indentation.by default 4 whitespaces are taken in each line.
#          The code that is written after whitespace belongs to that particular function.
#          In this case it belongs to add function. 
 
#   =    - It means assigning.

# sum=x+y - creating a variable called sum.
#         - Assingning the variables x and y  with the a arithmetic  operator + to the varible sum.
#         - + is the arithmetic operator for addition.This is a built in function.We don't have to define it here.
#         - x and y are arguements we use in the parameter.
#         - x and y are like holder.It holds whatever value we give it .
#         - Addition is the task here.
#         - This calculates the sum with the input given in parameters. Ex:sum=3+5

# return sum- returns the value of addition of the number given in parameters.        Ex:sum=3+5  return 8
#         | 
#         |    return is a keyword.
#         |    return brings the value we want.
#         |    It is important to write return in every function even when a value is not expected.
#         |    If return not given,by default it will be None.
#         |    if return not given it will show  None in output i.e, it will show None in print() statement.
#         |
#         |--> sum is the varible that holds the value of addition of the given input in parameters.

#t=add(6,5)-t is a variable.we assign add function to it.
#           =  means assigning.

#           add is the function.This holds the instructions that we have programmed i.e, the task we want to perform.

#           python assigns the value that we provide,in the variable(x,y)respectively into the function through parameters 
#           as arguements which we created while defining the add function.
#           Then performs the adiition.
#           In this case (6,5) are values we give in the parameters as arguements.x = 6 and y = 5.
#   
#print(t)- prints the result of addition  of 6 and 5

#output:11


#Local Variable
 
def name():
     n=78
     return n

print(name())
print(n)

#Here local variable is n.
#Local variables are used within the function because it belongs to that function.
#When local variable is called outside the function we will get error. 



#Global Variable

Cost=56
def Book():
    Profit=10/100*Cost
    GST=Profit+Cost*18/100
    Price=Cost+GST+Profit
    return Price
print("Recipt no-23154,\nDate -12/12/2024,\nBilled for Rs",Book())
print(Cost)
#Here global variable is Cost=56
# global variable can be called outside the function anywhere in the program. 

