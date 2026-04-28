def number_of_even (n):
    count = 0
    for i in n:
        if i%2==0:
            count+=1
    return count

tedad=number_of_even([1,4,3,8,7,5,9,13,75,32,28])
print(tedad)        