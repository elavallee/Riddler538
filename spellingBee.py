import re
import cProfile
from itertools import combinations
from collections import defaultdict

def getWords():
    "Get all the words from enable1.txt."
    big = open(r'c:\Users\user\Documents\python\enable1.txt', 'r').readlines()
    return {x.lower().strip() for x in big if len(x) >= 5}

WORDS = getWords()

print(len(WORDS))
print(list(WORDS)[:10])

alphabet = set('abcdefghijklmnopqrstuvwxyz')

def findValidWords(outerLetters, centralLetter):
    """For a given lattice, find all valid words that meet the criteria:
    1. Words must 4 letters long or longer (this one taken care of above)
    2. The word must include the central letter
    3. The word cannot include any letters beyond the seven letters given"""
    assert len(outerLetters) == 6 and len(centralLetter) == 1
    excluded = alphabet - set(outerLetters + centralLetter)
    validWords = []
    for word in filter(lambda x: centralLetter in x, WORDS):
        hasExcluded = False
        for letter in set(word):
            if letter in excluded:
                hasExcluded = True
                break
        if not hasExcluded:
            validWords.append(word)
    return validWords

Nalphabet = set('abcdefghijklmnopqrtuvwxyz') # `s` is removed from this one

def makeDict() -> defaultdict:
    "Return a lookup from 7 letter latice to a set of possible words."
    possible = defaultdict(list)
    for word in WORDS:
        letters = ''.join(sorted(set(word)))
        possible[letters].append(word)
    return possible

possible = makeDict()

def findValidWords(outerLetters, centralLetter) -> list:
    """For a given lattice, find all valid words that meet the criteria:
    1. Words must 4 letters long or longer (this one taken care of above)
    2. The word must include the central letter
    3. The word cannot include any letters beyond the seven letters given"""
    lattice = ''.join(sorted(outerLetters + centralLetter))
    assert len(lattice) == 7
    words = list(possible[lattice])
    for x in range(3, 7):
        for combo in combinations(lattice, x):
            letters = ''.join(sorted(combo))
            words += list(possible[letters])
    return [word for word in words if centralLetter in word]

def testValidWords():
    validWords = findValidWords('lapemx', 'g')
    assert 'great' not in validWords
    assert 'maple' not in validWords
    assert 'gape' in validWords
    assert 'palm' not in validWords
    assert 'gale' in validWords
    assert 'apex' not in validWords
    assert 'page' in validWords
    assert 'pale' not in validWords
    assert 'game' in validWords
    print('Success!')

print('gape' in WORDS)
testValidWords()

def totalPoints(words, letters) -> int:
    "Return the total number of points for a list of words."
    assert len(letters) == 7
    total = 0
    for word in words:
        if len(word) == 4: total += 1
        else:
            total += len(word)
            if isPangram(word, letters): total += 7
    return total

def isPangram(word, letters) -> bool:
    "Determine if the word is a pangram."
    return all([x in word for x in letters])

def tests():
    assert isPangram('help', 'pleh')
    assert isPangram('help', 'help')
    assert isPangram('help', ('p', 'l', 'e', 'h'))
    assert not isPangram('help', 'ehlpa')
    print({x: totalPoints([x], 'lapemxg') for x in [x.lower() for x in ['AMALGAM', 'GAME', 'GLAM', 'MAPLE', 'MEGAPLEX', 'PELAGIC']]})
    assert totalPoints([x.lower() for x in reversed(['AMALGAM', 'GAME', 'GLAM', 'MAPLE', 'MEGAPLEX', 'PELAGIC'])], 'lapemxg') == 7 + 15 + 1 + 5 + 1 + 7
    print('Success!')

tests()

def findHighestScoring():
    "Find the 7 letter lattice that produces the highest score (excluding `s`)."
    maxScore = 0
    maxScoring = ('','')
    cnt = 0
    pangrams = [s for s in possible if len(s) == 7]
    for lattice in combinations(Nalphabet, 7):
        for letter in lattice:
            outerLetters = ''.join(set(lattice) - set(letter))
            validWords = findValidWords(outerLetters, letter)
            cnt += 1
            if any([isPangram(word, lattice) for word in validWords]):
                score = totalPoints(validWords, lattice)
                if score > maxScore:
                    maxScore = score
                    maxScoring = (outerLetters, letter)
    return maxScore, maxScoring

validWords = findValidWords('alpmex', 'g')
print(totalPoints(validWords, 'lapgmex'))
validWords = findValidWords('tiegna', 'r')
print(len(validWords))
score = totalPoints(validWords, ('t', 'i', 'e', 'g', 'n', 'a', 'r'))
print(score)
validWords = sorted(findValidWords('tiegna', 'r'))
print('REINTEGRATING'.lower() in validWords)
print(len(validWords))
print(totalPoints(findValidWords('tiegna', 'r'), 'tiegnar'))
#cProfile.run('findHighestScoring()')
print(findHighestScoring())
