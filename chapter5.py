# exactly one black & white king - otherwise False
# max 16 black &  white pices
# max 8 black & white pawns
# max 2 pawns, kinghts, bishops, rooks
# must be within space 1a to 8h

def isValidChessBoard(board):
    # counting occurences of each figure from provided chessboard
    count = {}
    for v in board.values():
        count.setdefault(v, 0)
        count[v] += 1
    # check if exactly one white & one black king
    for x in
