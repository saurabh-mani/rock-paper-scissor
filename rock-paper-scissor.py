import random

option_map = {
    1 : "Rock",
    2 : "Paper",
    3 : "Scissor"
}
print("1. Rock\n2. Paper\n3. Scissor")
player = int(input("Enter Your Choice: "))
computer = random.randrange(1,4)
print("Player's Choice: "+ option_map[player])
print("Computer's Choice: "+ option_map[computer])
if player == computer:
    print("It's a draw...")
elif ((player > computer and player != 3) or (player == 3 and computer == 1)):
    print("Player Wins...")
else:
    print("Computer Wins...")