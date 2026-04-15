import re
import random
import string
import math



def calculate_entropy(password):
    pool = 0

    if re.search(r"[a-z]", password):
        pool += 26
    if re.search(r"[A-Z]", password):
        pool += 26
    if re.search(r"\d", password):
        pool += 10
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        pool += 32

    if pool == 0:
        return 0

    entropy = len(password) * math.log2(pool)
    return round(entropy, 2)



def check_password(password):
    score = 0
    feedback = []

    
    if len(password) >= 12:
        score += 25
    else:
        feedback.append("Use at least 12 characters.")

    
    if re.search(r"[a-z]", password):
        score += 15
    else:
        feedback.append("Add lowercase letters.")

    
    if re.search(r"[A-Z]", password):
        score += 15
    else:
        feedback.append("Add uppercase letters.")

    
    if re.search(r"\d", password):
        score += 15
    else:
        feedback.append("Add numbers.")

    
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 20
    else:
        feedback.append("Add special characters.")

    
    if len(set(password)) > 6:
        score += 10
    else:
        feedback.append("Avoid repeated characters.")

    if score >= 80:
        strength = " Very Strong"
    elif score >= 60:
        strength = " Medium"
    else:
        strength = " Weak"

    return score, strength, feedback


#gen
def generate_password(length=12):
    characters = string.ascii_letters + string.digits + "!@#$%^&*()"
    return "".join(random.choice(characters) for _ in range(length))



if __name__ == "__main__":
    print("\n=== PASSWORD SECURITY ANALYZER ===\n")

    choice = input("1. Check Password\n2. Generate Password\nChoose option: ")

    if choice == "1":
        pwd = input("\nEnter password: ")

        score, strength, feedback = check_password(pwd)
        entropy = calculate_entropy(pwd)

        print("\n--- RESULTS ---")
        print("Score:", score, "/100")
        print("Strength:", strength)
        print("Entropy:", entropy, "bits")

        if feedback:
            print("\nSuggestions:")
            for f in feedback:
                print("-", f)

    elif choice == "2":
        length = int(input("Enter password length: "))
        pwd = generate_password(length)

        print("\nGenerated Password:", pwd)
        print("Tip: Don’t reuse passwords across sites.")

    else:
        print("Invalid option")
