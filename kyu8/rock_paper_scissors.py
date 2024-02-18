"""
Rock Paper Scissors
Let's play! You have to return which player won! In case of a draw return Draw!.

Examples(Input1, Input2 --> Output):
"scissors", "paper" --> "Player 1 won!"
"scissors", "rock" --> "Player 2 won!"
"paper", "paper" --> "Draw!"
"""


def rps(p1, p2):
    beats = {
        "scissors": "paper",
        "paper": "rock",
        "rock": "scissors",
    }

    if p1 == p2:
        return "Draw!"
    elif beats[p1] == p2:
        return "Player 1 won!"
    else:
        return "Player 2 won!"


print(rps("scissors", "paper"))
print(rps("scissors", "rock"))
print(rps("paper", "paper"))
