def skyline(*args):
    highest=-1
    for i in args:
        if i>highest:
            highest=i
    return highest

print(skyline(3,7,15,2,9))        
