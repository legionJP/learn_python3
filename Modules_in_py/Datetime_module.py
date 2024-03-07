import datetime

d= datetime.date(2011,7,17)
print(d)

today =datetime.date.today()
print(today.day)

print(today.weekday()) #where monday ==0 , sunday==6
print(today.isoweekday()) #monday ==1 , sunday =6 )
print(today.isocalendar())

# finding the date from today to nextdays 

tdelta = datetime.timedelta(days=30)
print(today+tdelta)
print(today-tdelta)
