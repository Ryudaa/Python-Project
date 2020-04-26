from tabulate import tabulate
import itertools
import numpy
import os

def dist(graphh, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    if start not in graphh:
        return None
    shortest = None
    for node in graphh[start]:
        if node not in path:
            newpath = dist(graphh, node, end, path)
            if newpath:
                if not shortest or len(newpath) < len(shortest):
                    shortest = newpath
    return shortest

def write_file(nama, text):
    location = 'Output\\'+nama
    saveFile = open(location, 'w')
    saveFile.write(text)
    saveFile.close()

def ktwo(vertex, g):
    if not os.path.exists('Output'):
        os.makedirs('Output')
    jmlh_vertex = len(vertex)
    header = ['X']+vertex
    isi_table = []

    print('mencari jarak antar vertex...')
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
    print("jarak antar vertex : output_tabel_jarak.txt")

    comb = list(itertools.combinations(vertex, 2))
    list_w = []
    list_w_i = []
    list_r = []
    r_vj_w = []
    list_v_memenuhi = []

    print('mennghitung r(v|w) dan membandingkannya')
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

        for i in range(0, jmlh_vertex):
            r_vj_w_i = "r("+str(vertex[i])+"|"+w_string+")={"+isi_table[i][baris]+","+isi_table[i][kolom]+"}"
            
            #cek kiri
            jumlah_sama_b = 0
            jumlah_sama_k = 0
            for j in range(0, jmlh_vertex):
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

    tabel_3 = tabulate(r_vj_w)
    write_file('output_rw(2).txt', tabel_3)
    print("r(v|w) : output_rw(2).txt")

    tabel_4 = tabulate(list_v_memenuhi)
    write_file('output_tabel_v_dan_w(2)_yg_memenuhi.txt', tabel_4)
    print("r(v|w) yg memenuhi untuk semua vertex : output_tabel_v_dan_w(2)_yg_memenuhi.txt")

def stwo(vertex, g):
    if not os.path.exists('Output'):
        os.makedirs('Output')
    jmlh_vertex = len(vertex)
    header = ['X']+vertex
    isi_table = []

    print('mencari jarak antar vertex...')
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
    print("jarak antar vertex : output_tabel_jarak.txt")

    comb = list(itertools.combinations(vertex, 2))
    comb2 = list(itertools.combinations(range(0, jmlh_vertex), 2))
    list_s = []
    list_s_i = []
    list_r = []
    r_vj_s = []
    list_v_memenuhi = []

    print('menghitung r(v|s) dan membandingkannya')
    for c in comb:
        kiri = c[0]
        #print(str(vertex.index(c[0])+1)+str(c[0]))
        kanan = c[1]
        #print(str(vertex.index(c[1])+1)+str(c[1]))
        index = comb.index(c)+1
        baris = vertex.index(c[0])+1 #posisi c[0]
        kolom = vertex.index(c[1])+1 #posisi c[1]
        p1 = vertex.index(c[0])+1 #posisi c[0]
        p2 = vertex.index(c[1])+1 #posisi c[1]
        jarak_baris_kolom = isi_table[baris-1][kolom]
        #isi_table[1][1]=baris 2 kolom 1

    for c in comb2:
        s_i = "S={"+str(isi_table[c[0]][0])+","+str(isi_table[c[1]][0])+"}"
        #s_string = "S("+str(c[0])+","+str(c[1])+","+str(c[2])+")"
        #r_v_s_i = "r("+str(c[0])+"|S"+str(index)+")={0,"+jarak_baris_kolom+"}"
        #print(s_i)
        #print(r_v_s_i)
        
        list_s_i.append(s_i)
        #cek kiri
        jumlah_sama = 0
        for k in comb2:
            #if1 = 'isi_table[' + str(k[0]) + '][' + str(c[0]+1) + ']' + str(isi_table[k[0]][c[0]+1]) + ' ' + 'isi_table[' + str(k[1]) + '][' + str(c[0]+1) + ']' + str(isi_table[k[1]][c[0]+1])
            #if2 = 'isi_table[' + str(k[0]) + '][' + str(c[1]+1) + ']' + str(isi_table[k[0]][c[1]+1]) + ' ' + 'isi_table[' + str(k[1]) + '][' + str(c[1]+1) + ']' + str(isi_table[k[1]][c[1]+1])
            #if3 = 'isi_table[' + str(k[0]) + '][' + str(c[2]+1) + ']' + str(isi_table[k[0]][c[2]+1]) + ' ' + 'isi_table[' + str(k[1]) + '][' + str(c[2]+1) + ']' + str(isi_table[k[1]][c[2]+1])
            #print(if1+if2+if3)
            if isi_table[k[0]][c[0]+1] == isi_table[k[1]][c[0]+1]:
                if isi_table[k[0]][c[1]+1] == isi_table[k[1]][c[1]+1]:
                    jumlah_sama += 1

        if (jumlah_sama == 0):
            r_vj_s.append(str(s_i)+" Y")
            list_v_memenuhi.append(str(s_i))
        else:
            r_vj_s.append(str(s_i)+" N")

        #if (isi_table[i][kolom] == jarak_baris_kolom and i!=baris-1):
        #    r_vj_w.append(str(r_vj_w_i)+"BREAK")
        #    continue
        #r_vj_w.append(str(r_vj_w_i))
        #print(r_vj_w_i)

    tabel_3 = tabulate(r_vj_s)
    write_file('output_rs(2).txt', tabel_3)
    print("r(v|s) : output_rs(2).txt")

    tabel_4 = tabulate(list_v_memenuhi)
    write_file('output_tabel_v_dan_s(2)_yg_memenuhi.txt', tabel_4)
    print("r(v|s) yg memenuhi untuk semua vertex : output_tabel_v_dan_s(2)_yg_memenuhi.txt")

def sthree(vertex, g):
    if not os.path.exists('Output'):
        os.makedirs('Output')
    jmlh_vertex = len(vertex)
    header = ['X']+vertex
    isi_table = []

    print('mencari jarak antar vertex...')
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
    print("jarak antar vertex : output_tabel_jarak.txt")

    comb = list(itertools.combinations(vertex, 2))
    comb2 = list(itertools.combinations(range(0, jmlh_vertex), 2))
    comb3 = list(itertools.combinations(range(0, jmlh_vertex), 3))
    list_s = []
    list_s_i = []
    list_r = []
    r_vj_s = []
    list_v_memenuhi = []

    print('menghitung r(v|s) dan membandingkannya')
    for c in comb:
        kiri = c[0]
        #print(str(vertex.index(c[0])+1)+str(c[0]))
        kanan = c[1]
        #print(str(vertex.index(c[1])+1)+str(c[1]))
        index = comb.index(c)+1
        baris = vertex.index(c[0])+1 #posisi c[0]
        kolom = vertex.index(c[1])+1 #posisi c[1]
        p1 = vertex.index(c[0])+1 #posisi c[0]
        p2 = vertex.index(c[1])+1 #posisi c[1]
        jarak_baris_kolom = isi_table[baris-1][kolom]
        #isi_table[1][1]=baris 2 kolom 1

    for c in comb3:
        s_i = "S={"+str(c[0]+1)+","+str(c[1]+1)+","+str(c[2]+1)+"}"
        #s_string = "S("+str(c[0])+","+str(c[1])+","+str(c[2])+")"
        #r_v_s_i = "r("+str(c[0])+"|S"+str(index)+")={0,"+jarak_baris_kolom+"}"
        #print(s_i)
        #print(r_v_s_i)
        
        list_s_i.append(s_i)
        #cek kiri
        jumlah_sama = 0
        for k in comb2:
            #if1 = 'isi_table[' + str(k[0]) + '][' + str(c[0]+1) + ']' + str(isi_table[k[0]][c[0]+1]) + ' ' + 'isi_table[' + str(k[1]) + '][' + str(c[0]+1) + ']' + str(isi_table[k[1]][c[0]+1])
            #if2 = 'isi_table[' + str(k[0]) + '][' + str(c[1]+1) + ']' + str(isi_table[k[0]][c[1]+1]) + ' ' + 'isi_table[' + str(k[1]) + '][' + str(c[1]+1) + ']' + str(isi_table[k[1]][c[1]+1])
            #if3 = 'isi_table[' + str(k[0]) + '][' + str(c[2]+1) + ']' + str(isi_table[k[0]][c[2]+1]) + ' ' + 'isi_table[' + str(k[1]) + '][' + str(c[2]+1) + ']' + str(isi_table[k[1]][c[2]+1])
            #print(if1+if2+if3)
            if isi_table[k[0]][c[0]+1] == isi_table[k[1]][c[0]+1]:
                if isi_table[k[0]][c[1]+1] == isi_table[k[1]][c[1]+1]:
                    if isi_table[k[0]][c[2]+1] == isi_table[k[1]][c[2]+1]:
                        jumlah_sama += 1

        if (jumlah_sama == 0):
            r_vj_s.append(str(s_i)+" Y")
            list_v_memenuhi.append(str(s_i))
        else:
            r_vj_s.append(str(s_i)+" N")

        #if (isi_table[i][kolom] == jarak_baris_kolom and i!=baris-1):
        #    r_vj_w.append(str(r_vj_w_i)+"BREAK")
        #    continue
        #r_vj_w.append(str(r_vj_w_i))
        #print(r_vj_w_i)

    tabel_3 = tabulate(r_vj_s)
    write_file('output_rs(3).txt', tabel_3)
    print("r(v|s) : output_rs(3).txt")

    tabel_4 = tabulate(list_v_memenuhi)
    write_file('output_tabel_v_dan_s(3)_yg_memenuhi.txt', tabel_4)
    print("r(v|s) yg memenuhi untuk semua vertex : output_tabel_v_dan_s(3)_yg_memenuhi.txt")

def sfour(vertex, g):
    if not os.path.exists('Output'):
        os.makedirs('Output')
    jmlh_vertex = len(vertex)
    header = ['X']+vertex
    isi_table = []

    print('mencari jarak antar vertex...')
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
    print("jarak antar vertex : output_tabel_jarak.txt")

    comb = list(itertools.combinations(vertex, 2))
    comb2 = list(itertools.combinations(range(0, jmlh_vertex), 2))
    comb4 = list(itertools.combinations(range(0, jmlh_vertex), 4))
    list_s = []
    list_s_i = []
    list_r = []
    r_vj_s = []
    list_v_memenuhi = []

    print('mennghitung r(v|s) dan membandingkannya')
    for c in comb:
        kiri = c[0]
        #print(str(vertex.index(c[0])+1)+str(c[0]))
        kanan = c[1]
        #print(str(vertex.index(c[1])+1)+str(c[1]))
        index = comb.index(c)+1
        baris = vertex.index(c[0])+1 #posisi c[0]
        kolom = vertex.index(c[1])+1 #posisi c[1]
        p1 = vertex.index(c[0])+1 #posisi c[0]
        p2 = vertex.index(c[1])+1 #posisi c[1]
        jarak_baris_kolom = isi_table[baris-1][kolom]
        #isi_table[1][1]=baris 2 kolom 1

    for c in comb4:
        s_i = "S={"+str(isi_table[c[0]][0])+","+str(isi_table[c[1]][0])+","+isi_table[c[2]][0]+","+str(isi_table[c[3]][0])+"}"
        #s_string = "S("+str(c[0])+","+str(c[1])+","+str(c[2])+")"
        #r_v_s_i = "r("+str(c[0])+"|S"+str(index)+")={0,"+jarak_baris_kolom+"}"
        #print(s_i)
        #print(r_v_s_i)
        
        list_s_i.append(s_i)
        #cek kiri
        jumlah_sama = 0
        for k in comb2:
            #if1 = 'isi_table[' + str(k[0]) + '][' + str(c[0]+1) + ']' + str(isi_table[k[0]][c[0]+1]) + ' ' + 'isi_table[' + str(k[1]) + '][' + str(c[0]+1) + ']' + str(isi_table[k[1]][c[0]+1])
            #if2 = 'isi_table[' + str(k[0]) + '][' + str(c[1]+1) + ']' + str(isi_table[k[0]][c[1]+1]) + ' ' + 'isi_table[' + str(k[1]) + '][' + str(c[1]+1) + ']' + str(isi_table[k[1]][c[1]+1])
            #if3 = 'isi_table[' + str(k[0]) + '][' + str(c[2]+1) + ']' + str(isi_table[k[0]][c[2]+1]) + ' ' + 'isi_table[' + str(k[1]) + '][' + str(c[2]+1) + ']' + str(isi_table[k[1]][c[2]+1])
            #print(if1+if2+if3)
            if isi_table[k[0]][c[0]+1] == isi_table[k[1]][c[0]+1]:
                if isi_table[k[0]][c[1]+1] == isi_table[k[1]][c[1]+1]:
                    if isi_table[k[0]][c[2]+1] == isi_table[k[1]][c[2]+1]:
                        if isi_table[k[0]][c[3]+1] == isi_table[k[1]][c[3]+1]:
                            jumlah_sama += 1

        if (jumlah_sama == 0):
            r_vj_s.append(str(s_i)+" Y")
            list_v_memenuhi.append(str(s_i))
        else:
            r_vj_s.append(str(s_i)+" N")

        #if (isi_table[i][kolom] == jarak_baris_kolom and i!=baris-1):
        #    r_vj_w.append(str(r_vj_w_i)+"BREAK")
        #    continue
        #r_vj_w.append(str(r_vj_w_i))
        #print(r_vj_w_i)

    tabel_3 = tabulate(r_vj_s)
    write_file('output_rs(4).txt', tabel_3)
    print("r(v|s) : output_rs(4).txt")

    tabel_4 = tabulate(list_v_memenuhi)
    write_file('output_tabel_v_dan_s(4)_yg_memenuhi.txt', tabel_4)
    print("r(v|s) yg memenuhi untuk semua vertex : output_tabel_v_dan_s(4)_yg_memenuhi.txt")

def sfive(vertex, g):
    if not os.path.exists('Output'):
        os.makedirs('Output')
    jmlh_vertex = len(vertex)
    header = ['X']+vertex
    isi_table = []

    print('mencari jarak antar vertex...')
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
    print("jarak antar vertex : output_tabel_jarak.txt")

    comb = list(itertools.combinations(vertex, 2))
    comb2 = list(itertools.combinations(range(0, jmlh_vertex), 2))
    comb5 = list(itertools.combinations(range(0, jmlh_vertex), 5))
    list_s = []
    list_s_i = []
    list_r = []
    r_vj_s = []
    list_v_memenuhi = []

    print('mennghitung r(v|s) dan membandingkannya')
    for c in comb:
        kiri = c[0]
        #print(str(vertex.index(c[0])+1)+str(c[0]))
        kanan = c[1]
        #print(str(vertex.index(c[1])+1)+str(c[1]))
        index = comb.index(c)+1
        baris = vertex.index(c[0])+1 #posisi c[0]
        kolom = vertex.index(c[1])+1 #posisi c[1]
        p1 = vertex.index(c[0])+1 #posisi c[0]
        p2 = vertex.index(c[1])+1 #posisi c[1]
        jarak_baris_kolom = isi_table[baris-1][kolom]
        #isi_table[1][1]=baris 2 kolom 1

    for c in comb5:
        s_i = "S={"+str(isi_table[c[0]][0])+","+str(isi_table[c[1]][0])+","+isi_table[c[2]][0]+","+str(isi_table[c[3]][0])+","+str(isi_table[c[4]][0])+"}"
        #s_string = "S("+str(c[0])+","+str(c[1])+","+str(c[2])+")"
        #r_v_s_i = "r("+str(c[0])+"|S"+str(index)+")={0,"+jarak_baris_kolom+"}"
        #print(s_i)
        #print(r_v_s_i)
        
        list_s_i.append(s_i)
        #cek kiri
        jumlah_sama = 0
        for k in comb2:
            #if1 = 'isi_table[' + str(k[0]) + '][' + str(c[0]+1) + ']' + str(isi_table[k[0]][c[0]+1]) + ' ' + 'isi_table[' + str(k[1]) + '][' + str(c[0]+1) + ']' + str(isi_table[k[1]][c[0]+1])
            #if2 = 'isi_table[' + str(k[0]) + '][' + str(c[1]+1) + ']' + str(isi_table[k[0]][c[1]+1]) + ' ' + 'isi_table[' + str(k[1]) + '][' + str(c[1]+1) + ']' + str(isi_table[k[1]][c[1]+1])
            #if3 = 'isi_table[' + str(k[0]) + '][' + str(c[2]+1) + ']' + str(isi_table[k[0]][c[2]+1]) + ' ' + 'isi_table[' + str(k[1]) + '][' + str(c[2]+1) + ']' + str(isi_table[k[1]][c[2]+1])
            #print(if1+if2+if3)
            if isi_table[k[0]][c[0]+1] == isi_table[k[1]][c[0]+1]:
                if isi_table[k[0]][c[1]+1] == isi_table[k[1]][c[1]+1]:
                    if isi_table[k[0]][c[2]+1] == isi_table[k[1]][c[2]+1]:
                        if isi_table[k[0]][c[3]+1] == isi_table[k[1]][c[3]+1]:
                            if isi_table[k[0]][c[4]+1] == isi_table[k[1]][c[4]+1]:
                                jumlah_sama += 1

        if (jumlah_sama == 0):
            r_vj_s.append(str(s_i)+" Y")
            list_v_memenuhi.append(str(s_i))
        else:
            r_vj_s.append(str(s_i)+" N")

        #if (isi_table[i][kolom] == jarak_baris_kolom and i!=baris-1):
        #    r_vj_w.append(str(r_vj_w_i)+"BREAK")
        #    continue
        #r_vj_w.append(str(r_vj_w_i))
        #print(r_vj_w_i)

    tabel_3 = tabulate(r_vj_s)
    write_file('output_rs(5).txt', tabel_3)
    print("r(v|s) : output_rs(4).txt")

    tabel_4 = tabulate(list_v_memenuhi)
    write_file('output_tabel_v_dan_s(5)_yg_memenuhi.txt', tabel_4)
    print("r(v|s) yg memenuhi untuk semua vertex : output_tabel_v_dan_s(4)_yg_memenuhi.txt")