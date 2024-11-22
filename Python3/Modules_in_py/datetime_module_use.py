

#----------------------------------------------------------------------------------------------#
#          Calculate Number of Days , Weeks or Months to Reach Specific goals 
#           Using the Datetime Modules
#----------------------------------------------------------------------------------------------#

import datetime
import calendar

#----------------------------------------------------------------------------------------------#
#                    Making the pay off the credit card bill
#----------------------------------------------------------------------------------------------#

balance = 6000
interset_rate =13 *.01
monthly_payment = 623

today = datetime.date.today()
days_in_current_month = calendar.monthrange(today.year,today.month)[1] #year , month
print(days_in_current_month)

days_till_end_month= days_in_current_month-today.day
print(days_till_end_month)


start_date = today + datetime.timedelta(days=days_till_end_month+1) #staring on the month of the first adding the 1 
end_date = start_date #for new month date 

while balance > 0:
    interset_charge = (interset_rate/12)*balance
    balance+= interset_charge
    balance-= monthly_payment

    balance = round(balance,2)
    if balance < 0 :  #setting the balance  to equal to 0 
        balance = 0
    #balance = 0 if balance<0 else round(balance,2)

    print(end_date, balance)
    days_in_current_month = calendar.monthrange(end_date.year, end_date.month)[1] #get the days in the month 
    end_date = end_date + datetime.timedelta(days= days_till_end_month) #then the next month increment



#------------------------------------------------------------------
# Finding the Number of week days to loose the certain weight and goal date
#------------------------------------------------------------------------

import datetime

current_weight = 220
goal_weight = 180

avg_kg_week = 1.5

start_date1 = datetime.date.today()
end_date1 = start_date1

while current_weight > goal_weight:
    end_date1 += datetime.timedelta(days=7)
    current_weight -= avg_kg_week

print(f' You can reach to your goal in {(end_date1 - start_date1).days//7} weeks') #time delta has .days for end and start date

print(end_date1)


#-----------------------------------------------------
# finding the days to hit number of subscriber on channel
#--------------------------------------

import datetime
import math

goal_subscription = 1000000

current_subs = 100000

required_subs = goal_subscription -current_subs

avg_subs_day = 600

days_for_subs = math.ceil(required_subs/avg_subs_day)  # round up the value and Return the ceiling of x as an Integral.This is the smallest integer >= x.

today = datetime.date.today()
print(today + datetime.timedelta(days=days_for_subs))


