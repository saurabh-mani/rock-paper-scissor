import random

option_map = {
    1 : "Rock",
    2 : "Paper",
    3 : "Scissor"
}

while True:
    print("1. Rock\n2. Paper\n3. Scissor\n4. Quit")
    player = int(input("Enter Your Choice: "))
    if player == 4:
        break
    elif player < 1 or player > 4:
        print("Invalid choice...")
        continue
    computer = random.randrange(1,4)
    print("Player's Choice: "+ option_map[player])
    print("Computer's Choice: "+ option_map[computer])
    if player == computer:
        print("It's a draw...")
    elif ((player == (computer+1)) or (player == 1 and computer == 3)):
        print("Player Wins...")
    else:
        print("Computer Wins...")