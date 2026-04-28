def pick_even(*args):
    my_list=[]
    for i in args:
        if i%2==0:
            my_list.append(i)
    return my_list

print(pick_even(1,2,3,4,5,6))     
