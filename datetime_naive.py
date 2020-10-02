from datetime import *

tday = date.today()
print(tday)
print(tday.year)
print(tday.weekday())
print(tday.isoweekday())

tdelta = timedelta(days=7)

print(tdelta)
leap = tday + tdelta
print(leap)

bday = date(2021, 4, 26)
till_bday = bday - tday
print(till_bday)
print(till_bday.total_seconds())
