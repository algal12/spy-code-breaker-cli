import random

while True:
    print("🕵️ Spy Code Breaker")
    print("1. Play")
    print("2. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        code = []
        for i in range(3):
            code.append(random.randint(1, 9))

        attempts = 0
        print("A 3-digit code has been generated. Try to guess it!")

        while True:
            guess = input("Enter 3 numbers (like 1 2 3): ")
            guess_list = guess.split()

            if len(guess_list) != 3:
                print("Please enter exactly 3 numbers.")
                continue

            # Convert to integers
            guess_nums = [int(n) for n in guess_list]
            attempts += 1

            # Check for exact match
            if guess_nums == code:
                print("🎉 Code cracked in", attempts, "attempts!")
                print("The code was:", code)
                break

            # Give hints
            for i in range(3):
                if guess_nums[i] == code[i]:
                    print("✅ Number", guess_nums[i], "is correct and in the right place.")
                elif guess_nums[i] in code:
                    print("🔁 Number", guess_nums[i], "is in the code but in the wrong place.")
                else:
                    print("❌ Number", guess_nums[i], "is not in the code.")

    elif choice == "2":
        print("Goodbye, agent!")
        break
    else:
        print("Please enter 1 or 2.")
