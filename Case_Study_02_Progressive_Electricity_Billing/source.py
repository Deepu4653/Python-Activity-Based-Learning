# Progressive Electricity Billing
# Student: Leela Deepak Golukonda | Roll No: 26000521

print("PROGRESSIVE ELECTRICITY BILLING")
print("=" * 40)

# Slab rates (Rs per unit)
# 0-100   : 5
# 101-200 : 7
# 201-300 : 9
# >300    : 11
# fixed charge = 50, surcharge 5% if bill>500, rebate 2% if units<150

months = [("Jan", 120), ("Feb", 145), ("Mar", 210), ("Apr", 330), ("May", 95)]

print("%-8s %5s   %8s" % ("Month", "Units", "Bill(Rs)"))
print("-" * 30)
bills = []
for (month, units) in months:
    if units <= 100:
        cost = units * 5
    elif units <= 200:
        cost = 500 + (units - 100) * 7
    elif units <= 300:
        cost = 500 + 700 + (units - 200) * 9
    else:
        cost = 500 + 700 + 900 + (units - 300) * 11
    bill = cost + 50
    if units < 150:
        bill = bill - bill * 0.02
    if bill > 500:
        bill = bill + bill * 0.05
    bill = round(bill, 2)
    bills.append((month, units, bill))
    print("%-8s %5d   %8.2f" % (month, units, bill))

print("\nUnusual increase check (>50% rise in units):")
flagged = False
for i in range(1, len(bills)):
    pu = bills[i - 1][1]
    cu = bills[i][1]
    if pu > 0 and (cu - pu) / pu > 0.5:
        print("  %s -> %s : %.0f%% increase (UNUSUAL)" % (bills[i-1][0], bills[i][0], (cu - pu) / pu * 100))
        flagged = True
if not flagged:
    print("  No unusual increases detected.")
print("Analysis complete.")
