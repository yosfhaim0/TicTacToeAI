import alphaBetaPruning
import maxIt

board = maxIt.create()
maxIt.whoIsFirst(board)
while not maxIt.isFinished(board):
    if maxIt.isHumTurn(board):
        maxIt.inputMove(board)
    else:
        board = alphaBetaPruning.go(board)
maxIt.printState(board)
