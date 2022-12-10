ROCK = 1
PAPER = 2
SCISSORS = 3

LOSE = 0
DRAW = 3
WIN = 6

TO_MATERIAL = {
    "A": ROCK,
    "B": PAPER,
    "C": SCISSORS,
}

WIN_LOSE_OR_DRAW = {
    "X": LOSE,
    "Y": DRAW,
    "Z": WIN,
}

SCORE = {
    (ROCK, ROCK): DRAW,
    (ROCK, PAPER): WIN,
    (ROCK, SCISSORS): LOSE,
    (PAPER, ROCK): LOSE,
    (PAPER, PAPER): DRAW,
    (PAPER, SCISSORS): WIN,
    (SCISSORS, ROCK): WIN,
    (SCISSORS, PAPER): LOSE,
    (SCISSORS, SCISSORS): DRAW,
}


########################################################################
def strategy(opponent_choice, win_lose_or_draw):
    if win_lose_or_draw == DRAW:
        return opponent_choice
    elif win_lose_or_draw == WIN:
        if opponent_choice == ROCK:
            return PAPER
        elif opponent_choice == PAPER:
            return SCISSORS
        else:
            return ROCK
    else:
        if opponent_choice == ROCK:
            return SCISSORS
        elif opponent_choice == PAPER:
            return ROCK
        else:
            return PAPER


########################################################################
def check_score(opponent_choice, win_lose_or_draw):
    opponent_material = TO_MATERIAL[opponent_choice]
    my_material = strategy(opponent_material, WIN_LOSE_OR_DRAW[win_lose_or_draw])

    win_score = SCORE[(opponent_material, my_material)]
    return win_score + my_material


########################################################################
def main():
    total_score = 0
    for line in open("input.txt"):
        opponent_choice, win_lose_or_draw = line.split()
        score = check_score(opponent_choice, win_lose_or_draw)
        total_score += score

    print("total_score:", total_score)


########################################################################
main()
