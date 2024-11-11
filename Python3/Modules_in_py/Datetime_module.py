import datetime
import pytz
d= datetime.date(2011,7,17)
print(d)

t_day =datetime.date.today()
print(t_day.day)

print(t_day.weekday()) #where monday ==0 , sunday==6
print(t_day.isoweekday()) #monday ==1 , sunday =6 )
print(t_day.isocalendar())

#---------------------------------------------------------
# finding the date from today to nextdays and vice versa
#-------------------------------------------------------
tdelta = datetime.timedelta(days=30)
print(t_day+tdelta)
print(t_day-tdelta)

bday = datetime.date(2024,5,3)
till_bday = bday-t_day
print(till_bday)
print(till_bday.days)
print(till_bday.total_seconds())

#--------------------------------
# Working with the time
#--------------------------------

T = datetime.time(10,30,30,1000)
T== datetime.datetime(2023,12,24,10,30,30,10000)
print(T)
t= datetime.datetime.today()

print(t.time())
print(t.date())
#printing the next time with hours different
tdelta =datetime.timedelta(hours=13)
print(t+tdelta)

t_today= datetime.datetime.today() #return the datetime with cuurrent local time zone
t_now= datetime.datetime.now(tz=pytz.UTC) # gives the option to pass on the time zone 

t_utcnow=datetime.datetime.utcnow() #this give the current utc time
#t_now= datetime.datetime.utcnow().replace(tzinfo=pytz.UTC) 
print(t_today) 
print(t_now)
print(t_utcnow)

T1 = datetime.datetime(2023,12,24,10,30,30, tzinfo=pytz.UTC)
print(T1)

t_z = t_utcnow.astimezone(pytz.timezone('Asia/Calcutta'))
print(t_z)

for tz in pytz.all_timezones:
     print(tz)

'''    
tm_now =datetime.datetime.now(tz=pytz.timezone('Asia/Kolkata'))
my_tmz=pytz.timezone('Asia/Kolkata')
tm_now=my_tmz.localize(my_tmz)
tm_kolkata=my_tmz.astimezone(pytz.timezone('Aisa/Kolkata'))

'''
#-----------------------
#format code of datetime
#------------------------
dt__kolkata= datetime.datetime.now(tz=pytz.timezone('Asia/Kolkata')) 
print(dt__kolkata.strftime('%B %d , %Y'))   #datetime to string
dt_str =' March 7 ,2016 '
dt2 = datetime.datetime.strptime(dt_str,'%B %d , %Y') # string to datetime
print(dt2)