from datetime import datetime, timedelta

data = datetime.now()
print("current date and time :", data) # 2025-07-10 21:41:37.403172
print("Get today date :", data.date()) # 2025-07-10
print("Get today's day :", data.day) # 10
print("Get current month :", data.month) # 7
print("Get current month :", data.year) # 2025

datetime_variable = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
print(datetime_variable) # 2025_07_10_21_47_55
# m :  month
# M :  Minutes
# H :  Hours
# S : Seconds
# d : day
# Y : Year : 2025
# y : Year : 25


print("_"*50)
# Future date of 2 days
future_date = data + timedelta(days=2)
print("future date :", future_date.date())  #future date : 2025-07-12

# previous date of 2 days before
previous_date = data - timedelta(days=2)
print("previous date :", previous_date.date()) # previous date : 2025-07-08

