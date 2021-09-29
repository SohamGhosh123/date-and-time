from datetime import date
from datetime import time
from datetime import datetime,timedelta
D=date.today()
print(D)
s=date(2021,9,29)
print(s)
T=time(5,45,10)
print(T)
DT=datetime(2021,9,29,5,46,50)
print(DT.strftime("%d/%m/%Y    :     %H/%M/%S"))
age=DT-timedelta(days=4380)
print(age)