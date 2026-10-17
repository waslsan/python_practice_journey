from datetime import datetime


def time(f):
    now = datetime.now()
    minute = now.minute
    if minute % 2 == 0:
        f()
    else:
        print("it's fard")


@time
def zoj():
    num = (2, 4, 6, 8, 10)
    print(num)
