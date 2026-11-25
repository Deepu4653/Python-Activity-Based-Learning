# Advanced Numeric Pattern Generator (Hollow Diamond)
# Student: Leela Deepak Golukonda | Roll No: 26000521

print("HOLLOW DIAMOND PATTERN GENERATOR")
print("=" * 45)

n = 5   # half-height; total rows = 2n-1
if n < 1:
    print("Invalid dimension")
else:
    # upper half
    for i in range(1, n + 1):
        spaces = " " * (n - i)
        if i == 1:
            print(spaces + "1")
        else:
            nums = str(i) + " " * (2 * i - 3) + str(i)
            print(spaces + nums)
    # lower half
    for i in range(n - 1, 0, -1):
        spaces = " " * (n - i)
        if i == 1:
            print(spaces + "1")
        else:
            nums = str(i) + " " * (2 * i - 3) + str(i)
            print(spaces + nums)
