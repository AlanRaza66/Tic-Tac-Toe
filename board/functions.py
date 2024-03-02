class Board:
    def __init__(self, content=[0]*9):
        # Assurez-vous que la longueur de content est égale à 9
        if len(content) != 9:
            raise ValueError("La longueur de 'content' doit être de 9 éléments.")
        
        # Assurez-vous que les valeurs de content sont soit -1, 0 ou 1
        for value in content:
            if value not in (-1, 0, 1):
                raise ValueError("Les valeurs de 'content' doivent être soit -1, 0 ou 1.")
        
        self.content = content
    
    def showBoard(self):
        line = []
        for i in range(0,9):
            if len(line) < 3 :
                if self.content[i] == 0:
                    line.append("-")
                elif self.content[i] == 1:
                    line.append("X")
                elif self.content[i] == -1:
                    line.append("O")
                if len(line) == 3:
                    print(" ".join(line))
                    line = []
    
    def getValue(self, x):
        return self.content[x]
    
    def setValue(self, x, val):
        self.content[x] = val