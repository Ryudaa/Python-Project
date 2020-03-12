from tabulate import tabulate
from celline_graph import find_shortest_path as dist

# Mencari jarak antar vertex pada suatu graf #
##################################################################################
## -- Ini yang diedit -- ##

# List vertex
vertex1 = ['v1','v2','v3','v4','v5','v6','v7','v8','v9','v10','v11','v12']

# Keterhubungan vertex
# Format : 'vertex':['adjacent1','adjacent2']
#
# jika v1 adjacent dengan v2 maka ditulis dua kali (untuk setiap vertex)
# 'v1':['v2'],
# 'v2':['v1']
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

# Bisa tambah graf, kalo graf yang sebelumnya sayang dibuang
# jadi tulis lagi misal vertex2 = ['v1','v2',...], lalu vertex1 diganti vertex2
# begitu juga dengan g
vertex = vertex1
g = graph1
## -- Editnya sampai sini saja -- ##
##################################################################################
## -- Sini ke bawah jangan di edit -- ##

header = ['X']+vertex
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
