from collections import Counter
from random import choices, choice
from itertools import chain

rps = ['R', 'P', 'S']
rep = {'P': 'S', 'R': 'P', 'S': 'R'}

def sp(events, baseline=()):
    rel_freq = Counter(chain(baseline, events))
    population, weights = zip(*rel_freq.items())
    return choices(population, weights)[0]

def sm(events, baseline=()):
    rel_freq = Counter(chain(baseline, events))
    return rel_freq.most_common(1)[0][0]

def rr(bot, player):
    return choice(rps)

def sep(bot, player):
    pred = sp(player, rps)
    return rep[pred]

def seg(bot, player):
    pred = sm(player, rps)
    return rep[pred]

def dep(bot, player):
    rp = player[-1:]
    d = zip(player, player[1:])
    f = [b for a, b in d if a == rp]
    pred = sp(f, rps)
    return rep[pred]

def deg(bot, player):
    rp = player[-1:]
    d = zip(player, player[1:])
    f = [b for a, b in d if a == rp]
    pred = sm(f, rps)
    return rep[pred]
