print('import module')
from defgraph import write_file
from defgraph import ktwo
from defgraph import stwo
from defgraph import sthree
from defgraph import sfour

from graph import vertex
from graph import g

import sys

#if (len(sys.argv) > 1):
#    dimensi = sys.argv[1]
#else:

print('k2 : K-metrik dimensi 2')
print('s2 : S dengan ukuran 2')
print('s3 : S dengan ukuran 3')
print('s4 : S dengan ukuran 4')
dimensi = input('Pilih 1 : ')

# Dimensi 2 : two, dua, 2
if dimensi == 'k2':
    ktwo(vertex, g)
elif dimensi == 's2':
    stwo(vertex, g)
elif dimensi == 's3':
    sthree(vertex, g)
elif dimensi == 's4':
    sfour(vertex, g)
else:
    print('Dimensi tidak sesuai. Silahkan baca programs.py untuk info lebih lanjut')
    print('Untuk dimensi 2, tuliskan "2", "dua", atau "two" tanpa tanda petik')