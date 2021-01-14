import random, time, word_list, os

def clear_screen():
	if os.name == "nt":
		os.system("cls")
	if os.name == "posix":
		os.system("clear")

def select_word():
	random_word = random.choice(word_list.list_of_words)
	return random_word

def game_board(word):
	word_line = []
	for letter in word:
		if letter == " ":
			word_line.append(' ')
		else:
			word_line.append('-')
	return word_line

def check_letter(letter_guess, word):
	return letter_guess in word

def letter_index(letter_guess, word):
	index = 0
	list_of_indexes = []
	for letter in word:
		if letter == letter_guess:
			list_of_indexes.append(index)
		index += 1
	return list_of_indexes

def guess_letter(letter_guess, word):
	letter_guess = letter_guess.lower()
	word = word.lower()
	if check_letter(letter_guess, word):
		list = letter_index(letter_guess, word)
		return list
	else:
		return False

def show_guessed_letter(indexes, guessed_letter, game_board):
	if indexes != False:
		for index in indexes:
			if game_board[index] == guessed_letter:
				return False
			game_board[index] = guessed_letter
	else:
		return False

	return game_board

def main():
	clear_screen()
	random_word = select_word()
	game_board_ = game_board(random_word)
	guesses_left = len(random_word)+3
	letters_guessed = []
	#print(random_word)
	print(*game_board_)
	while guesses_left > 0:
		letter_guess = input("Guess letter: ")
		letters_guessed.append(letter_guess)
		indexes = guess_letter(letter_guess, random_word)
		game_board_new = show_guessed_letter(indexes,letter_guess, game_board_)
		letters_left = len(random_word)
		if game_board_new != False:
			game_board_ = game_board_new
			clear_screen()
			print(*game_board_)
			print('')
			print('Guesses left:', guesses_left,end="")
			print(" | Already guessed: ",letters_guessed)

		else:
			guesses_left -= 1
			clear_screen()
			print(*game_board_)
			print('')
			print('Guesses left:', guesses_left, end="")
			print(" | Already guessed: ",letters_guessed)
		for each in game_board_:
			if each != '-':
				letters_left -= 1
			if letters_left == 0:
				print("CONGRATULATIONS!")
				replay = input("Do you want to play again? yes / no: ")
				if replay.lower()=="yes":
					main()
				else:
					clear_screen()
					exit()

	input("GAME OVER!")
	replay = input("Do you want to play again? yes / no: ")
	if replay.lower()=="yes":
		main()
	else:
		clear_screen()
		exit()


# Testing


# main profram

if __name__ == "__main__":
	try:
		main()
	except KeyboardInterrupt:
		clear_screen()
		input("Thanks for playing!")
		clear_screen()
		exit()
