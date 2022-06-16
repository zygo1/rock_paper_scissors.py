from random import randrange

# dictionary for the pc coding
pc_dict = {
    0: "rock",
    1: "scissors",
    2: "paper"
}
reverse_dict = {
    "rock": 0,
    "scissors": 1,
    "paper": 2
}
score = [0, 0]  # score[0] = player, score[1] = pc
rounds = 0  # count each round
history = []

while True:
    rounds += + 1
    print(f"------------------------------ Round {rounds}------------------------------")
    # input
    player = input("Choose rock, paper or scissors: ")
    pc = randrange(0, 3)
    while player not in ["rock", "paper", "scissors"]:
        player = input("Wrong input. Choices are: rock, paper or scissors. : ")

    # print their choices
    print("You: " + player)
    print(f"Computer: {pc_dict[pc]}")

    # Check who win in every round
    winner = None
    if reverse_dict[player] - pc == 0:
        winner = "draw"
    elif reverse_dict[player] - pc == 1 or reverse_dict[player] - pc == -2:
        score[1] += 1
        winner = "pc"
    elif reverse_dict[player] - pc == 2 or reverse_dict[player] - pc == -1:
        score[0] += 1
        winner = "player"

    # Check winner
    if winner == "player":
        print(f"You win! \nScore: {score[0]}-{score[1]}")
    elif winner == "pc":
        print(f"You lost. \nScore: {score[0]}-{score[1]}")
    else:  # winner = draw
        print(f"Draw. \nScore: {score[0]}-{score[1]}")

    # Update History
    history.append(f"Round {rounds}, Player: {player}, Computer: {pc_dict[pc]}, Score: {score[0]}-{score[1]}")

    # Check which one wins the game
    if score[0] == 3:
        print("Your score 3/3! You won the game!")
        # print history in a better format that a simple list
        print("----------------------------Game History ----------------------------")
        for element in history:
            print(element)
        break
    elif score[1] == 3:
        print("Computer's score 3/3. Computer won the game.")
        # print history in a better format that a simple list
        print("----------------------------Game Results ----------------------------")
        for element in history:
            print(element)
        break
