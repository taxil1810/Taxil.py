# list
# tuple
# set
# dictionary

# list
# mutable

# you can modify element after creation(add , change , remove)
# example

my_list = [1 , 2 , 3]

my_list[2] = 10

my_list.append(20)

del my_list[0]

print(my_list)

# tuple
# immutable

my_tuple = (1 , 2 , 3)

my_tuple[0] = 10

my_tuple[1]

print(my_tuple)

# set
# mutable

my_set = {1 , 2 ,3}

my_set.add(10)

print(my_set)

# dictionary
# mutable

my_dics = {"1":"alice" , "2":"vishakha" }

my_dics["1"] = "india"

my_dics["3"] = "english"

del (my_dics)

name1 = "taxil"
name2 = "manan"
name3 = "harshil"
name4 = "preet"
name5 = "falgun"

print (name1)
print (name2)
print (name3)
print (name4)
print (name5)

name_list = ("taxil" , "manan" , "harshil" , "preet" , "preet")

print(name_list[0])
print(name_list[1])
print(name_list[2])
print(name_list[3])
print(name_list[4])

for user in name_list:
    print(user)

# type   casting constructor

a = [1 , 2 , 3]

b = tuple(a)

c = set(b)

d = dict(c)

print(b)

print(c)

print(d)