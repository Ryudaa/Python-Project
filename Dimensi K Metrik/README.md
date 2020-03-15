# Dimensi K Metrik

Penjelasan setiap file dan folder

##Contents
- [Folder Output](#folder-output)
- [defgraph.py](#defgraphpy)
- [graph.py](#graphpy)
- [programs.py](#programspy)

### Folder Output
Di folder ini semua output program disimpan.

### defgraph.py
Berisi fungsi-fungsi program.

### graph.py
Tempat untuk membentuk graph.

Contoh membentuk graf dengan 3 vertex :
```
vertexx = ["v1", "v2", "v3"]
```
Jangan diberi nama `vertex` karena nama itu nanti akan dipakai.

Selanjutnya menentukan edge pada graf. Misalkan ada 2 edge, yaitu `(v1,v2)` dan `(v2,v3)`.
```
graph = {"v1":["v2"],
  "v2":["v1", "v3"],
  "v3":["v2"]
  }
```
Perhatikan bahwa tidak cukup menjelaskan `v1` adjacent dengan `v2`, tapi juga harus sebaliknya.

### programs.py
File yang harus di run lewat Command Prompt.
