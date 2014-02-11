import numpy as np
from pprint import pprint
import random

#colors = ['rot', 'gruen', 'blau', 'gelb', 'orange', 'pink']
shapes = ['kreis', 'quadrat', 'blume', 'rhombus', 'sechseck', 'dreieck'] 

num_shapes = len(shapes)
# assert len(colors) == len(shapes)
el = range(num_shapes)

latin_square = np.array([[el[i - j] for i in el] for j in el])
poss = latin_square[:, 0:-1]

named = [ [shapes[c] for c in col] + [shapes[s] for s in sha] for col in poss for sha in poss]

for card in named:
	l, s = card[:num_shapes-1], card[num_shapes-1:]
	random.shuffle(l)
	random.shuffle(s)
	print 'Large: {}\nSmall: {}\n'.format(l, s)
	raw_input('')