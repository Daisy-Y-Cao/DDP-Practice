# Enter your code here. Read input from STDIN. Print output to STDOUT
import calendar
m, d, y=map(int, input().split())
d = calendar.weekday(y, m, d)
print(calendar.day_name[d].upper())
