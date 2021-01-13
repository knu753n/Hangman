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
	return if letter_guess in word



# Testing
print(game_board(str(select_word())))
