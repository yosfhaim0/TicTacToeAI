import alphaBetaPruning
import maxIt

board = [[[6, -33, 14, -29],[20, -1, 47, -74], [59, 100, 57, 68],[89, 42, 54, -67]], 0.00001, 1, 2, 1, 0, 0]
maxIt.whoIsFirst(board)
while not maxIt.isFinished(board):
    if maxIt.isHumTurn(board):
        maxIt.inputMove(board)
    else:
        board = alphaBetaPruning.go(board)
maxIt.printState(board)
