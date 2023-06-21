import itertools


towns = {
    'a':{'b':5, 'c':3},
    'b':{'a':5,},
    'c':{'a':3, 'd':4},
    'd':{'c':4, 'm':2},
    'm':{'d':2}
}

def create_new_name():
    new_name = str(input('new name: '))
    while towns.get(new_name) != None:
        print(f'name {new_name} hes reserved')
        new_name = str(input('new name: '))
    return new_name
    
def create_town(towns, town = ''):
    if town != '':
        towns[town]={}
        return towns
    while True:
        town_name = create_new_name()
        if town_name != '':
            towns[town_name]={}
        else:
            return towns

def rename_town(towns):
    if towns == {}:
        return
    show_town(towns)
    while True:
        town = str(input('what town rename: '))
        if towns.get(town) == None and town != '':
            if str(input(f'town {town} not found, do you want create {town}? y/n: ')) == 'y':
                create_town(towns, town)
                print(f'town {town} created')
                continue
            else:
                continue
        elif town != '':
            new_name = create_new_name()
            for town_key in towns:
                if town_key != town:
                    towns[town_key][new_name] = towns[town_key].pop(town)
            towns[new_name] = towns.pop(town)
        else:
            return towns

def create_ways(towns):
    parent_town = str(input('town name: '))
    if parent_town == '':
        return towns
    try:
        ways = towns[parent_town]
    except:
        ways = {}
    while True:
        child_town = str(input(f'{parent_town} -> '))
        if child_town == '':
            towns[parent_town] = ways
            return towns
        if parent_town == child_town:
            print('chek town name')
            continue
        if ways.get(child_town) != None:
            agree = str(input(f'Do you want change way to {child_town} y/n: '))
            if agree == 'y':
                way = int(input(f'way {child_town}: '))
                ways[child_town] = way
                child_ways = towns[child_town]
                child_ways[parent_town] = way
        else:
            way = int(input(f'way {child_town}: '))
            ways[child_town] = way
            towns[child_town] = {parent_town: way}
            
def show_town(towns):
    for key, value in towns.items():
        print(key, value)
    return

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
                    print(route)
                    route = find_way
                    find_rout = way
         
    way = find_rout
    str_way = f'{way[0]} -> '
    for i in range(1,len(way)-1):
        str_way += f'{way[i]} -> ' 
    print(f'{str_way}{way[-1]} == {route}')





comands = {
    'create':create_town,
    'way':create_ways,
    'rename': rename_town,
    'show':show_town,
    'route':math_route
}

while True:
    try:
        comand = comands.get(str(input('select comand:\nway\nrename\nshow\ncreate\nroute\n\n:')))
        comand(towns)
        print('___\n___')
    except:
        print('___\n___')
