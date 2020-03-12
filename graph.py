from tabulate import tabulate
from celline_graph import find_shortest_path as dist

##################################################################################

vertex = ['v1','v2','v3','v4','v5','v6','v7','v8','v9','v10','v11','v12']
header = ['X']+vertex

graph1 = {'v1':['v2','v4'],
    'v2':['v1','v3','v7'],
    'v3':['v2','v10'],
    'v4':['v1','v5','v6'],
    'v5':['v4'],
    'v6':['v4'],
    'v7':['v2','v8','v9'],
    'v8':['v7'],
    'v9':['v7'],
    'v10':['v3','v11','v12'],
    'v11':['v10'],
    'v12':['v10'],
    }

g = graph1
##################################################################################

isi_table = []

for v in vertex:
    isi_kolom = [v]
    for w in vertex:
        list_path = dist(g,v,w)
        panjang = str(len(list_path)-1)
        isi_kolom = isi_kolom + [panjang]
    isi_table.append(isi_kolom)

print("Jarak antar vertex :")
print(tabulate(isi_table, headers=header, tablefmt="grid"))