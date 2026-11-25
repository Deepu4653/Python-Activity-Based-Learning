# University Scholarship Allocation
# Student: Leela Deepak Golukonda | Roll No: 26000521

# Each applicant: (name, aggregate, [sub1, sub2, sub3, sub4], attendance, income)
applicants = [
    ("Aarav", 88.2, [82, 79, 90, 85], 92, 180000),
    ("Bhavya", 76.5, [70, 65, 72, 68], 88, 250000),
    ("Charan", 91.0, [88, 90, 85, 92], 95, 150000),
    ("Divya", 69.0, [60, 58, 62, 55], 80, 120000),
    ("Esha", 84.0, [80, 78, 82, 79], 90, 300000),
    ("Farhan", 81.5, [77, 75, 80, 79], 85, 140000),
]

MIN_AGG = 75.0
MIN_SUB = 60
MIN_ATT = 75
MAX_INCOME = 250000

print("UNIVERSITY SCHOLARSHIP ALLOCATION")
print("=" * 50)
print("Eligibility: Aggregate >= %.1f, Each subject >= %d," % (MIN_AGG, MIN_SUB))
print("Attendance >= %d%%, Family income <= %d" % (MIN_ATT, MAX_INCOME))
print("=" * 50)

eligible = []
for (name, agg, subs, att, inc) in applicants:
    sub_ok = True
    for s in subs:
        if s < MIN_SUB:
            sub_ok = False
    if agg >= MIN_AGG and sub_ok and att >= MIN_ATT and inc <= MAX_INCOME:
        eligible.append((name, agg, att, inc))

# rank by aggregate desc, tie by attendance desc
ranked = sorted(eligible, key=lambda x: (x[1], x[2]), reverse=True)

print("\nTotal applicants:", len(applicants))
print("Eligible applicants:", len(eligible))
print("\nRanked eligible list:")
print("-" * 50)
rank = 1
for (name, agg, att, inc) in ranked:
    print("%2d. %-10s Agg: %.1f  Att: %d%%  Income: %d" % (rank, name, agg, att, inc))
    rank += 1

if len(ranked) == 0:
    print("No eligible candidates found.")
