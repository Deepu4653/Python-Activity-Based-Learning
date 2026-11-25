# Hospital Billing and Patient Classification
# Student: Leela Deepak Golukonda | Roll No: 26000521

print("HOSPITAL BILLING AND PATIENT CLASSIFICATION")
print("=" * 45)

# patient: (name, category, consultation, diagnostics, treatment)
patients = [
    ("Ravi", "General", 300, 500, 2000),
    ("Sarla", "Senior", 300, 500, 2000),
    ("Kiran", "Child", 250, 300, 1500),
    ("Imran", "Insured", 400, 600, 3000),
    ("Meena", "General", 100, 200, -50),
]

print("%-8s %-9s %10s %8s" % ("Name", "Category", "Final(Rs)", "Class"))
print("-" * 45)
for (name, cat, cons, diag, treat) in patients:
    if cons < 0 or diag < 0 or treat < 0:
        print("%-8s INVALID billing (negative charge)" % name)
        continue
    concession = 0
    if cat == "Senior":
        concession = treat * 0.20
    elif cat == "Child":
        concession = treat * 0.10
    elif cat == "Insured":
        concession = treat * 0.15
    final = cons + diag + treat - concession
    final = round(final, 2)
    if final <= 1000:
        cls = "Low"
    elif final <= 5000:
        cls = "Medium"
    else:
        cls = "High"
    print("%-8s %-9s %10.2f %8s" % (name, cat, final, cls))
