# Employee Payroll and Deduction Analysis
# Student: Leela Deepak Golukonda | Roll No: 26000521

print("EMPLOYEE PAYROLL AND DEDUCTION ANALYSIS")
print("=" * 50)

employees = [
    ("Ramesh", 40000, 5000, 10, 200, 3000),
    ("Sneha", 55000, 7000, 5, 250, 4000),
    ("Arjun", 30000, 3000, 8, 180, 1500),
]
# (name, basic, allowance, ot_hours, ot_rate, incentive)

print("%-8s %10s %10s %10s" % ("Name", "Gross", "Deduct", "Net"))
print("-" * 42)
for (name, basic, allw, ot, otr, inc) in employees:
    gross = basic + allw + ot * otr + inc
    pf = basic * 0.12
    if gross > 50000:
        tax = gross * 0.20
    else:
        tax = gross * 0.10
    ptax = 200
    deduct = pf + tax + ptax
    net = gross - deduct
    print("%-8s %10.2f %10.2f %10.2f" % (name, gross, deduct, net))

print("\n(Full statements are printed in detail section below)")
(name, basic, allw, ot, otr, inc) = employees[0]
gross = basic + allw + ot * otr + inc
pf = basic * 0.12
tax = gross * 0.20 if gross > 50000 else gross * 0.10
ptax = 200
deduct = pf + tax + ptax
net = gross - deduct
print("\nSALARY STATEMENT")
print("Employee        :", name)
print("Basic Pay       : Rs", basic)
print("Allowance       : Rs", allw)
print("Overtime (%d h)  : Rs %d" % (ot, ot * otr))
print("Incentive       : Rs", inc)
print("Gross Salary    : Rs %.2f" % gross)
print("PF (12%%)        : Rs %.2f" % pf)
print("Tax             : Rs %.2f" % tax)
print("Prof. Tax       : Rs %.2f" % ptax)
print("Total Deduction : Rs %.2f" % deduct)
print("Net Salary      : Rs %.2f" % net)
