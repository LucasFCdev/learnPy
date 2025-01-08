# Programação Orientada a Objetos

# Import
import random
from os import system, name

# Board (tabuleiro)
board = ['''

>>>>>>>>>>Hangman<<<<<<<<<<

+---+
|   |
    |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
|   |
    |
    |
=========''', '''

 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']

#Função para limpara tela a cada execução
def limpa_tela():

  #windows
  if name == 'nt':
    _ =system('cls')

  #Mac ou Linux
  else:
    _ = system('clear')

# Classe
class Hangman:
    

    # Método Construtor
    def __init__ (self, choiceWord):
        self.choiceWord = choiceWord   
        self.correctLetters = []
        self.wrongLetters = []
        
        
    # Método para adivinhar a letra
    def guessLetter (self, tryLetter):
        self.tryLetter = tryLetter

        if self.tryLetter in self.choiceWord and tryLetter not in self.correctLetters:
            self.correctLetters.append(self.tryLetter)
            self.setLetter()
        elif tryLetter not in self.choiceWord :
            self.wrongLetters.append(self.tryLetter)
        else:
            return
        return True
    # Método para não mostrar a letra no board        
    def setLetter (self):
        
        showWord = ''

        for letter in self.choiceWord:
            if letter in self.correctLetters:
                showWord += letter
            else:
                showWord += '_'
        return showWord        
    
    # Método para verificar se o jogo terminou
    # Método imprimir o board na tela
    def printScreen(self):
        print(self.setLetter())

        print("Letras erradas: ", self.wrongLetters)

        print (board[len(self.wrongLetters)])
    
    # Método para checar o status do game
    def checkStatus (self):
        if len(self.wrongLetters) > 6:
            return True
    
    # Método para verificar se o jogador venceu
    def playWin(self):
        if self.checkStatus and '_' not in  self.setLetter():
            return True


# Método para verificar se o jogador venceu

# Método para não mostrar a letra no board

# Método para checar o status do game e imprimir o board na tela
    
# Metodo para ler uma palavra
def selWord ():
    words = ['banana', 'abacate', 'uva', 'morango', 'laranja']

    choiceWord = random.choice(words)

    return choiceWord

def main ():
    game = Hangman(selWord())
    while game.checkStatus:
            
            limpa_tela()

            game.printScreen()
            
            tryLetter = input("Digite a Letra:").lower()
            game.guessLetter(tryLetter)

            if game.playWin():
                print('Parabens! Você ganhou')
                break
            elif game.checkStatus():
                print("Você perdeu a palavra é: ", game.choiceWord)
                break
if __name__ == "__main__":
    main()        
            
        


