# Password Policy Validation Engine
# Student: Leela Deepak Golukonda | Roll No: 26000521

print("PASSWORD POLICY VALIDATION ENGINE")
print("=" * 45)

passwords = ["Abcd@123", "short", "NoSpecial1", "alllowercase1!", "RepeatingAA1!", "goodPass9#xQ"]

for pw in passwords:
    errors = []
    if len(pw) < 8:
        errors.append("length must be at least 8")
    if not any(ch.isupper() for ch in pw):
        errors.append("needs an uppercase letter")
    if not any(ch.islower() for ch in pw):
        errors.append("needs a lowercase letter")
    if not any(ch.isdigit() for ch in pw):
        errors.append("needs a digit")
    specials = "!@#$%^&*"
    if not any(ch in specials for ch in pw):
        errors.append("needs a special character (!@#$%^&*)")
    rep = False
    for i in range(len(pw) - 2):
        if pw[i] == pw[i + 1] == pw[i + 2]:
            rep = True
    if rep:
        errors.append("no character may repeat 3+ times consecutively")
    if "password" in pw.lower():
        errors.append("contains prohibited word 'password'")
    print("Password: %-15s -> %s" % (pw, "VALID" if not errors else "INVALID"))
    for e in errors:
        print("    - " + e)
