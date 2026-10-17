def security_check(f):

    def wrapper():
        num = 0
        while num < 3:
            code = int(input("write the secret code to get the password: "))
            if code == 123:
                f()
                break
            else:
                print("access denied!")
                num += 1
        if num == 3 :
            print("system locked!")
    return wrapper()


@security_check
def show_pass():
    print("access granted")
    print("your password is 1384")
