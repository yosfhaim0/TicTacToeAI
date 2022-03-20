import maxIt
import copy

DEPTH = 5


def go(s):
    if maxIt.isHumTurn(s):
        x=abmin(s, DEPTH, float("-inf"), float("inf"))[1]
        return x
    else:
        y=abmax(s, DEPTH, float("-inf"), float("inf"))[1]
        return y


# s = the state (max's turn)
# d = max. depth of search
# a,b = alpha and beta
# returns [v, ns]: v = state s's value. ns = the state after recomended move.
#        if s is a terminal state ns=0.
def abmax(s, d, a, b):
    if d == 0 or maxIt.isFinished(s):
        return [maxIt.value(s), 0]
    v = float("-inf")
    ns = maxIt.getNext(s)
    bestMove = 0
    for i in ns:
        tmp = abmin(copy.deepcopy(i), d - 1, a, b)
        if tmp[0] > v:
            v = tmp[0]
            bestMove = i
        if v >= b:
            return [v, i]
        if v > a:
            a = v
    return [v, bestMove]


# s = the state (min's turn)
# d = max. depth of search
# a,b = alpha and beta
# returns [v, ns]: v = state s's value. ns = the state after recomended move.
#        if s is a terminal state ns=0.
def abmin(s, d, a, b):
    if d == 0 or maxIt.isFinished(s):
        return [maxIt.value(s), 0]
    v = float("inf")
    ns = maxIt.getNext(s)
    bestMove = 0
    for i in ns:
        tmp = abmax(copy.deepcopy(i), d - 1, a, b)
        if tmp[0] < v:
            v = tmp[0]
            bestMove = i
        if v <= a:
            return [v, i]
        if v < b:
            b = v
    return [v, bestMove]


'''
s=maxIt.create()
maxIt.makeMove(s,1,1)
print(s)
maxIt.makeMove(s,0,0)
maxIt.makeMove(s,0,1)
maxIt.makeMove(s,0,2)
maxIt.makeMove(s,1,0)
maxIt.makeMove(s,1,1)
maxIt.makeMove(s,1,2)
maxIt.makeMove(s,2,1)
maxIt.makeMove(s,2,0)
maxIt.printState(s)
print(go(s))
'''
