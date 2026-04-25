from datetime import datetime,timedelta,timezone



print(datetime.now())
current_date_time = datetime.now()

print(f"date ::- {current_date_time.date()}")

print(f"Day ::- {current_date_time.day}")

print(f"Moth ::- {current_date_time.month}")

print(f"Year ::- {current_date_time.year}")

# time 

print("\n**************** Time ***********************\n")
print(current_date_time.time())
print(current_date_time.hour)
print(current_date_time.minute)

print("\n**************** Time Delta ***********************\n")
expiry = current_date_time + timedelta(days=10)
print(expiry)

print(current_date_time)
expiry = current_date_time +timedelta(hours=24)
print(expiry)





