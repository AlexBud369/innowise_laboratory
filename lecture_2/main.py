
def generate_profile(age):
    if age >= 0 and age <= 12:
        return "Child"
    elif age <= 19:
        return "Teenager"
    else:
        return "Adult"
