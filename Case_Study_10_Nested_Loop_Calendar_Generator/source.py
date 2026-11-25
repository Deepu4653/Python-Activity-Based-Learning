# Nested Loop Calendar Generator
# Student: Leela Deepak Golukonda | Roll No: 26000521

print("MONTHLY CALENDAR GENERATOR")
print("=" * 40)

month_name = "March"
year = 2025
start_weekday = 6   # 0=Sun ... 6=Sat (March 2025 starts on Saturday)
days_in_month = 31

print("      %s %d" % (month_name, year))
print("Su Mo Tu We Th Fr Sa")
print("-" * 21)
line = ""
for i in range(start_weekday):
    line = line + "   "
for day in range(1, days_in_month + 1):
    line = line + "%2d " % day
    if (start_weekday + day) % 7 == 0:
        print(line)
        line = ""
if line != "":
    print(line)
print("-" * 21)
