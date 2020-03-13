def find_shortest_path(graphh, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    if start not in graphh:
        return None
    shortest = None
    for node in graphh[start]:
        if node not in path:
            newpath = find_shortest_path(graphh, node, end, path)
            if newpath:
                if not shortest or len(newpath) < len(shortest):
                    shortest = newpath
    return shortest

def write_file(nama, text):
    saveFile = open(nama, 'w')
    saveFile.write(text)
    saveFile.close()