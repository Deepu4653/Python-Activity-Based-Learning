# String-Based Examination Answer Evaluation
# Student: Leela Deepak Golukonda | Roll No: 26000521

print("STRING-BASED ANSWER EVALUATION")
print("=" * 45)

key = "ABCDABCD"   # answer key (A/B/C/D/space for unattempted)
students = [
    ("Stu1", "ABCDABCA"),
    ("Stu2", "ABCABCDD"),
    ("Stu3", "AB DAB D"),
    ("Stu4", "ABCDABCD"),
]
NEG = 0.25
print("Answer key:", key)
print("-" * 45)
for (name, ans) in students:
    correct = 0
    wrong = 0
    unattempt = 0
    ans = (ans + " " * len(key))[:len(key)]
    for i in range(len(key)):
        k = key[i]
        a = ans[i]
        if a == " ":
            unattempt += 1
        elif a == k:
            correct += 1
        else:
            wrong += 1
    score = correct - wrong * NEG
    score = round(score, 2)
    print("%-5s correct=%d wrong=%d unattempted=%d score=%.2f" % (name, correct, wrong, unattempt, score))
