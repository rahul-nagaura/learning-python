# loops in python 
# While and for loop in python 

# count = 1; 
# n=int(input('Enter the number which table you want:'));
# while count <= 10:
#     print(count*n)
#     count +=1;

# count = 1; 
# while count <= 100:
#     print(count)
#     count+=1;

# count = 100;
# while count >= 0:
#     print(count)
#     count -=1;


# list = [1,4,9,16,25,36,49,64,81,100];
# count = 0;
# n = len(list);
# print(n);
# while count < n:
#     # print(count)
#     print(list[count])
#     count+=1;


# list = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# # num = int(input('Enter a number you are going to search: '))
# num =812

# count = 0
# isSearch = False
# n = len(list)

# while count < n:
#     if list[count] == num:
#         isSearch = True
#         break
#     count += 1

# if isSearch:
#     print("Yes")
# else:
#     print("No")




# For loop 
# list = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# for el in list:
#     print(el);

# list = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# isTrue = True
# n = int(input('enter a number'))
# for num in list:
#     if num == n:
#         isTrue = False
# if isTrue:
#     print("NO")
# else:
#     print("Yes");

# range() --> (start, stop,step)
# stop is not included 
# for i in range(10): stop 
#     print("hi",1)

# for i in range(0,10):
#     print(i,"Hi how are you ") range(start,start)

# for i in range(0,10,2):  range(start,start,step)
#     print('Hi: ',i)

# pass is used to done nothing 
# for i in range(5):
#     pass
# print("pass used to do nothing");

sum = 0;
for ele in range(0,100,1):
    sum = sum+ele
print(sum)


