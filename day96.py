#Simple Voting System Program in Python
def voting_system():
    print("Welcome to the Simple Voting System!")
    print("Type 'exit' to finish voting.")
    votes = {}
    while True:
        candidate = input("Enter the name of the candidate you want to vote for (or 'exit' to finish): ")
        
        if candidate.lower() == "exit":
            print("Exiting the voting system. Here are the final results:")
            for candidate, count in votes.items():
                print(f"{candidate}: {count} votes")
            break
        else:
            if candidate in votes:
                votes[candidate] += 1
            else:
                votes[candidate] = 1
    print("Thank you for participating in the voting!")
    if votes:
        winner = max(votes, key=votes.get)
        print(f"The candidate with the most votes wins: {winner} with {votes[winner]} votes!")
    else:
        print("No votes were cast.")

if __name__ == "__main__":
    voting_system()