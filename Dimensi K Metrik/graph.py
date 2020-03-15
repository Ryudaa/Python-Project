# List vertex

# Graphnya Celline
vertex1 = ['v1','v2','v3','v4','v5','v6','v7','v8','v9','v10','v11','v12']

# Graphnya Afif
vertex2 = ['a','b','c','d','e','f','g','h','i','j']

# Graphnya Erik
vertex3 = ['v1','v2','v3','v4','u1','u2','u3','u4']

# Keterhubungan vertex
# Format : 'vertex':['adjacent1','adjacent2']
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
graph2 = {'a':['b','c','d','e','f','g','h','i'],
    'b':['a','c','d','e','f','g','h','j'],
    'c':['a','b','d','e','f','g','i','j'],
    'd':['a','b','c','e','f','h','i','j'],
    'e':['a','b','c','d','g','h','i','j'],
    'f':['a','b','c','d','g','h','i','j'],
    'g':['a','b','c','e','f','h','i','j'],
    'h':['a','b','d','e','f','g','i','j'],
    'i':['a','c','d','e','f','g','h','j'],
    'j':['b','c','d','e','f','g','h','i']
    }
graph3= {'v1':['v2','v4','u1','u2','u4'],
    'v2':['v1','v3','u1','u2','u3'],
    'v3':['v2','v4','u2','u3','u4'],
    'v4':['v1','v3','u1','u3','u4'],
    'u1':['v1','v2','v4','u2','u4'],
    'u2':['v1','v2','v3','u1','u3'],
    'u3':['v2','v3','v4','u2','u4'],
    'u4':['v1','v3','v4','u1','u3']
    }

#########################################
vertex = vertex3
g = graph3
#########################################