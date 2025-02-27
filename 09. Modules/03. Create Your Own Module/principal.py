import bday_messages as ms
import datetime

today = datetime.date.today()

next_birthday = datetime.date(2026, 1, 23)

days_away = next_birthday - today

if today == next_birthday:
    print(ms.random_message)
else:
    print(f'My next birthday is {days_away} days away!')
    