import numpy as np
import string


def get_ord(char1):
    if char1.isspace():
        return 26
    return ord(char1) - ord('A')


def clean_string(line):
    translator = str.maketrans(string.whitespace + 'Ã',
                               ' ' * len(string.whitespace) + 'a',
                               string.punctuation + 'ª' + '©' + '¤')
    line = line.translate(translator).strip()
    line_f = f" {line.upper()} "
    return line_f


def get_transition_probs():
    t_count = np.zeros((27, 27))
    with open("C:/Users/jacob/Documents/GitHub/MCCypher/mc_cypher/warandpeace.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            line_f = clean_string(line)
            for i, char in enumerate(line_f[:-1]):
                index1 = get_ord(char)
                index2 = get_ord(line_f[i+1])
                t_count[index1, index2] += 1

    letter_count = np.expand_dims(t_count.sum(1), 1)
    t_prob = t_count / letter_count
    return t_prob








