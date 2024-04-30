# div_by_3 = [x for x in range(0,100) if x % 3 == 0]
# print(div_by_3)
# import copy


# my_ls = [[1],2,3]
# def double_list(ls):
#     new_list = [i for i in ls]
#     length = len(new_list)
#     i = 0
#     while(i < length):
#         new_list.append(new_list[i])
#         i += 1
#     return new_list
# list1 = double_list(ls)
# list1[2].append(4)
# print(list1)

# def new_list2(ls):
#     if(not len(ls)):
#         return []
#     if(isinstance(ls[0], list)):
#         return  ls + [x for x in ls[0]] + new_list2([x for x in ls[1:]])
#     else:
#         return  ls + [ls[0]] + new_list2([x for x in ls[1:]])

# lss = new_list2(my_ls)
# print(new_list2(my_ls))
# lss[0].append(6)
# print(lss)

# import matplotlib.pyplot as plt
# import numpy as np

# x = np.linspace(0,20,100)
# plt.plot(x, np.sign(x))
# plt.show()

# import time

# def first_element(lst):
#     return lst[0]

# my_list = [1, 2, 3, 4, 5]
# print(first_element(my_list))

# def find_max(lst):
#     max_num = lst[0]
#     for num in lst:
#         if num > max_num:
#             max_num = num
#     return max_num

# my_list = [3, 7, 2, 9, 5]
# print(find_max(my_list))  # Output: 9


# def binary_search(arr, target):
#     low = 0
#     high = len(arr) - 1
#     while low <= high:
#         mid = (low + high) // 2
#         if arr[mid] == target:
#             return mid
#         elif arr[mid] < target:
#             low = mid + 1
#         else:
#             high = mid - 1
#     return -1

# my_list = [2, 3, 5, 7, 9, 11, 13]
# print(binary_search(my_list, 9)) 


# def fibonacci(n):
#     if n <= 1:
#         return n
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)

# start = time.time()
# print(fibonacci(5))
# end = time.time()

# print(1000 * (end - start))

# start = time.time()
# print(fibonacci(50))
# end = time.time()

# print(1000 * (end - start))

# def wrapper_check_int(fn):
#     def wrapper(*args,**kwargs):
#         try:
#             fn(*args,**kwargs)
#         except Exception as e:
#             print(e)
#     return wrapper

# @wrapper_check_int
# def multiply(num1, num2):
#     print(f'The multiply result is: {num1 * num2}')
    
# @wrapper_check_int
# def divide(num1, num2):
#     print(f'The divide result is: {num1 / num2}')

# multiply(5, 9)

# multiply({}, 7)

# divide(10, 2)

# divide("", 2)

import bcrypt 

# example password 
password = 'password123'

# converting password to array of bytes 
bytes = password.encode('utf-8') 

# generating the salt 
salt = bcrypt.gensalt() 

# Hashing the password 
hash = bcrypt.hashpw(bytes, salt) 

print(hash)
