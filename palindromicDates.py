from datetime import date, timedelta

def isPalin(word) -> bool:
    "Return true if the word is a palindrome."
    word = word.lower()
    return word == word[::-1]

dayd = timedelta(days=1)
today = date.today()
current = today
for _ in range(int(365.25*100)):
    month = "{:02d}".format(current.month)
    day = "{:02d}".format(current.day)
    year = str(current.year)
    if current.year < 2100 and isPalin(month + day + year):
        print("{:%m/%d/%Y}".format(current))
    current = current + dayd
