def compress(coords):
    sort = sorted(set(coords))
    
    order = {}
    index = 0
    for coord in sort:
        order[coord] = index
        index += 1
    
    compressed = []
    for coord in coords:
        compressed.append(order[coord])
    
    return compressed


N = int(input())
coords = list(map(int, input().split()))

compressed = compress(coords)
print(' '.join(map(str, compressed)))
