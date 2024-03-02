from board.functions import Board

class Game:
    round = 1
    end = False
    def newGame():
        board = Board()
        board.showBoard()
        
        while Game.end == False:
                board.showBoard()
                if Game.round % 2 == 1:
                    print("Tour du joueur X")
                else:
                     print("Tour du joueur O")
                Game.round+=1
                if Game.round == 10:
                    Game.end = True
        