import random

avgs = {}


def detect_turn(pvel, pposx, pposy, cvel, cposx, cposy, cid):

    cval, samples = avgs.get(cid, (0, 0))

    cavg = (cval / samples) if samples != 0 else 0

    result, nval = _probable_turn(pvel, pposx, pposy, cvel, cposx, cposy, cavg)
    avgs[ci] = (cval + nval, samples + 1)

    return 0


def _probable_turn(pvel, pposx, pposy, cvel, cposx, cposy, avg):
    return True, random.randint(10)
