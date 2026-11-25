# ATM Transaction Sequence Simulation
# Student: Leela Deepak Golukonda | Roll No: 26000521

print("ATM TRANSACTION SEQUENCE SIMULATION")
print("=" * 45)

balance = 5000
WITHDRAW_LIMIT = 4000
transactions = [
    ("deposit", 2000),
    ("withdraw", 1500),
    ("withdraw", 5000),   # exceeds limit -> reject
    ("withdraw", 1000),
    ("deposit", 500),
    ("withdraw", 3000),
    ("withdraw", -200),   # invalid
]

print("Starting balance: Rs", balance)
print("-" * 45)
for (t, amt) in transactions:
    if t == "deposit":
        if amt <= 0:
            print("Invalid deposit amount", amt, "-> REJECTED")
            continue
        balance = balance + amt
        print("Deposit  Rs %5d -> Balance Rs %d" % (amt, balance))
    elif t == "withdraw":
        if amt <= 0:
            print("Invalid withdrawal amount", amt, "-> REJECTED")
            continue
        if amt > WITHDRAW_LIMIT:
            print("Withdraw Rs %5d -> EXCEEDS LIMIT -> REJECTED" % amt)
            continue
        if amt > balance:
            print("Withdraw Rs %5d -> INSUFFICIENT FUNDS -> REJECTED" % amt)
            continue
        balance = balance - amt
        print("Withdraw Rs %5d -> Balance Rs %d" % (amt, balance))
    else:
        print("Unknown transaction", t, "-> REJECTED")

print("-" * 45)
print("Final balance: Rs", balance)
