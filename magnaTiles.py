# Solution to the classic puzzle here: https://fivethirtyeight.com/features/can-you-roll-the-perfect-bowl/

import math

# assume a length of the tiles, this length is from the midpoint of the
# magna tile base to it's peak
l = 2.0 # inches

# w is the measurement of the magna tile base
def getW(l): return 2 * l / math.tan(math.radians(75))

# alpha is the interior angle of an N sided polygon
def getAlpha(N): return math.radians(180 - 360 / N)

# x is the distance from the center of the polygon to a midpoint of one of it's
# sides
def getX(alpha, w): return (w / 2) * math.tan(alpha / 2)

# area of the magna tile
def getArea(w, l): return (1 / 2) * w * l

# theta is the angle between the magna tile and the ground
def getTheta(x, l): return math.acos(x / l)

# volume under the tiles
def volume(A, h, N, theta): return (1 / 2) * A * math.cos(theta) * h * N

# get the height of the pyramid
def getHeight(l, x): return math.sqrt(l**2 - x**2)

def getMax():
    "Return the number of tiles that gives the maximum volume under them."
    alphas = [getAlpha(x) for x in range(3, 12)]
    w = getW(l)
    xs = [getX(x, w) for x in alphas]
    thetas = [getTheta(x, l) for x in xs]
    A = getArea(w, l)
    vs = [volume(A, getHeight(l, x), n, theta)
          for x, n, theta in zip(xs, range(3, 12), thetas)]
    ix = vs.index(max(vs))
    return ix + 3

print(getMax())
