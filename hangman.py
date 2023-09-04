import random

def hangman(word):
    wrong = 0
    stages = ["",
              "________  ",
              "|      |  ",
              "|      O  ",
              "|     /|\ ",
              "|     / \ ",
              "|         ",
              "|________ ",
              ]
    rletters = list(word)
    board = ["__"]*len(word)
    win = False
    print("Welcome to Hangman")
    print((" ".join(board)))
    while wrong < len(stages)-1:
        print("\n")
        msg = "Guess a letter: "
        char = input(msg).lower()
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = '$'
        else:
            wrong += 1
        print((" ".join(board)))
        e = wrong + 1
        print("\n".join(stages[0:e]))
        if "__" not in board:
            print("You win!")
            print("You guessed the secret word: " + " ".join(board))
            win = True
            break
    if not win:
        print("\nYou lose! It was {}.".format(word))

WordList = ["cat", "computer", "variable", "python", "water", "mug", "plant", "mouse", "phone", "plate"]
a = random.randint(1,10)

hangman(WordList[a])
