# a=[1,2,3,[4,5,6],2,3,4]
#
# for i in a:
#     if type(i)==list:
#         for ele in i:
#             print(ele)
#     else:
#         print(i)
from multiprocessing.reduction import duplicate



# a=[1,2,3,[4,5,6],7,8,9]
# for i in a:
#     if isinstance(i,list):
#         for ele in i:
#             print(ele)
#     else:
#         print(i)

# a = {
#     "Name": "uday",
#     "Details": {"age": 24, "place": "kippam"}
# }
#
# for i in a:
#     if isinstance(a[i], dict):
#         for ele in a[i]:
#             print(ele, a[i][ele])
#     else:
#         print(i, a[i])



# a = [{
#     "Name": "uday",
#     "Details": {"age": 24, "place": "kuppam"}
# },(1,2,3,4)]
#
# for i in a:
#     if isinstance(i, int):
#         for ele in i:
#             print(ele)
#     elif isinstance(a[i], dict):
#         for key in a[i]:
#             print(key.a[i][key])
#     else:
#         print(i, a[i])

# a = [{
#     "Name": "uday",
#     "Details": {"age": 24, "place": "kuppam"}
# }, (1, 2, 3, 4)]
#
# for i in a:
#     if isinstance(i, int) or isinstance(i, tuple):
#         for x in i:
#             print(x)
#     elif isinstance(i, dict):
#         for key in i:
#             print(key, i[key])
#             if isinstance(i[key], dict):  # Check if the value is a dictionary
#                 for sub_key in i[key]:
#                     print( sub_key ,i[key][sub_key])  # Indented for clarity
#     else:
#         print(i)


#
# dict1 = [{
#     "Name": "uday",
#     "Details": {"age": 24, "place": "kuppam"}
# }, (1, 2, 3, 4)]
#
# for mydict in dict1:
#     if isinstance(mydict,int) or isinstance(mydict,tuple):
#         for list in mydict:
#             print(list)
#
#     elif isinstance(mydict,dict):
#         for newdict in mydict:
#             print(newdict)
#             if isinstance(mydict[newdict],dict):
#                 for subdict in mydict[newdict]:
#                     print(subdict,mydict[newdict][subdict])



#
# a=[{"Name":"uday",
#    "age":{"height":24}
#
#    }]
#
# for i in a:
#     if isinstance(i,dict):
#         for x in i:
#             print(x,i[x])
#             if isinstance(i[x],dict):
#                 for z in i[x]:
#                     print(z,i[x][z])
#     else:
#         print(i)
#
# def age(num):
#     if num<0:
#         raise ValueError("only integers")
#     if num%2==0:
#         print("even")
#
#     else:
#         print("exception not occured")
#
#
# try:
#     num = int(input("Enter a number: "))
#     age(num)
# except:
#     print("Exception occurred:")


#
# a=[{"Name":"uday",
#    "age":{"height":24}
#
#    }]
#
# for i in a:
#     if isinstance(i,dict):
#         for x in i:
#             print(x,i[x])
#
#     if isinstance(i[x],dict):
#         for y in i[x]:
#             print(y,i[x][y])

#
# a=["A","B",'c','d','e','f','g']
# # [ 0,  1, 2,  3,  4,  5,   6,  7]
# for i in range(len(a)-2,len(a)):
#     print(i)
#     # print(len(a),"uday")
# print(len(a))


# employees = {"satyam": [35, 50000],
#
#              "shivam": [45, 60000],
#
#              "Bhaskar": [55, 70000]
#
#              }

#approach1

# vals = employees.values()
# vals = [i[1] for i in vals]
# print(vals)
# lowest = min(vals)
# print(lowest)
#
# #approach2
#
# for k, v in employees.items():
#     if lowest in v:
#         print(k, lowest)


# Output: satyam
# Find the employee name & his age whose salary is lowest.



#


# Convert a nested list into a simple list.
# # output = [1, 2, 3, 4, 5, 6, 7, 8, 9]

input = [[1, 2, [3, 4]], [5, 6], [7, [8, 9]]]

l = []

def fun_nested_list(l1):
    for i in l1:
        if isinstance(i, list):
            fun_nested_list(i)   # Recursive call for nested lists
        else:
            l.append(i)
    return l

print(fun_nested_list(input))

# approach2
#
# input = [[1, 2, [3, 4]], [5, 6], [7, [8, 9]]]
#
# l = []
#
# def fun_nested_list(l1):
#     for i in l1:
#         if isinstance(i, list):
#             for j in i:
#                 if isinstance(j,list):
#                     for k in j:
#                         l.append(k)
#                 else:
#                     l.append(j)
#
#         else:
#             l.append(i)
#
#     return l
#
# print(fun_nested_list(input))



#dictionary count



# d = {"name": "sai", "place": "bang", "interview": "msys", 1: "sai", 2: "bang", 3: "bang", 4: "msys"}
#
# c = {}
# for key, value in d.items():
#     if value in c:
#         c[value] += 1
#     else:
#         c[value] = 1
#
# print(c)

# d = {"name": "sai", "place": "bang", "interview": "msys", 1: "sai", 2: "bang", 3: "bang", 4: "msys"}
#
# for key, value in d.items():
#     if key:"name":
#         print(value)


# a="hello world"
# c={}
# for i in a:
#     if i in c:
#         c[i]+=1
#     else:
#         c[i]=1
# print(c)


# a="hello world"
# result=a.split()
# print(result)
# for i in result:
#     print(i[::-1])
# #






# a=[1,2,3,4,5]
# b=a[0]
# for i in a:
#     if i>b:
#         b=i
# print(b)

# a = "udayudayuudayday"
# v = "aeiou"
# c = []
#
# for i in v:
#     if a.count(i) > 1:
#         c.append(i)
#
# print(c)

# a = "udayudayuudayday"
# v = "udayudayuday"
# c = []
#
# for i in a:
#     if i not in c and v.count(i)>1:
#         c.append(i)
# print(c)

# a = "udayudayuudayday"
# v = "aeiou"
# c = []
#
# for i in v:
#     if a.count(i)>1:
#         c.append(i)
# print(c)


# a = "abcdefgh"
# v = "abcdefghab"
# c = []
#
# for i in a:
#     if v.count(i)>1:
#         c.append(i)
# print(c)


# a=[1,2,3,[4,5,6],7,8,9]
# for i in a:
#     if isinstance(i,list or dict):
#         for j in i:
#             print(j)
#     else:
#         print(i)
#
#
# def get_even_numbers(lst):
#     even_list = []
#     for i in lst:
#         if i % 2 == 0:
#             even_list.append(i)
#     return even_list
#
# # Test
# a = [1, 2, 3, 4, 5, 6]
# print(get_even_numbers(a))  # Output: [2, 4, 6]

#
# a=[1,2,3,4,5,6,7,1,2]
# b=[]
# duplicates=[]
# for i in a:
#     if i not in  b:
#         b.append(i)
#     elif i not in duplicates:
#         duplicates.append(i)
#
# print(b)
# print(duplicates)

# a="hello world"
# b=''
# for i in a:
#     b=i+b
# print(b)
  # Output: [1, 3, 12, 0, 0]
#


# def move_zeroes(nums):
#     result = []  # to store non-zero numbers
#     zero_count = 0  # to count how many zeros we find
#
#     for num in nums:
#         if num != 0:
#             result.append(num)
#         else:
#             zero_count += 1
#
#     result.extend([0] * zero_count)  # add zeros at the end
#     return result
#
#
# nums = [0, 1, 0, 3, 12]
# nums = move_zeroes(nums)  # assign the returned result back to nums
# print(nums)  # Output: [1, 3, 12, 0, 0]

# a=[2,3,4,8,5,6,11]
# b=a[0]
#
# for i in a:
#     if i<b:
#         b=i
# print(b)


# a = [8,2,3,7,2,4,1]
# if a[0] > a[1]:
#     flarge = a[0] #8
#     slarge = a[1] #2
# else:
#     flarge = a[1]
#     slarge = a[0]
#
# for i in range(2, len(a)):
#     if a[i] > flarge:
#         slarge = flarge
#         flarge = a[i]
#     elif a[i] > slarge:
#         slarge = a[i]
#
# print(f"First largest: {flarge}, Second largest: {slarge}")

# approach2


        










#prime number
#
# a = [1, 3, 5, 7, 9]
#
# for num in a:
#     if num > 1:
#         for i in range(2, num):
#             if num % i == 0:
#                 print(num, "is NOT a prime number")
#                 break
#         else:
#             print(num, "is a PRIME number")
#     else:
#         print(num, "is NOT a prime number")






# a=[1,2,3,5,6,6,7,8,9]
#
# for num in a:
#     if num>1:
#         for i in range(2,num):
#             if num%i==0:
#                 print(num,"not a prime")
#                 break
#
#         else:
#              print(num,"prime")
#     else:
#         print(num,"not a prime")

# approach2
# num = 2
# ct = 0
#
# if num > 1:
#     for i in range(1, num + 1):
#         if num % i == 0:
#             ct += 1
#     if ct == 2:
#         print("prime")
#     else:
#         print("not a prime")
# else:
#     print("not a prime")

# num=[1,2,3,4,5,6,7,8,9]
# for i in num:
#     if i>1:
#         for j in range(2,i):
#             if i%j==0:
#                 print(i,"not a prime")
#                 break
#         else:
#             print(i,"prime")
#     else:
#         print(i,"not a peime")

#
# a=[1,2,3,4,5,5,6,6,7]
# for i in a:
#     if i>1:
#         for j in range(2,i):
#             if i%j==0:
#                 print(i,"Not a prime")
#                 break
#         else:
#             print(i,"prime")
#     else:
#         print(i,"pure not a prime")
#
# a = [1, 2, 3, 4, 5, 6, 7]
#
# for i in a:
#     x = 0  # reset counter for each number
#     if i > 1:
#         for j in range(1, i + 1):
#             if i % j == 0:
#                 x += 1
#         if x == 2:
#             print(i, "prime")  # print actual number
#         else:
#             print(i, "not a prime")
#     else:
#         print(i, "purely not a prime")

















