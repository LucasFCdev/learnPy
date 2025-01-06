import random
from os import system, name

#Função para limpara tela a cada execução
def limpa_tela():

  #windows
  if name == 'nt':
    _ =system('cls')

  #Mac ou Linux
  else:
    _ = system('clear')

def game():

  limpa_tela()

  print("\nBem-vindo(a) ao jogo de força!")
  print("Adivinhe a palavra abaixo\n")

  # Lista de palavras para o jogo
  palavras = ['banana','abacate','uva','morango','laranja']

  palavra = random.choice(palavras)

  letras_descobertas = ['_' for letra in palavra] 

  #Número de chances
  chances = 6

  #Lista para as letras erradas
  letras_erradas = []

  #Loop enquanto número de chances for maior que zero 
  while chances > 0:
    
    print(" ".join(letras_descobertas))
    print("\nChances restantes:", chances)
    print("Letras erradas:", " ".join(letras_erradas))

    tentativa = input("\n Digite uma letra: ").lower()

    if tentativa in palavra:
      index = 0

      for letra in palavra:
        if letra == tentativa:
          letras_descobertas[index] = letra
        index += 1
    else:
      chances -= 1
      letras_erradas.append(tentativa)

   
    if "_" not in letras_descobertas:
      print("Você acertou a palavra!")
      break
  if "_" in letras_descobertas:
    print("\nVocê perdeu a palavra era: ", palavra)

if __name__ == "__main__":
  game()  