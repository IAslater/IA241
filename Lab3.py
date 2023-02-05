# list and set lec. 3


my_list=[1,2,3,4,5]#define the list we need square brackets

print(type(my_list))#type shows you what it is. 

my_nested_list=[1,2,3,my_list]
print(my_nested_list)

my_list[0]=6# you can fix a value like this

print(my_list) # call index by asking the position in the list (starts at O from the left or from the right it is -1 )
print(my_list[0])
print(my_list[-1]) # calling the right most number 
# to slice we need to separate them with a colon(in the index)
print(my_list[2])#end of index lesson 

print(my_list[0:1]) #slice reported! the value of the last inex will not be reporeted
print(my_list[:3])

print(my_list[:])

x,y,z = ['a','b','c']

print(x)

my_list.append(7)# this is addddddding
print(my_list)

my_list.remove(5)
print(my_list)

my_list.sort()
print(my_list)

my_list.reverse()
print(my_list)

# show you if it is true or false not the same as index and do not make is a string
# lab section 3.1
str_list= ['a','d','e','b','c']
str_list.sort()
print(str_list)
#3.2
str_list.append("F")
print(str_list)

#3.3

str_list.remove("d")
print(str_list)
#3.4

print(str_list[2])
# 3.5

my_list = ['a', '123', 123,'b', 'False', 'False', 123, None, "None"]

print(len(set(my_list)) )
#3.6

print(len("this is my third python lab".split()) )
#3.7
num_list = [12,32,43,35]
num_list.sort()

print(num_list[0])
print(num_list[-1])
#3.8
game_board = [ [0,0,0],[0,0,0],[0,0,0] ]

game_board[1][1]=1
print(game_board)

#Test