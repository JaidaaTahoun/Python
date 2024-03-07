import random

TIE = 0
COMPUTER_WON = 1
PLAYER_WON = 2

random.seed(10)

def convertChoiceToString(choice):
    if choice == 1:
        return "rock"
    elif choice == 2:
        return "paper"
    elif choice == 3:
        return "scissors"

def rockPaperScissors(computerChoice, playerChoice):
    if computerChoice == playerChoice:
        return TIE
    elif (computerChoice == 1 and playerChoice == 3) or \
         (computerChoice == 2 and playerChoice == 1) or \
         (computerChoice == 3 and playerChoice == 2):
        return COMPUTER_WON
    else:
        return PLAYER_WON

def main():
    playerScore = 0
    computerScore = 0

    for _ in range(3):
        playerChoice = int(input("Enter 1 for rock, 2 for paper, 3 for scissors: "))

        while playerChoice not in [1, 2, 3]:
            print("Invalid choice.")
            playerChoice = int(input("Enter 1 for rock, 2 for paper, 3 for scissors: "))

        computerChoice = random.randint(1, 3)

        print(f"Computer chose {convertChoiceToString(computerChoice)}")
        print(f"You chose {convertChoiceToString(playerChoice)}")

        result = rockPaperScissors(computerChoice, playerChoice)

        if result == TIE:
            print("You made the same choice as the computer")
        elif result == COMPUTER_WON:
            print("The computer won this round")
            computerScore += 1
        else:
            print("You won this round")
            playerScore += 1

    if playerScore > computerScore:
        print(f"Game ended with you winning {playerScore} vs. {computerScore} for computer")
    elif playerScore < computerScore:
        print(f"Game ended with computer winning {computerScore} vs. {playerScore} for you")
    else:
        print(f"Game ended with a tie {playerScore} points each")

main()

