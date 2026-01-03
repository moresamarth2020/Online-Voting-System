candidates = {
    "Amit": 0,
    "Neha": 0,
    "Rahul": 0
}

def cast_vote():
    print("\nCandidates:")
    for name in candidates:
        print("-", name)

    vote = input("Enter candidate name to vote: ")

    if vote in candidates:
        candidates[vote] += 1
        print("✔ Vote cast successfully!")
    else:
        print("❌ Invalid candidate!")

def show_results():
    print("\n----- VOTING RESULTS -----")
    for name, votes in candidates.items():
        print(f"{name}: {votes} votes")

    winner = max(candidates, key=candidates.get)
    print("\n🏆 Winner:", winner)

def voting_system():
    while True:
        print("\n----- ONLINE VOTING MENU -----")
        print("1. Cast Vote")
        print("2. Show Results")
        print("3. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            cast_vote()
        elif choice == "2":
            show_results()
        elif choice == "3":
            print("Thank you for voting!")
            break
        else:
            print("Invalid choice. Try again.")

voting_system()
