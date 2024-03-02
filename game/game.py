from board.functions import Board

class Game:
    round = 1
    end = False
    def newGame():
        board = Board()
        
        while Game.end == False:

                board.showBoard()
                print("Tour {}".format(Game.round))
                print("Tour du joueur X" if Game.round % 2 == 1 else "Tour du joueur O")
                play = int(input("Dans quelle case voulez-vous jouer?\n")) - 1
                if board.getValue(play) != 0 :
                    play = int(input("Cette case est déjà pleine, choisissez une autre: \n")) - 1
                else:
                    board.setValue(play, 1 if Game.round % 2 == 1 else -1)
                    Game.round+=1
                    if board.checkIfFull() :
                        print("Fin de la partie")
                        board.showBoard()
                        Game.end = True
    