import datetime

# It gives current date and time
x = datetime.datetime.now()

m = x.strftime("%Y")   # Full year with century: 2026
n = x.strftime("%y")   # Only last two digits of year: 26

o = x.strftime("%b")   # Short month name: Aug
p = x.strftime("%B")   # Full month name: August

q = x.strftime("%M")   # Minutes
r = x.strftime("%m")   # Month number

s = x.strftime("%S")   # Seconds

t = x.strftime("%H")   # Hour in 24-hour format
u = x.strftime("%I")   # Hour in 12-hour format

v = x.strftime("%p")   # AM/PM

print(m)
print(n)
print(o)
print(p)
print(q)
print(r)
print(s)
print(t)
print(u)
print(v)

#/| Code | Meaning      | Example  |
#/| ---- | ------------ | -------- |
#/| `%Y` | Full year    | `2026`   |
#/| `%y` | Short year   | `26`     |
#/| `%b` | Short month  | `Aug`    |
#/| `%B` | Full month   | `August` |
#/| `%m` | Month number | `08`     |
#/| `%M` | Minutes      | `05`     |
#/| `%S` | Seconds      | `30`     |
#/| `%H` | 24-hour      | `14`     |
#/| `%I` | 12-hour      | `02`     |
#/| `%p` | AM/PM        | `PM`     |
