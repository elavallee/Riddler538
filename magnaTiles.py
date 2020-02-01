import math

# assume a length of the tiles, this length is from the midpoint of the
# magna tile base to it's peak
l = 2 # inches

# w is the measurement of the magna tile base
def getW(l): return 2 * l / math.tan(math.radians(75))

# alpha is the interior angle of an N sided polygon
def getAlpha(N): return math.radians(180 - 360 / N)

# x is the distance from the center of the polygon to a midpoint of one of it's
# sides
def getX(alpha, w): return (w / 2) * math.tan(alpha / 2)

# area of the magna tile
def getArea(w, l): return (1 / 2) * w * l

# volume under the tiles
def volume(A, h, N): return (1 / 2) * A * h * N

# get the height of the pyramid
def getHeight(l, x): return math.sqrt(l**2 - x**2)

def getMax():
    "Return the number of tiles that gives the maximum volume under them."
    alphas = [getAlpha(x) for x in range(3, 12)]
    w = getW(l)
    xs = [getX(x, w) for x in alphas]
    A = getArea(w, l)
    vs = [volume(A, getHeight(l, x), n) for x, n in zip(xs, range(3, 12))]
    ix = vs.index(max(vs))
    return ix+3

print(getMax())
