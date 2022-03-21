import copy

SIZE = 4
COMPUTER = 0  # Marks the computer's cells on the board
HUMAN = 1  # Marks the human's cells on the board
valueMin = -99
valueMax = 99
VIC = 10 ** 20  # The value of a winning board (for max)
LOSS = -VIC  # The value of a losing board (for max)
TIE = 0  # The value of a tie
CURSOR = valueMax + 1
EMPTY = CURSOR + 1

import random


# return [board, 0.00001, HUMAN, r, c, sumH, sumC]
# s[0]= board=SIZE*SIZE Arry whit SIZE varable [[1...SIZE]...[1...SIZE]]
# s[1]= 0.00001 = huristic value
# s[2]=turn=This value says whose turn (computer or human)
# s[3] and s[4]= r and c =The cursor row and column at the moment
# s[4]=How much has the HUMAN score accumulated so far
# s[5]=How much has the CUMPUTER score accumulated so far
def create():
    board = []
    row = []
    for i in range(SIZE):
        for j in range(SIZE):
            x = random.randrange(valueMin, valueMax)
            row = row + [x]
        board = board + [row]
        row = []
    c = random.randrange(0, SIZE)
    r = random.randrange(0, SIZE)
    board[r][c] = CURSOR
    sumH = 0
    sumC = 0
    return [board, 0.00001, HUMAN, r, c, sumH, sumC]


def inputMove(s):
    # Reads, enforces legality and executes the user's move.
    printState(s)
    flag = True
    while flag:
        r = int(input("Enter r: "))
        if r < 0 or r >= SIZE:
            print("Ilegal move.")
        elif s[3] == r:
            print("Ilegal move.")
        elif s[0][r][s[4]] == EMPTY or s[0][r][s[4]] == CURSOR:
            print("Ilegal move.")
        else:
            flag = False
            makeMove(s, r, s[4])


def isFinished(s):
    # Returns True iff the game ended
    return checkSeq(s) in [LOSS, VIC, TIE]


def isHumTurn(s):
    # Returns True iff it the human's turn to play
    return s[2] == HUMAN


def whoIsFirst(s):
    # The user decides who plays first
    print("hello! Welcome to MaxIt!\n\
    You always select the row and the computer in a column, good luck!")
    if int(input("Who plays first? 1-me / anything else-you. : ")) == 1:
        s[2] = COMPUTER
    else:
        s[2] == HUMAN


# s[5]=sunH
# בודק האם יש ניצחון לאחד הצדדים
def checkSeq(s):
    if s[2] == HUMAN:
        for i in range(SIZE):
            if s[0][i][s[3]] != EMPTY and s[0][i][s[3]] != CURSOR:
                if s[5] > s[6]:
                    return s[6] - s[5]
                elif s[5] < s[6]:
                    return s[6] - s[5]
                else:
                    return 0.00001
    if s[2] == COMPUTER:
        for i in range(SIZE):
            if s[0][s[3]][i] != EMPTY and s[0][s[3]][i] != CURSOR:
                if s[5] > s[6]:
                    return s[6] - s[5]
                elif s[5] < s[6]:
                    return s[6] - s[5]
                else:
                    return 0.00001
    if s[5] < s[6]:
        return VIC
    elif s[5] > s[6]:
        return LOSS
    else:
        return TIE


def getNext(s):
    # returns a list of the next states of s
    ns = []
    if s[2] == HUMAN:
        for r in range(SIZE):
            if s[0][r][s[4]] != EMPTY and s[0][r][s[4]] != CURSOR:
                tmp = copy.deepcopy(s)
                makeMove(tmp, r, s[4])
                ns += [tmp]
    elif s[2] == COMPUTER:
        for c in range(SIZE):
            if s[0][s[3]][c] != EMPTY and s[0][s[3]][c] != CURSOR:
                tmp = copy.deepcopy(s)
                makeMove(tmp, s[3], c)
                ns += [tmp]
    return ns


def value(s):
    # Returns the heuristic value of s
    return s[1]


def makeMove(s, r, c):
    if s[2] == HUMAN:
        s[5] += + s[0][r][c]
    elif s[2] == COMPUTER:
        s[6] += s[0][r][c]
    s[2] = abs(s[2] - 1)
    s[0][s[3]][s[4]] = EMPTY
    s[0][r][c] = CURSOR
    s[3] = r
    s[4] = c
    t = checkSeq(s)
    if t in [TIE, VIC, LOSS]:
        s[1] = t
    else:
        s[1] += t


def printState(s):
    print("_r/c___", end="")
    for i in range(SIZE):
        print(i, "___", end="")
    i = 0
    for r in range(SIZE):
        print("\n", i, ":  ", end="")
        i = i + 1
        for c in range(SIZE):
            if s[0][r][c] == CURSOR:
                print("**", " |", end="")
            elif s[0][r][c] == EMPTY:
                print("--", " |", end="")
            elif s[0][r][c] > 9 and s[0][r][c] < 100:
                print(s[0][r][c], " |", end="")
            elif s[0][r][c] < 10 and s[0][r][c] > -1:
                print(s[0][r][c], "  |", end="")
            elif s[0][r][c] < 0 and s[0][r][c] > -10:
                print(s[0][r][c], " |", end="")
            else:
                print(s[0][r][c], "|", end="")
    print("\n -- -- --\n")
    print("hum score: ", s[5], "  cum score:  ", s[6])
    if value(s) == VIC:
        print("Ha ha ha I won!")
    elif value(s) == LOSS:
        print("You did it!")
    elif value(s) == TIE:
        print("It's a TIE")


if __name__ == "__main__":
    x = create()
    printState(x)
