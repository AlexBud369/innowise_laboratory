CURRENT_YEAR = 2025

def generate_profile(age):
    if age >= 0 and age <= 12:
        return "Child"
    elif age <= 19:
        return "Teenager"
    else:
        return "Adult"


def get_user_info():
    user_name = input("Enter your full name: ")
    birth_year_str = input("Enter your birth year: ")
    birth_year = int(birth_year_str)
    current_age = CURRENT_YEAR - birth_year

    return user_name, birth_year, current_age


def collect_hobbies():
    hobbies = []

    while True:
        hobby = input("Enter a favorite hobby or type 'stop' to finish: ")
        if hobby.lower() == "stop":
            break
        hobbies.append(hobby)

    return hobbies

def create_profile(name, age, life_stage, hobbies):

    return {
        "name": name,
        "age": age,
        "life_stage": life_stage,
        "hobbies": hobbies
    }

def main():
    user_name, birth_year, current_age = get_user_info()
    hobbies = collect_hobbies()
    life_stage = generate_profile(current_age)

    user_profile = create_profile(user_name, current_age, life_stage, hobbies)

if __name__ == "__main__":
    main()