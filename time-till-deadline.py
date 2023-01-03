# a)Accepts user input of goal and a deadline
# b) print back
# how much time remains untill deadline
from datetime import datetime

user_input = input("enter your goal with a deadline separated by colon\n")

#date format = 13.02.2021
input_list = user_input.split(':')

goal = input_list[0]
deadline = input_list[1]

deadline_date = datetime.strptime(deadline, '%d.%m.%Y') # module.definition of module




#Output split that  into lists,very important to know here both of these lists are strings,
#  because end user intrepetted as strings ,so we need to convert date from string format
# by using datetime module
# This datetime module can create a date,formatting the dates,updating the value


#Calculation - how many days from now till deadline
today_date = datetime.today()
time_till = deadline_date - today_date
hours_till = int(time_till.total_seconds() / 60 / 60)
print(f'Dear user time reamining for your goal: {goal} is {time_till}') #if include time_till.days it only shows days
print(f'Dear user time reamining for your goal: {goal} is {time_till.days}')
print(f'Dear user time reamining for your goal: {goal} is {hours_till} hours')


