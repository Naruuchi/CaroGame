scores = {
    1 : 10,
    -1 : -10,
    0 : 0
}
def checkWinner(gametable, n): 
    score = [0 for i in range (0, 6)]

    zero = False
    for i in range (0, n):
        if zero:
            break
        for j in range (0, n):
            if gametable[i][j] == 0:
                zero = True
                break

    for i in range (0, n - 1):
        #wrong
        if gametable[0][i] != 0 and gametable[0][i] == gametable[0][i + 1]:
            score[0]+= 1
            if score[0] == n - 1:
                return gametable[0][i]

        if gametable[n - 1][i] != 0 and gametable[n - 1][i] == gametable[n - 1][i + 1] :
            score[1]+= 1
            if score[1] == n - 1:
                return  gametable[n - 1][i]
            
        if gametable[i][0] != 0 and gametable[i][0] == gametable[i + 1][0]:
            score[2]+= 1
            if score[2] == n - 1:
                return  gametable[i][0]
        
        if gametable[i][n - 1] != 0 and gametable[i][n - 1] == gametable[i + 1][n - 1]:
            score[3]+= 1
            if score[3] == n - 1:
                return  gametable[i][n - 1]
        
        if gametable[i][i] != 0 and gametable[i][i] == gametable[i + 1][i + 1]:
            score[4]+= 1
            if score[4] == n - 1:
                return  gametable[i][i]

        if gametable[i][n - i - 1] != 0 and (gametable[i][n - i - 1] == gametable[i + 1][n - i - 2]):
            score[5]+= 1
            if score[5] == n - 1:
                return  gametable[i][n - i - 1]
    if zero == False:
        return 0
    return 2

def nextBestMove(gametable, n):
    bestScore = -999999
    bestMove = [0,0]
    for i in range (0, n):
        for j in range (0, n):
            if gametable[i][j] == 0:
                gametable[i][j] = 1
                score = minimax(gametable, n, 0, False)
                gametable[i][j] = 0
                if bestScore < score:
                    bestScore = score
                    bestMove = [i,j]
    gametable[bestMove[0]][bestMove[1]] = 1
    return gametable
        
def minimax(gametable, n, depth, isMax):
    result = checkWinner(gametable, n)
    if result != 2:
        return scores[result]
    
    if isMax == True:
        bestScore = -999999
        for i in range (0, n):
            for j in range (0, n):
                if gametable[i][j] == 0:
                    gametable[i][j] = 1
                    score = minimax(gametable, n, depth + 1, False)
                    gametable[i][j] = 0
                    bestScore = max(score, bestScore)
        
        return bestScore
    else:
        bestScore = 999999
        for i in range (0, n):
            for j in range (0, n):
                if gametable[i][j] == 0:
                    gametable[i][j] = -1
                    score = minimax(gametable, n, depth + 1, True)
                    gametable[i][j] = 0
                    bestScore = min(bestScore, score)

        return bestScore
