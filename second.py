import random
from pprint import pprint
from matplotlib import pyplot as plt
import numpy as np

num_elements = 50
per_card = 8
num_common = 1

elements = range(num_elements)


## A generator for cards.
def card_generator(num_elements, per_card):
	el = range(num_elements)
	latin_square = np.array([[el[i - j] for i in el] for j in el])
	num = 0
	rows = range(0, num_elements-1, num_elements/per_card)
	cards = square[:, rows]
	yield


cards = []
# How many tries did the card take
tries = []
cur_tries = 0

card_gen = card_generator(num_elements, per_card)

for i in xrange(10000):
	cur_tries += 1

	try:
		card = card_gen.next()
	except StopIteration:
		break

	if card not in cards:
		for c in cards:
			if len(card.intersection(c)) != 1:
				break
		else:
			cards.append(card)
			tries.append(cur_tries)
			cur_tries = 0

print 'Found {} cards. Last card took {} tries.'.format(len(cards), tries[-1])
pprint(cards)
pprint(tries)
plt.plot(range(1, len(tries)+1), tries)
plt.show()