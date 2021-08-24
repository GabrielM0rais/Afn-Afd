state = 0
transitions = {
    (0, '1'): [0],
    (0, '2'): [0, 1],
    (1, '1'): [2],
    (1, '2'): [2],
}
validstate = [2]


def afn(word, initial_state, transition, valid_state):
    if word == "":
        return initial_state in valid_state

    else:
        initialWord = word[0]
        if (initial_state, initialWord) in transition:
            for next_word in transition[(initial_state, initialWord)]:
                if afn(word[1:], next_word, transition, valid_state):
                    return True

            return False


test = ['1', '2', '12', '121', '1122', '1221', '211', '122' * 3, '211' * 3]

for string in test:
    if afn(string, state, transitions, validstate):
        print(f'\n{string} Palavra valida!')
    else:
        print(f'\n{string} Palavra invalida!')

