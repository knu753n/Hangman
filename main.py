import random, time, word_list

def select_word():
	x = word_list.list_of_words[random.randint(1,len(word_list.list_of_words))]
	return x

def game_board(word):
	word_line = ""
	for letter in word:
		if letter == " ":
			word_line += ' '
		else:
			word_line += '-'
	return word_line

def check_letter(letter_guess, word):
	return letter_guess in word

def letter_index(x,y):
	if check_letter(x,y.lower()):
		index = 0
		list_of_indexes = []
		for each in y:
			if each == x:
				list_of_indexes.append(index)
			index += 1
		return list_of_indexes


# Testing
random_word = select_word()
game_board = game_board(random_word)
print(random_word)
print(game_board)
x = input("Skriv en bokstav: ").lower()
