from mc_cypher import transition_probs, cypher
import matplotlib.pyplot as plt
import numpy as np


def main():
    t_probs = transition_probs.get_transition_probs()
    cyph = cypher.Cypher()
    swaps = []
    scores = []
    ciphered_text = 'a'
    for i in range(1000):
        swap, score = cyph.consider_swap_random(ciphered_text, t_probs)
        swaps.append(swap)
        scores.append(score)
    plt.plot(scores)
    print(swaps)
