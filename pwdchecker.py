import string

COMMON_PASSWORDS = ["123456", "password", "qwerty", "admin123", "12345678", "letmein"]

def check_password_strength(password):
    if password in COMMON_PASSWORDS:
        print(f"Password: '{password}'")
        print("Strength: Very Weak")
        print("Feedback: This is an extremely common password. Choose something unique.\n")
        return

    has_length = len(password) >= 8
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in string.punctuation for c in password)

    score = sum([has_length, has_upper, has_lower, has_digit, has_special])

    feedback = []
    if not has_length:
        feedback.append("Make it at least 8 characters long.")
    if not has_upper:
        feedback.append("Add an uppercase letter.")
    if not has_lower:
        feedback.append("Add a lowercase letter.")
    if not has_digit:
        feedback.append("Add a number.")
    if not has_special:
        feedback.append("Add a special character.")

    if score == 5:
        rating = "Strong"
    elif score >= 3:
        rating = "Medium"
    else:
        rating = "Weak"

    print(f"Password: '{password}'")
    print(f"Strength: {rating}")
    if feedback:
        print("Feedback: " + " ".join(feedback))
    else:
        print("Feedback: Perfect password structure!")
    print()


test_passwords = [
    "123456",
    "hello",
    "password123",
    "TehamIrfan21",
    "TehamIrfan21!",
    "AribIrfan19#"
]

for pwd in test_passwords:
    check_password_strength(pwd)