# Solution

class GuessNumber:
	def __init__(self, number, mn=0, mx=100):
		self.number = number 
		self.guesses = 0
		self.min = mn 
		self.max = mx 

	def get_guess(self):
		''' get user guess '''
		guess = input(f"Please guess a number ({self.min} - {self.max})")
		if self.valid_number(guess):
			return int(guess)
		else:
			print("please enter a valid number.")
			return self.get_guess()

	def valid_number(self, str_number):
		''' validates the integer '''
		try:
			number =  int(str_number)
		except:
			return False 

		return self.min <= number <= self.max 

	def play(self):
		''' start the game '''
		while True:
			self.guesses += 1

			guess = self.get_guess()

			if guess < self.number:
				print("Your guess was under")
			elif guess > self.number:
				print("Your guess was over")
			else:
				break 

		print(f"You guessed it in {self.guesses} guesses")

game = GuessNumber(56,0,100)
game.play()

'''
Separar o codigo em uma classe
separar as funcoes em funcoes ( melhor ter uma funcao qeu relaize uma açao bem feita 
que uma que faca muito mas que fica dificil de rastrear bugs )
deixar o codigo mais 'legivel (literalmente)'  e mais escalavel

'''