# Hangman Game (Jogo da Forca)
# Programação Orientada a Objetos

# Import
import random

# Board (tabuleiro)
board = ['''

\033[1;37m>>>>>>>>>>Hangman<<<<<<<<<<

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

# Classe
class Hangman:

	# Método Construtor
	def __init__(self, word):
		self.word = word
		self.corretas = []
		self.erradas = []
		self.total = self.word.count(' ')
		self.count = 0
		
	# Método para adivinhar a letra
	def guess(self, letter):
		self.letter = letter

		if (len(letter) > 1):
			print('\033[1;33mVocê só pode digitar uma LETRA por vez.\033[1;37m')
		elif (len(letter) <= 0):
			print('\033[1;33mVocê DEVE informar pelo menos uma LETRA.\033[1;37m')
		else:
			if ((letter in self.corretas) or (letter in self.erradas)):
				print(f'\033[1;36m\nVocê já tentou essa letra antes.\033[1;37m')
			else:
				if(letter in self.word):
					self.corretas.append(letter)
					self.total += self.word.count(letter)
					print(f'\033[1;35mMuito bem. A palavra possui a letra {letter}.\033[1;37m')
				else:
					self.erradas.append(letter)
					self.count += 1
					print(f'\033[1;31mQue pena. A palavra NÃO possui a letra {letter}.\033[1;37m')

	# Método para verificar se o jogo terminou
	def hangman_over(self):
		if self.count >= 6:
			return True	
			
	# Método para verificar se o jogador venceu
	def hangman_win(self):
		if self.total == len(self.word):
			return True
	
	# Método para checar o status do game e imprimir o board na tela
	def print_game_status(self):
		print(board[self.count])

		print(f'The word is: {self.word}\n')
		print('Palavra: ', end = '')
		for w in range(0,len(self.word)):
			if(self.word[w] == ' '):
				print(' ', end='')
			elif(self.word[w] in self.corretas):
				print(f'{self.word[w]} ', end='')
			else:
				print('_ ', end='')
					
		print('\n\nLetras Corretas: ', end='')
		for c in self.corretas:
			print(f'{c} ', end='')
		print('\nLetras Erradas: ', end='')
		for e in self.erradas:
			print(f'{e} ', end='')
		print()	

# Função para ler uma palavra de forma aleatória do banco de palavras
def rand_word(sorteado):

	if(sorteado == 0):
		with open("arquivos/bandas.txt", "rt") as file:
			bank = file.readlines() # retorna uma lista de todas as palavras do arquivo
		return bank[random.randint(0,(len(bank) - 1))].upper().strip()
	elif sorteado == 1:
		with open("arquivos/comidas.txt", "rt") as f:
			bank = f.readlines()
		return bank[random.randint(0,(len(bank) - 1))].upper().strip()
	elif sorteado == 2:
		with open("arquivos/cores.txt", "rt") as f:
			bank = f.readlines()
		return bank[random.randint(0,(len(bank) - 1))].upper().strip()
	elif sorteado == 3:
		with open("arquivos/livros.txt", "rt") as f:
			bank = f.readlines()
		return bank[random.randint(0,(len(bank) - 1))].upper().strip()
	else:
		with open("arquivos/times.txt", "rt") as f:
			bank = f.readlines()
		return bank[random.randint(0,(len(bank) - 1))].upper().strip()

# Função Main - Execução do Programa
def main():

	resposta = 'S'
	while (resposta == 'S'):
		sorteado = random.randint(0, 4)

		# Objeto
		game = Hangman(rand_word(sorteado))

		dicas = ['Banda/Cantor(a)', 'Comidas Típicas do Brasil', 'Cores', 'Livros', 'Times de Futebol']

		# Enquanto o jogo não tiver terminado, print do status, solicita uma letra e faz a leitura do caracter

		while(True):
			# Verifica o status do jogo
			game.print_game_status()

			print(f'\nDICA: \033[1;32m{dicas[sorteado]}\033[1;37m')
			
			if(game.hangman_over()):
				break
			if(game.hangman_win()):
				break

			game.guess(str(input('\nDigite uma letra: ')).upper())
			
		# De acordo com o status, imprime mensagem na tela para o usuário
		if (game.hangman_win()):
			print ('\n\033[1;93mParabéns! Você venceu!!\033[1;37m')

			resposta = str(input('\033[1;36mDeseja jogar novamente? [S/N] \033[1;37m')).upper()

		elif(game.hangman_over()):
			print ('\n\033[1;95mGame over! Você perdeu.\033[1;37m')
			print (f'A palavra era \033[1;33m{game.word}\033[1;37m')

			resposta = str(input('\033[1;36mDeseja jogar novamente? [S/N] \033[1;37m')).upper()
				
	print ('\nÓtimo jogo. Até a próxima!\n')

# Executa o programa		
if __name__ == "__main__":
	main()