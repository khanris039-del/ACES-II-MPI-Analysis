# variables
# print
# lists
# comments

# x = 1 #integer
# y = [0, 1, 2, 3, 4]
#
# for i in range(6):
#     print(i)
#
# while x == 5:
#     print(5)

# if
# and
# in
# else
# elif


#########################
#AND STATEMENTS
#########################
# SYNTAX

# x = 4
# y = 4
# z = 5
#
# if y == x and y == z:
#     print('potato')
# else:
#     print('spud')

#########################
#NOT STATEMENTS
#########################
#SYNTAX
# NOT, !
# x, name = 5, "arissa"
# print (x, name)

# x, y, z = False, True, False

#not reverses the logic
#
# if x is not True:
#     print("Potato")

# y = [[1], [2], [3], [5, 6, 7]]
# if not [5, 6, 7] in y:
#     print("This is a happy potato")
# else:
#     print("this is a sad potato")

# z, k = 1, 2
#
# if z == 1:
#     print("Spud")
#     #assigning not statement
#     if k  != 2 :
#         print("tuber")


#########################
#INEQUALITIES
#########################
#syntax
# <, >, <=, >=

# x, y = 3, 9
#
# #comparing lists
# z, j = [5, 6],[5, 6]
#
# if z == j:
#      print("test")

#########################
#IN STATEMENTS
#########################

# SYNTAX
# in


# a = [1,2,3,4,5]

# if 5 in a:
#     print('test')

# look inside the ray and print the thing
# for value in a:
#     print(value)
#
# b = [[1], [48397], 44847, [3849], "wooooowwwwwwww", (74837497)]
#
# for thing in b:
#     print(thing)


#########################
#RANGE AND ENUMERATE
#########################

# RANGE
# A = range(1, 6, 1)

#for  thing in A:
#   print(thing)

#ENUMERATE

# B = [1, 2, 3, 4, 5]
# for thing, idx in enumerate(B):
#     print(idx, thing)

#enumerate will pull out the index and the thing itself; order sensitive
#under the hood
# x, y = (1, 2)
# print(x, y)


#########################
#  APPENDING
#########################

# a = [1,2,3,4]
# a.append([4,5,6])
# print(a)

# c = []
# for val in range(1000000):
#     c.append(val)
# print(c)


#########################
#  FOR LOOPS SPECIAL SYNTAX
#########################


# L = [[1,2], [3,4], [5,6]]
#
# for sublist in L:
#     print(L)



#########################
#  LIST COMPREHENSION
#########################


# a = []
# for val in range(5):
#     a.append(val)

# same as

a = [val for val in range(5)]

a = [val/10 for val in range(5)]
#this is a lot faster
#This is saying go into the range and print each thing inside it, and ou can manipulate the output by adding operations onto the output


#########################
#  DICTIONARIES
#########################


dict1 = {}
