# -- To read a file 
# f = open('demo.txt', 'r')
# data = f.read()
# print(data)
# f.close()

# -- To write a file 
# f = open('demo.txt','w')
# f.write('I am Rahul Nagaura. I am learning new language')
# f.close()


# -- To append a something 
# f = open('demo.txt','a')
# f.write('\nI am third year student')
# f.close()


# r+ read overwrite pointer start no turncate
# w+ read overwrite pointer start turncate
# a+ read append pointer end no turncate


# with syntax --> with automatically close the file so no need to use f.close()
# with open('demo.txt','r') as f:
#     data = f.read()
#     print(data)

# with open('demo.txt', 'w') as f:
#     data = f.write('This is new file')
#     print(data)


# # Deleting a function 
# import os
# os.remove('sample.txt')

# f = open('sample.txt', 'w')
# data = f.write('Hi everyone\nwe are learning File I/O\nusing Java\nI like programing in Java')
# print(data)

# f = open('sample.txt', 'r')
# data = f.read()
# new_data = data.replace('Java','python')
# print(new_data)

# w = open('sample.txt', 'w')
# data1 = w.write(new_data)
# print(data1)
# f.close()


f = open('num.txt', 'r')
data = f.read()
print(data)

# 1st method 
# num = ''
# for i in range(len(data)):
#     if(data[i] == ','):
#         print(int(num))
#         num = ''
#     else:
#         num = num+data[i]

# 2nd method    
# nm = data.split(',')
# print(nm)

# for ele in nm:
#     if(int(ele)%2 == 0):
#         print(ele,': even')
#     else:
#         print(ele,': odd')





