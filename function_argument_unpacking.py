#Function argument unpacking 
def myfunc(x,y,z):
    print(x,y,z)

tuple_vec = (1,2,3)
dict_vec = {"x":1,"y":2,"z":3}

myfunc(*tuple_vec) # 1 2 3
myfunc(**dict_vec) # 1 2 3
