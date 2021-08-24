state = 1
transitions1 = {
    (1, '1'): 2,
    (1, '2'): 4,
    (2, '2'): 3,
    (3, '1'): 2,
    (3, '2'): 4,
    (4, '1'): 3,
}
transitions2 = {
    (1, '1'): 2,
    (2, 'b'): 3,
    (3, '1'): 2,
    (2, '2'): 3,
    (3, '2'): 4,
}

validstate = {3}


def afd(transition, stateAfd, valid, stringAfd):
    for word in stringAfd:
        try:
            stateAfd = transition[stateAfd, word]
        except KeyError:
            return False
    return stateAfd in valid


test = ['1', '2', '12', '121', '1122', '1221', '1221' * 3, '122' * 3, '211' * 3]

for string in test:
    if afd(transitions1, state, validstate, string):
        print(f'\n{string} Palavra valida!')
    else:
        print(f'\n{string} Palavra invalida!')

print('\nTESTANDO COM OUTRO TIPO DE TRANSIÇÃO')
for string in test:
    if afd(transitions2, state, validstate, string):
        print(f'\n{string} Palavra valida!')
    else:
        print(f'\n{string} Palavra invalida!')
