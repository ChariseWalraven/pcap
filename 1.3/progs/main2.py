import os

from sys import path

dir_path = os.path.dirname(os.path.realpath(__file__))

path.append(f'{dir_path}/../packages')

import extra.good.best.sigma as sig
import extra.good.alpha as alp

print(sig.FunS())
print(alp.FunA())
