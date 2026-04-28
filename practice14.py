names=["asal","sara","hassan","ali","maryam"]
short_names=filter(lambda x:len(x)<=4,names)
new_list=[]
for i in short_names:
    new_list.append(i)
print(new_list)    