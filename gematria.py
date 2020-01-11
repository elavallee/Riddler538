ones = {1:  'ONE',
        2:  'TWO',
        3:  'THREE',
        4:  'FOUR',
        5:  'FIVE',
        6:  'SIX',
        7:  'SEVEN',
        8:  'EIGHT',
        9:  'NINE',
        10: 'TEN',
        11: 'ELEVEN',
        12: 'TWELVE',
        13: 'THIRTEEN',
        14: 'FOURTEEN',
        15: 'FIFTEEN',
        16: 'SIXTEEN',
        17: 'SEVENTEEN',
        18: 'EIGHTEEN',
        19: 'NINTEEN'}

tens = {2: 'TWENTY',
        3: 'THIRTY',
        4: 'FORTY',
        5: 'FIFTY',
        6: 'SIXTY',
        7: 'SEVENTY',
        8: 'EIGHTY',
        9: 'NINETY'}

def convert(num) -> str:
    "Convert the number num to it's written out string form (21 -> TWENTY ONE)."
    if num == 0: return ''
    elif num < 20: return ones[num]
    elif num < 100:
        return tens[num // 10] + ' ' + convert(num - (num // 10) * 10)
    elif num < 1000:
        return ones[num // 100] + ' HUNDRED ' + convert(num - (num // 100) * 100)
    elif num < 1000000:
        return (convert(num // 1000) + ' THOUSAND ' +
                convert(num - (num //1000) * 1000))
    elif num < 1000000000:
        return (convert(num // 1000000) + ' MILLION ' +
                convert(num - (num // 1000000) * 1000000))
    else:
        raise ValueError('This function is not yet able to handle numbers over a billion.')

print(convert(1417))
print(convert(379))
print(convert(3))
print(convert(99))
print(convert(912000))
print(convert(3140275))

alphabet = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8,
            'I': 9, 'J': 10, 'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15,
            'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20, 'U': 21, 'V': 22,
            'W': 23, 'X': 24, 'Y': 25, 'Z': 26}

def getLetterVal(letter) -> int:
    "Return the integer value of a letter (A = 1, ... Z = 26)."
    return alphabet[letter]

WORDS = {}

def gematria(num) -> int:
    "Return the coded value of number num."
    global WORDS
    words = convert(num).split()
    total = 0
    for word in words:
        if word in WORDS:
            total += WORDS[word]
        else:
            tmp = sum([getLetterVal(letter) for letter in word])
            WORDS[word] = tmp
            total += tmp
    return total

def tests():
    assert gematria(1417) == 379
    assert gematria(3140275) == 718
    print('Passed!')

tests()

def findLargest(small=1, large=1000000) -> int:
    "Find the largest number whose Gematria code is greater than it's value."
    for x in range(large, small - 1, -1):
        if gematria(x) >= x: return x

num = findLargest(1, 1000)
print('{} = {}'.format(convert(num), gematria(num)))
print('{} = {}'.format(convert(num+1), gematria(num+1)))
