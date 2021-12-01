import sys
import math
import itertools
from decimal import *

HEX = '0123456789abcdef'
HEX2 = dict((a+b, HEX.index(a)*16 + HEX.index(b)) for a in HEX for b in HEX)


def rgb(triplet):
    triplet = triplet.lower()
    return (HEX2[triplet[0:2]], HEX2[triplet[2:4]], HEX2[triplet[4:6]])


def MidSort(lst):
  if len(lst) <= 1:
    return lst
  i = int(len(lst)/2)
  ret = [lst.pop(i)]
  left = MidSort(lst[0:i])
  right = MidSort(lst[i:])
  interleaved = [item for items in itertools.izip_longest(left, right)
    for item in items if item != None]
  ret.extend(interleaved)
  return ret


def GetColors(numColors):
    numColors += 1
    max = 255
    segs = int(numColors**(Decimal("1.0")/3))
    step = int(max/segs)
    p = [(i*step) for i in range(1,segs)]
    points = [0,max]
    points.extend(MidSort(p))
    colors = []
    rangee = 0
    total = 1
    while total < numColors and rangee < len(points):
      rangee += 1
      for c0 in range(rangee):
        for c1 in range(rangee):
          for c2 in range(rangee):
            if total >= numColors:
              break
            c = "%02X%02X%02X" % (points[c0], points[c1], points[c2])
            if rgb(c) not in colors:
              colors.append(rgb(c))
              total += 1
    return colors
