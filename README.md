	                                              **CARO Game With AI**
        - This is a for education purpose that I create an web app for player to play CARO game with the AI
         which is running Minimax Algorithm.

        - The rule of the is simple, you just have choose one spot every turn on the gameboard and try to 
        have N straight spot on a row, col or one diagonal to win the game. Every spot you choose on 
        the board game will be display as X and AI with O, Your jobs is to WIN the game or get a Tie from
        prevent the AI to win the game.

        - For anyone to use this code I have every you need inside this project, after pulling this code down 
         you just need to run the virtual environment by type envScriptsactivate and then run the app file
         with python3 by simply type python3 app.py

                About the Project

        - This project was written by Me using Flask for Back-End and html, css, js for Front-End.

        - The Minimax algorithm which we was using for the AI is kind of a recursive (backtracking algorithm)
        trying to look through every single posible action in order to find the best action to take among them.
        The problem of this algorithm is it can be up to O(n^n) in the time complexity and O(NxN) space to save
        the gameboard state. To solve this i apply the alpha beta pruning to cut unessessary branch, also the
        depth limit of 5 and some heuristic value.

        - The depth limit is to return the value of the terminal state with the best action on the lowest depth,
        when we reach the depth of 5 and it was not a terminal state then it will return the heuristic value
        base on the location of that spot. It will be 0 for corner spot like [0,0], [0,n - 1], [n - 1, 0] 
        and [n - 1, n - 1], 3 for spot in the center and 1 for all other spot.These heuristic value was put out
        by me through my experiment that the player have more spot on middle have more chance to WIN the game and
        the spot around the center will have chance to Tie the game hinger than the Corner spot.

                **About The Minmax with alpha beta pruning**
        - Alpha beta pruning is a method to cut unessessary recursive tree base whenever alpha >= beta because
        with alpha is stand for best value among all child branch and beta is the worst, when we check a MAX node
        we will need to get the min state value of opponent action (MIN node) which go into the next child state (MAX Node)
        on and on until we reach the terminal state or a depth limit which is 6 then backtracking. If one branch is clear 
        then alpha is update with higher value than minus INF (-999999 for this project) then we pass down the alpha to 
        next child node and because child is a Min Node it will find the Min and update the beta but if we saw one value
        that make beta <= alpha then we stop explore that branch cause no mater what next value of that branch is it will take the smallest and it might take the value beta which currently smaller than alpha so it not greater than alpha to change
        and it a bad action to take so we cut that branch. 

         
        
