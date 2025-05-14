# Find second largest number in list
#
# a=[8,4,9,5,6,7,2,3,4]
# if a[0]>a[1]:
#     flarge=a[0] #8
#     slarge=a[1] #4
#
# else:
#     flarge = a[1]
#     slarge = a[0]
#
# for i in range(2,len(a)):
#     if a[i]>flarge:
#         slarge=flarge
#         flarge=a[i]
#
#     elif a[i]>slarge:
#         slarge=a[i]
# print("slarge",slarge,"flarge",flarge)


# Third heighest

# a = [8, 4, 9, 5, 6, 7, 2, 3, 4]
#
# # First, second, and third largest initialized
# if a[0] > a[1]:
#     flarge = a[0] #8
#     slarge = a[1]  #4
# else:
#     flarge = a[1]
#     slarge = a[0]
# tlarge = float('-inf')  # Start with very low number
#
# for i in range(2, len(a)):
#     if a[i] > flarge:
#         tlarge = slarge
#         slarge = flarge
#         flarge = a[i]

#     elif a[i] > slarge and a[i] != flarge:
#         tlarge = slarge
#         slarge = a[i]

#     elif a[i] > tlarge and a[i] != slarge and a[i] != flarge:
#         tlarge = a[i]
#
# print("1st highest (flarge):", flarge)
# print("2nd highest (slarge):", slarge)
# print("3rd highest (tlarge):", tlarge)

# prime numbers or nt

# a=[1,2,3,4,5,6,7,8,9]
# for i in a:
#     if i>1:
#         for j in range(2,i):
#             if i%j==0:
#                 print(i,"Not a prime")
#                 break
#         else:
#             print(i,"prime")
#     else:
#         print(i,"purely not a prime")

# approach2

# a=[1,2,3,4,5,6,7]
# for i in a:
#     count=0
#     if i>1:
#         for j in range(1,i+1):
#             if i%j==0:
#                 count+=1
#         if count==2:
#             print(i,"prime")
#         else:
#             print(i,"not a prime")
#     else:
#         print(i,"purely not a prime")




# def a(i):
#     result=[]
#     count=0
#
#     for j in i:
#         if j!=0:
#             result.append(j)
#         else:
#             count+=1
#     result.extend([0]*count)
#     return result
#
# x=[1,2,0,3,4,0,2,2]
# y=a(x)
# print(y)

# a=[1,2,0,3,4,5,0,1]
# r=[]
# c=[]
#
# for i in a:
#     if i!=0:
#         r.append(i)
#     else:
#         c.append(i)
# r.extend(c)
# print(r)


# swapping 2 numbers
#
# num1=10
# num2=20
#
# print(num1)
# print(num2)
#
# temp=num1
# num1=num2
# num2=temp
# print(num1,num2)

# factorial of a number

# factor=1
# num=5
#
# if num<0:
#     print("Factor does not exist")
# elif num==0:
#     print("Factor 0 does not exist")
# else:
#     for i in range(1,num+1):
#         factor=factor*i
# print(factor)

# approach2

# def fact(n):
#     if n==0 or n<1:
#         return 1
#     else:
#         return n*fact(n-1)
#
# a=fact(5)
# print(a)


# def s(a):
#     for i in a:
#         if isinstance(i, dict):
#             for j in i:
#                 print(j, i[j])
#                 if isinstance(i[j], dict):
#                     s([i[j]])  # Recursively call the function for nested dictionaries
#         elif isinstance(i, tuple):
#             for k in i:
#                 print(k)
#
# a = [
#     {
#         "Name": "uday",
#         "Details": {"age": 24, "place": "kuppam"}
#     },
#     (1, 2, 3, 4)
# ]
#
# s(a)  # No need to assign it to `u` because `s(a)` prints directly

# Finosis series

# 0,1,1,2,3,5,8,13,21

# n1=0
# n2=1
# for i in range(1,10):
#     sum=n1+n2
#     print(sum)
#     n1=n2
#     n2=sum


#sum of numbers in list

# a=[1,2,3,4,5]
# sum=0
# for i in a:
#     sum=i+sum
# print(sum)

# approach2

# a=[1,2,3,4,5]
# print(sum(a))

#find maximum number in array

# a=[2,4,6,7,8,9,2,4]
# b=a[0]
# for i in a:
#     if i>b:
#         b=i
# print(b)

# a=[6,8,3,4,5,2]
# b=a[0]
#
# for i in range(1,len(a)):
#     if b<a[i]:
#         b=a[i]
#
# print(b)

# how to find lengeth

# a=[1,2,3,4,5,6,7,8]
# count=0
#
# for i in a:
#     print(i)
#     count+=1
# print("total count",count)

# a=[1,2,3]
#
# first=a[0]  #1
# last=a[-1]  #3
# a[0]=last
# a[-1]=first
#
#
# print(a)

# a=10
# b=20
#
# temp=a
# a=b
# b=temp
# print(a,b)

#swap
# a,b=10,20
# a,b=b,a
# print(a,b)

#swap list

# a=[1,2,3,4,5,6,7]
# post1,post2=0,6
# first_e=a.pop(post1)
# last_e=a.pop(post2-1)
#
# a.insert(post1,last_e)
# a.insert(post2,first_e)
# print(a)

# approach3
# a=[1,2,3,4,5,6]
#
# first=a.pop(0)
# last=a.pop(-1)
# a.insert(0,last)
# a.append(first)
# print(a)


# approach2
# a=[1,2,3,4,5,6,7]
# a[0],a[6]=a[6],a[0]
# print(a)

# Approach4
# a=[1,2,3,4,5,6,7]
# size=len(a)
# print(size)
#
# first=a[0]
# last=a[size-1]
#
# a[0]=last
# a[size-1]=first
#
# print(a)

#how to remove nth element in lis
# a = ["uday", "nirmal", "balaji"]
# for i in a:
#     if i == "uday":
#         a.remove(i)
# print(a)  # Output: ['nirmal', 'balaji']
#
#
#
# for i in range(len(a)):
#     if a[i] == "nirmal":
#         del a[i]
#         break  # Needed to stop after deletion
#
# print(a)


#how to search for an eleemnt in alist
# a=[1,2,3,4,5,6,7,8]
# b=2
#
# for i in a:
#     if i==b:
#         print("yes")

#reverse a list
a = [1, 2, 3, 4, 5]
a.reverse()
print(a)
# b = []
# for i in a:
#     b = [i] + b  # Concatenate each element at the beginning of b
# print(b)

# a="welcome to uday"
# b=""
# for i in a:
#     b=i+b
# print(b)

#sum of list
# a = [1, 2, 3, 4, 5]
# c=0
# for i in a:
#     c=i+c
# print(c)

# copy list

# a=[1,2,3,4]
# b=[5,6,7,8]
# for i in b:
#     a.append(i)
# print(a)


# a = [1, 2, 3, 4,1,2, 5, 6]
# b = {}

# for i in a:
#     if i in b:
#         b[i] += 1
#     else:
#         b[i] = 1
#
# print(b)

# a=[1,2,3,4,5,6]
# a[0],a[-1]=a[-1],a[0]
# print(a)

# a=[1,2,3,4,5]
# f=a[0]
# l=a[-1]
# a[0]=l
# a[-1]=f
# print(a)
#
# a=[1,2,3,9,4,5,6]
#
# if a[0]>a[1]:
#     flarge=a[0]
#     slarge=a[1]
#
# else:
#     flarge = a[1]
#     slarge = a[0]
#
# tlarge = float('-inf')
#
# for i in range(2,len(a)):
#     if a[i]>flarge:
#         slarge=flarge
#         flarge = a[i]
#
#     elif a[i]>slarge:
#         slarge=a[i]
#
# print(flarge,slarge)

#prime number

# a=[1,2,3,4,5,6,7,8,9,10,11,12]
#
# for i in a:
#     count = 0
#     if i>1:
#         for j in range(1,i+1):
#             if i%j==0:
#                 count+=1
#         if count==2:
#             print(i,"prime")
#         else:
#             print(i,"not a prime")
#     else:
#         print("purely not a prime")

#finosis

#0,1,1,2,3

# n1=0
# n2=1
#
# for i in range(1,10):
#     sum=n1+n2
#     print(sum)
#     n1=n2
#     n2=sum


# mutlipy list

# a=[1,2,3,4,5]
# z=1
# for i in a:
#     z=i*z
# print(z)

# a="welcome to python"
# s=a.split()
# x=s[::-1]
# y=" ".join(x)
# print(y)

# print(s)

# a="welcome to uday"
#
# if "uday" in a:
#     print("yes")

# import re
# a = "welcometopython@gmai.com^&$@"
#
# regex = re.compile(r"[^a-zA-Z0-9@.\s]")
#
# if regex.search(a):
#     print("Special characters found")
# else:
#     print("No special characters found")

# a=[1,0,2,0,1,2]
# b=[]
# c=[]
# for i in a:
#     if i>0:
#         b.append(i)
#     else:
#         c.append(i)
#
# b.extend(c)
# print(b)

# a=[1,0,2,0,1,2]
# b=[]
# count=0
#
# for i in a:
#     if i>0:
#         b.append(i)
#     else:
#         count+=1
# b.extend([0]*count)
# print(b)





# s =[1,1,0,0,1,0,1,2]
# #sequence changed count 1 to 0 or 0 to 1
# count =0
# for i in range(len(s)):
#     if s[i+1] != s[i]:
#         count +=1
#
#
# print(count)

# a=[1,2,3,4,5,6,7,8]
# for i in a:
#     count=0
#     if i>1:
#         for j in range(1,i+1):
#             if i%j==0:
#                 count+=1
#         if count==2:
#             print(i,"prime")
#         else:
#             print(i,"not a prime")
#
#     else:
#         print(i,"purely notba prime")
#



# a=[4,2,3,4,5,6,79,1,2,43]
#
# if a[0]>a[1]:
#     flarge=a[0]
#     slarge=a[1]
# else:
#     flarge=a[1]
#     slarge=a[0]
#
# for i in range(2,len(a)):
#     if a[i]>flarge:
#         slarge = flarge
#         flarge=a[i]
#
#     elif a[i]>slarge:
#         slarge=a[i]
#
#
# print(flarge,slarge)







