import datetime

birthday_year = int(input("enter the year you were born: "))
birthday_month = int(input("enter the month you were born: "))
birthday_day = int(input("enter the day you were born: "))

my_birthday = datetime.date(birthday_year, birthday_month, birthday_day)
now = datetime.datetime.now()

my_age = now.year - my_birthday.year

print(f"my birthday is on {my_birthday}")
print(f"my birthday is on day {my_birthday.weekday()} of the week")
print(my_birthday.ctime())
print(f"and now it is {now}")
print(f"so i am {my_age} years old")