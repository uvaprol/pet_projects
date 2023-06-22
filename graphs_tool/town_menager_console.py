import itertools


towns = {
    'a': {'b': 2, 'd': 1},
    'b': {'a': 2, 'c': 3, 'd': 3},
    'c': {'b': 3, 'd': 3, 'e': 2},
    'd': {'a': 1, 'b': 3, 'c': 3},
    'e': {'b': 2}
}

def router(start, finish):
    towns_mas=[[]]
    for key in towns:
        towns_mas[0] += key
    n = len(towns_mas[0])
    for i in range(2,n):
        towns_mas += itertools.permutations(towns_mas[0],i)
    return towns_mas

def way_calculade(way, towns):
    rout = 0
    gate = True
    for key in range(len(way)-1):
        try:
            rout += (towns[way[key]][way[key+1]])
        except:
            rout = 0
            gate = False
            break
    return rout, way, gate
    
def math_route(towns):
    start = str(input('start town: '))
    finish = str(input('finish town: '))
    towns_mas = router(start, finish)
    route = -1
    find_rout = ''
    for i in towns_mas:
        if i[0] == start and i[-1] == finish:
            find_way, way, gate = way_calculade(i, towns)
            if gate:
                if route == -1:
                    route = find_way
                    find_rout = way
                if route > find_way:
                    route = find_way
                    find_rout = way
         
    way = find_rout
    str_way = f'{way[0]} -> '
    for i in range(1,len(way)-1):
        str_way += f'{way[i]} -> ' 
    print(f'{str_way}{way[-1]} == {route}')



while True:
    math_route(towns)
    print('___\n___')
