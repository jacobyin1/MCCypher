import numpy as np
from mc_cypher import transition_probs

p = transition_probs.get_transition_probs()
b = np.all(np.isclose(np.sum(p, 1), np.ones(27)))

a = dict()
a['2'] = '2'
print(a['2'])
