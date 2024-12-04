import string
import transition_probs
import math
import random


class Cypher:
    def __init__(self, cypher_values=string.ascii_uppercase + ' '):
        keys = string.ascii_uppercase + ' '
        self.cypher_map = dict(zip(keys, cypher_values))

    def score(self, ciphered_text, t_probs):
        score = 0
        ciphered_text = transition_probs.clean_string(ciphered_text)
        for i, c in enumerate(ciphered_text[:-1]):
            c1_deciphered = self.cypher_map.get(c)
            c2_deciphered = self.cypher_map.get(ciphered_text[i+1])
            index1 = transition_probs.get_ord(c1_deciphered)
            index2 = transition_probs.get_ord(c2_deciphered)
            score += math.log(t_probs[index1, index2])
        return score

    def consider_swap_random(self, ciphered_text, t_probs):
        rand_key1 = random.choice(self.cypher_map.keys())
        rand_key2 = random.choice(self.cypher_map.keys())
        b, score = self.consider_swap(ciphered_text, t_probs, (rand_key1, rand_key2))
        return b, score

    def consider_swap(self, ciphered_text, t_probs, swap_keys):
        s_f = self.score(ciphered_text, t_probs)
        self.__swap(swap_keys)
        s_f_star = self.score(ciphered_text, t_probs)

        swapped = True
        if s_f_star < s_f:
            p_keep_swap = math.exp(s_f_star) / math.exp(s_f)
            if random.random() >= p_keep_swap:
                k1, k2 = swap_keys
                self.__swap((k2, k1))
                swapped = False
                return swapped, s_f
        return swapped, s_f_star

    def __swap(self, swap_keys):
        key1, key2 = swap_keys
        temp = self.cypher_map[key1]
        self.cypher_map[key1] = self.cypher_map[key2]
        self.cypher_map[key2] = temp




