def sum_numbers(*args):
    sum=0
    for i in args:
        sum+=i
    return sum

print(sum_numbers(2,4,5,2,1))           
