names=["asal","sara","ali","fatemeh"]
infos={
    "asal":{"age":20,"score":19},
    "ali":{"age":19,"score":17},
    "fatemeh":{"age":21,"score":18}
    }
for name in names:
    if name in infos:
        x=f"name is {name} and they are {infos[name]["age"]} years old"
    else:
        x=f"there is no info about {name}"
    print(x)        