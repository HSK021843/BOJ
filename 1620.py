N, M = map(int, input().split())
pokemons_name = {}
pokemons_index = {}

for i in range(N):
    pokemon = input()
    pokemons_name[i] = pokemon
    pokemons_index[pokemon] = i + 1

for _ in range(M):
    q = input()

    if q.isdigit():
        print(pokemons_name[int(q) - 1])
    else:
        print(pokemons_index[q])
