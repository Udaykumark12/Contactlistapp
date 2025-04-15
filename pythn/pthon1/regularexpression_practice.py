import re
# a="hello wolrd"
# print(re.match("he",a).group())
#
#
# import re
# a="hello wolrd"
# print(re.match(r'hello',a).group())

import re

# a = "Hello i am python 3.12 version,i am python 3.14 version"
# # Use re.sub() with a fixed regex pattern
# # c=re.compile(r'python \d+\.\d+')
# # print(re.sub(c,"udaaay",a))
# print(re.sub.ignorecase(r'python \d+\.\d+',"uday",a))

#meta characters
a = "Hllo i am python 3.12 version,i am python 3.14 version"
# print(re.search(r'[a-l]',a).group())
# print(re.search(r'^Hllo',a).group())
# print(re.search(r'versi$',a).group())
# print(re.search(r'a...',a).group()) #am p
# print(re.search(r'o.*',a).group()) # o i am python 3.12 version,i am python 3.14 version
# print(re.search(r'o.+',a).group()) # o i am python 3.12 version,i am python 3.14 version
# print(re.search(r'am?',a).group())

def a(n):
    if n==1:
        return 1
    else:
        return n *a(n-1)
print(a(5))