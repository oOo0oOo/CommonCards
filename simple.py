import random
from pprint import pprint
from matplotlib import pyplot as plt

num_elements = 50
per_card = 8
num_common = 2

elements = range(num_elements)

cards = []
# How many tries did the card take
tries = []
cur_tries = 0
for i in xrange(5000000):
	cur_tries += 1

	card = set( random.sample(elements, per_card) )
	if card not in cards:
		for c in cards:
			if len(card.intersection(c)) != num_common:
				break
		else:
			cards.append(card)
			tries.append(cur_tries)
			cur_tries = 0

print 'Found {} cards. {} tries since last card.'.format(len(cards), cur_tries)
pprint(cards)
pprint(tries)
plt.plot(range(1, len(tries)+1), tries)
plt.show()