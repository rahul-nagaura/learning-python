# def sum(a,b):
#     sum = a +b 
#     print(sum)
#     return sum

# sum(5,6)


# function definition 
# def  cal_sum(a,b):
#     return a+b

# def cal_avg(a,b,c):
#     sum = a+b+c
#     avg = sum/3
#     # print(avg)
#     return avg

# print('avg is ')
# print(cal_avg(1,2,3))
# print("Hello ",end ="")
# print("World")

# list1 = [1,2,3,4,5,6,7,8,9,10,23]
# cities = ['danta','sikar','pune','mumnbai','chenai']
# def cal_len(list):
#     return len(list)

# def print_list(list):
#     for el in list:
#         print(el," ",end="")

    
# print(cal_len(list1));
# print(cal_len(cities));
# print(print_list(list1))


def cal_fact(num):
    sum = 1
    for el in range(1, num+1):
        sum *=el
    return sum

print(cal_fact(5))

def conv_m(m):
    INR = 83.3*m
    return INR
 
print(conv_m(5))
