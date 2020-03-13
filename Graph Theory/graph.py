from tabulate import tabulate
import itertools
import numpy
from celline_graph import find_shortest_path as dist
from celline_graph import write_file

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
jmlh_vertex = len(vertex)
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

tabel = tabulate(isi_table, headers=header, tablefmt="grid")+"\n"
#print(tabel)
write_file('output_tabel_jarak.txt', tabel)

comb = list(itertools.combinations(vertex, 2))
list_w = []
list_w_i = []
list_r = []
r_vj_w = []
list_v_memenuhi = []
for c in comb:
    kiri = c[0]
    #print(str(vertex.index(c[0])+1)+str(c[0]))
    kanan = c[1]
    #print(str(vertex.index(c[1])+1)+str(c[1]))
    index = comb.index(c)+1
    baris = vertex.index(c[0])+1 #posisi c[0]
    kolom = vertex.index(c[1])+1 #posisi c[1]
    jarak_baris_kolom = isi_table[baris-1][kolom]
    #isi_table[1][1]=baris 2 kolom 1
    
    w_i = "W"+str(index)+"("+str(c[0])+","+str(c[1])+")"
    w_string = "W("+str(c[0])+","+str(c[1])+")"
    r_v_w_i = "r("+str(c[0])+"|W"+str(index)+")={0,"+jarak_baris_kolom+"}"
    #print(w_i)
    #print(r_v_w_i)
    
    list_w_i.append(w_i)
    list_r.append(r_v_w_i)

    for i in range(0, len(vertex)):
        r_vj_w_i = "r("+str(vertex[i])+"|"+w_string+")={"+isi_table[i][baris]+","+isi_table[i][kolom]+"}"
        
        #cek kiri
        jumlah_sama_b = 0
        jumlah_sama_k = 0
        for j in range(0, len(vertex)):
            if isi_table[i][baris] == isi_table[j][baris]:
                jumlah_sama_b += 1
            if isi_table[i][kolom] == isi_table[j][kolom]:
                jumlah_sama_k += 1
        
        if (jumlah_sama_b == 1 and jumlah_sama_k == 1):
            r_vj_w.append(str(r_vj_w_i)+" Y")
            list_v_memenuhi.append(str("r("+str(vertex[i])+"|"+w_string+")"))
        else:
            r_vj_w.append(str(r_vj_w_i)+" N")

        #if (isi_table[i][kolom] == jarak_baris_kolom and i!=baris-1):
        #    r_vj_w.append(str(r_vj_w_i)+"BREAK")
        #    continue
        #r_vj_w.append(str(r_vj_w_i))
        #print(r_vj_w_i)

list_w.append(list_w_i)
list_w.append(list_r)
list_w = numpy.transpose(list_w)
tabel_2 = tabulate(list_w, tablefmt="grid")
write_file('output_tabel_w.txt', tabel_2)

#r_vj_w = numpy.transpose(r_vj_w)
tabel_3 = tabulate(r_vj_w)
write_file('output_tabel_rw.txt', tabel_3)
#print(r_vj_w)

tabel_4 = tabulate(list_v_memenuhi)
write_file('output_tabel_v_dan_w_yg_memenuhi.txt', tabel_4)

print("jarak antar vertex : output_tabel_jarak.txt")
print("semua kemungkinan w : output_tabel_w.txt")
print("r(v|w) : output_tabel_rw.txt")
print("r(v|w) yg memenuhi untuk semua vertex : output_tabel_v_dan_w_yg_memenuhi.txt")