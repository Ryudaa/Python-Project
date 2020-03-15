print('import module')
from defgraph import write_file
from defgraph import two

from graph import vertex
from graph import g

import sys

if (len(sys.argv) > 1):
    dimensi = sys.argv[1]

else:
    dimensi = input('Masukan dimensi : ')

# Dimensi 2 : two, dua, 2
if (dimensi == 'two' or dimensi == 'dua' or dimensi == '2'):
    two(vertex, g)
else:
    print('Dimensi tidak sesuai. Silahkan baca programs.py untuk info lebih lanjut')