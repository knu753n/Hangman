import random, time, word_list

def select_word():
	x = word_list.list_of_words[random.randint(1,len(word_list.list_of_words))]
	print(x)
select_word()
