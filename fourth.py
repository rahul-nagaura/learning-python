# Dictionary in python


student = {
    "name": "rahul",
    "sub": {
        "ch": 98,
        "math": 89,
        "phy": 56
    },
    "roll_no": '22JE0764'
}
# print(student);
# print(student['name']);
# student["surname"] = 'nagaura';
# print(student);

# print(student['sub']['ch']);

# print(student.keys());
# print(list(student.keys()));
# print(student.values()); #return all the values of the dic......

# print(student.items()); #retrun all the key and values in paires......
# print(list(student.items()));

# SET in python 
# set is mutable but it's element's are immutable 
# immutable --> hashvalue --> same beacuse they n didn't change in life --> hashable
# unordered items 
# each set of the item is unique and immutable 
# int,boolean,float,str,tuple --> stored in the set
# but dic and list are not stored in tuple 
# unhashable --> dic,list, set 


num = {1,2,3,4,5,6,7,8};

# if there are some repetable values then set ignore these values
# len --> total number of  items duplicate values are ignored


# empty set syntax : collection = set(); 
print(num);
print(type(num));

# use of add function --> to add values in given set
# num.add(56);
# num.add("ram");
print(num);


# use of remove function --> to remove a given value from set 
# num.remove('56');

# use of clear function --> to clear all the element within the set 
# num.clear();
# print(num);

# pop --> remove a random values form the set 
# print(num.pop());
# print(num.pop());
# print(num);


# union & intersection method 
a = {1,2,3,4,5,6,7,8};
b = {5,3,6,7,8,2,10,9,11};
# retrun a new set 
print(a.union(b)); # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}

# intersection --> common element 
print(a.intersection(b)); #{2, 3, 5, 6, 7, 8}


