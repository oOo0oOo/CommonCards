from matplotlib import pyplot as plt

import numpy as np

def latin_square(size):
	el = range(size)
	return np.array([[el[i - j] for i in el] for j in el])
	#return np.array([[el[i - j] for i in el] for j in range(size, 0, -1)])
	
def unique_cards(array):
	cards = []
	for r in array:
		l = set(r)
		if l not in cards:
			cards.append(l)

	return cards

num_elements = 8
per_card = 8

square = latin_square(num_elements)
print square
rows = range(0, num_elements-1, num_elements/per_card)

cards = square[:, rows]

print cards
good_cards = []
for i in range(len(cards)):
	card = set(list(cards[i, :]))
	if card not in good_cards:
		for c in good_cards:
			if len(card.intersection(c)) > 1:
				break
		else:
			good_cards.append(card)

print len(good_cards)