from datetime import datetime

def calculate(usersdate):
    today=datetime.today()
    ages=today.year-usersdate.year
    if today.month<usersdate.month or (today.month==usersdate.month and today.day<usersdate.day):
        ages-=ages
    return ages

usersbirth=input("enter your birthday like DD.MM.YYYY:")
frmat="%d.%m.%Y"
x=datetime.strptime(usersbirth,frmat)
print(f"Your age:{calculate(x)}")
