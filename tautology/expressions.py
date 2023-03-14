import collections
import itertools
from time import sleep


# check if expression 'w' is written correctly
def check(w):
    nb = 0  # number of brackets
    state = True
    for c in w:
        if state:  # want letter, true, false, '(' or '~'
            if c in ')&|>^':
                return False
            elif c.islower() or c in 'TF':
                state = False
        else:  # want operator or ')'
            if c.islower() or c in '(~TF':
                return False
            elif c in '&|>^':
                state = True
        if c == '(':
            nb += 1
        elif c == ')':
            nb -= 1
        if nb < 0:
            return False
    return nb == 0 and not state


# remove external brackets from expression 'w'
def bracket(w):
    while w[0] == '(' and w[-1] == ')' and check(w[1:-1]):
        w = w[1:-1]
    return w


# return the position of the rightmost operator 'op' not in brackets in expression 'w'
def bal(w, op):
    nb = 0
    for i in range(len(w) - 1, -1, -1):
        if w[i] == ')':
            nb += 1
        elif w[i] == '(':
            nb -= 1
        if nb == 0 and w[i] in op:
            return i
    return None


# convert an expression 'w' from infix form to ONP form
def onp(w):
    w = bracket(w)
    p = bal(w, '>')
    if p:
        return onp(w[:p]) + onp(w[p + 1:]) + w[p]
    p = bal(w, '&|')
    if p:
        return onp(w[:p]) + onp(w[p + 1:]) + w[p]
    p = bal(w, '^')
    if p:
        return onp(w[:p]) + onp(w[p + 1:]) + w[p]
    p = bal(w, '~')
    if p is not None:   # negation can be on position 0
        return onp(w[p + 1:]) + w[p]
    return w


# map letters in expression 'w' to their logical values from dictionary 'vec'
# and replace T and F with 1 and 0
def map1(w, vec):
    w1 = list(w)
    for i in range(len(w)):
        if w[i].islower():
            w1[i] = str(vec[w[i]])
        elif w[i] == 'T':
            w1[i] = str(1)
        elif w[i] == 'F':
            w1[i] = str(0)
    w = ''.join(w1)
    return w


# generate 0/1 combinations of length 'x'
def gen(x):
    combinations = list(itertools.product([0, 1], repeat=x))
    for comb in combinations:
        yield comb


# generate dictionaries with letters contained in expression 'w' and their logical value for every 0/1 combination
def letters_values(w):
    num_of_letters = 0
    letters = collections.defaultdict(int)
    for i in range(len(w)):
        if w[i].islower() and w[i] not in w[:i]:
            num_of_letters += 1
            letters[w[i]] = 0
    for comb in gen(num_of_letters):
        i = 0
        for letter in list(letters.keys()):
            letters[letter] = comb[i]
            i += 1
        yield letters


# evaluate a logical expression 'w'
# expression in ONP form and with mapped values
def val(w):
    for i in range(len(w)):
        if w[i] == '~':
            if w[i-1] == '1':
                return val(w[:i - 1] + '0' + w[i + 1:])
            else:
                return val(w[:i - 1] + '1' + w[i + 1:])
        elif w[i] == '^':
            if (w[i - 2] == '1' and w[i - 1] == '0') or (w[i - 2] == '0' and w[i - 1] == '1'):
                return val(w[:i - 2] + '1' + w[i + 1:])
            else:
                return val(w[:i - 2] + '0' + w[i + 1:])
        elif w[i] == '&':
            if w[i - 2] == '1' and w[i - 1] == '1':
                return val(w[:i - 2] + '1' + w[i + 1:])
            else:
                return val(w[:i - 2] + '0' + w[i + 1:])
        elif w[i] == '|':
            if w[i - 2] == '0' and w[i - 1] == '0':
                return val(w[:i - 2] + '0' + w[i + 1:])
            else:
                return val(w[:i - 2] + '1' + w[i + 1:])
        elif w[i] == '>':
            if w[i - 2] == '1' and w[i - 1] == '0':
                return val(w[:i - 2] + '0' + w[i + 1:])
            else:
                return val(w[:i - 2] + '1' + w[i + 1:])
    return int(w)


# check if expression 'w' is a tautology
def tautology(w):
    for letters in letters_values(w):
        if val(map1(onp(w), letters)) == 0:
            return False
    return True


# check if two expressions 'w' and 'z' are equivalent
def are_equivalent(w, z):
    both = w + z
    for letters in letters_values(both):
        if val(map1(onp(w), letters)) != val(map1(onp(z), letters)):
            return False
    return True


# expression input assistant
def input_expression():
    while True:
        expression = input(">>")
        if check(expression) is False:
            print('you have to enter correct expression')
        else:
            break
    return expression


if __name__ == '__main__':
    while True:
        print('\nwhat do you want to do?')
        print('0 quit')
        print('1 check if the expression is a tautology')
        print('2 check if two expressions are equivalent')
        choice = input(">>")
        if choice == '0':
            print('closing...')
            sleep(1)
            break
        elif choice == '1':
            print('you can use lower letters as variables, T (true), F (false) and operators: ')
            print('& (and), | (or), > (implies), ~ (not), ^ (xor)')
            expr = input_expression()
            print('is tautology? ', tautology(expr))
        elif choice == '2':
            print('you can use lower letters as variables, T (true), F (false) and operators: ')
            print('& (and), | (or), > (implies), ~ (not), ^ (xor)')
            expr1 = input_expression()
            expr2 = input_expression()
            print('are equivalent?', are_equivalent(expr1, expr2))
        else:
            print('you have to type 0, 1 or 2')
            input('press enter to continue')
