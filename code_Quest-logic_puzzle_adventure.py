users = {}

def login():
    print("=== Welcome to the Logic Dungeon ===")
    print("1. Register")
    print("2. Login")

    while True:
        choice = input("Select option (1 or 2): ")
        if choice == '1':
            email = input("Enter your email: ")
            password = input("Create a password: ")
            if email in users:
                print("Email already registered. Try logging in.")
            else:
                users[email] = {'password': password, 'score': 0}
                print("Registration successful. You can now log in.\n")
        elif choice == '2':
            email = input("Enter your email: ")
            password = input("Enter your password: ")
            if email in users and users[email]['password'] == password:
                print(f"Login successful! Welcome, {email}!\n")
                return email
            else:
                print("Incorrect email or password. Try again.")
        else:
            print("Invalid choice. Try 1 or 2.")

def add_points(user, points):
    users[user]['score'] += points

def welcome():
    print("*******  Welcome, Adventurer!  ********")
    print("\nYou're trapped in a logic dungeon.")
    print("Solve puzzles to unlock the next gate!\n")

def level_1(user):
    print("Level 1: The Number Gate")
    while True:
        num = int(input("> Enter a number divisible by 3 and 5 but not 10: "))
        if num % 3 == 0 and num % 5 == 0 and num % 10 != 0:
            print("Gate opens! Proceed...\n")
            add_points(user, 10)
            break
        else:
            print("Wrong number. Try again!")
            add_points(user, -2)

def level_2(user):
    print("Level 2: The Code Wall")
    secret = int("3142"[::-1]) * 2
    while True:
        guess = int(input("> Crack the passcode: it's the reverse of '3142', doubled: "))
        if guess == secret:
            print("Wall crumbles. You're through!\n")
            add_points(user, 10)
            break
        else:
            print("Incorrect passcode!")
            add_points(user, -2)

def level_3(user):
    print("Level 3: The Word Riddle")
    while True:
        word = input("> Find the word with 3 vowels and ends with 'ing': ").lower()
        vowels = "aeiou"
        vowel_count = sum(1 for ch in word if ch in vowels)
        if vowel_count == 3 and word.endswith("ing"):
            print("Riddle solved. Continue!\n")
            add_points(user, 10)
            break
        else:
            print("Nope! Try another word.")
            add_points(user, -2)

def level_4(user):
    print("Level 4: The Loop Maze")
    print("> Reach 100 by adding only even numbers from 1–20. How many steps?")
    total = 0
    steps = 0
    for num in range(1, 21):
        if num % 2 == 0:
            total += num
            steps += 1
            if total >= 100:
                break
    guess = int(input("Your guess: "))
    if guess == steps:
        print("You found the path! Well done!")
        add_points(user, 10)
    else:
        print(f"Not quite. The answer was {steps} steps.")
        add_points(user, -2)

def prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def level_5(user):
    print("Level 5: The Prime Cipher")
    while True:
        code = input("> Enter a 4-digit prime number ending in 3, with prime digit sum: ")
        if not code.isdigit() or len(code) != 4:
            print("Must be a 4-digit number.")
            add_points(user, -1)
            continue
        num = int(code)
        digit_sum = sum(int(d) for d in code)
        if not prime(num):
            print("Not a prime number.")
            add_points(user, -1)
            continue
        if not prime(digit_sum):
            print(f"Digit sum {digit_sum} is not prime.")
            add_points(user, -1)
            continue
        if not code.endswith("3"):
            print("Doesn't end in 3.")
            add_points(user, -1)
            continue
        print("Vault unlocks! You may proceed.\n")
        add_points(user, 10)
        break

def level_6(user):
    print("Level 6: The Final Equation")
    print("> Solve this: answer**3 - 3 * answer**2 + 2 == 0")
    while True:
        try:
            answer = int(input("Your x: "))
            if (answer**3 - 3 * answer**2 + 2 == 0):
                print("Correct! You've solved the final puzzle.\n")
                add_points(user, 10)
                break
            else:
                print("Incorrect. Try again!")
                add_points(user, -2)
        except ValueError:
            print("Please enter a valid number.")

def play_game():
    user = login()
    welcome()
    level_1(user)
    level_2(user)
    level_3(user)
    level_4(user)
    level_5(user)
    level_6(user)
    print(f"\n Congratulations, {user}! You escaped the Logic Dungeon!")
    print(f" Your Final Score: {users[user]['score']} points")

play_game()
