import random, time, word_list

def select_word():
	x = word_list.list_of_words[random.randint(1,len(word_list.list_of_words))]
	return x

def game_board(word):
	word_line = ""
	for each in word:
		if each == " ":
			word_line += ' '
		else:
			word_line += '-'
	return word_line

print(game_board("test ord"))
