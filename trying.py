# div_by_3 = [x for x in range(0,100) if x % 3 == 0]
# print(div_by_3)
import copy


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
