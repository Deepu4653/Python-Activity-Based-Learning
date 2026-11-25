# Nested Loop Examination Seating Generator
# Student: Leela Deepak Golukonda | Roll No: 26000521

print("EXAMINATION SEATING ARRANGEMENT")
print("=" * 45)

rows = 4
cols = 5
students = ["S01", "S02", "S03", "S04", "S05", "S06", "S07", "S08", "S09", "S10",
            "S11", "S12", "S13", "S14", "S15", "S16", "S17", "S18", "S19", "S20"]
reserved = [(2, 2), (2, 3)]  # reserved (row, col) zero-indexed

seating = []
idx = 0
for r in range(rows):
    rowseats = []
    for c in range(cols):
        if (r, c) in reserved:
            rowseats.append("RSVD")
        elif idx < len(students):
            rowseats.append(students[idx])
            idx += 1
        else:
            rowseats.append("----")
    seating.append(rowseats)

print("Classroom: %d rows x %d cols" % (rows, cols))
print("Reserved seats:", reserved)
print("-" * 45)
for r in range(rows):
    line = ""
    for c in range(cols):
        line = line + "%-5s" % seating[r][c]
    print("Row %d: " % (r + 1) + line)
print("-" * 45)
print("Students seated:", idx, "| Vacant:", rows * cols - idx - len(reserved))
