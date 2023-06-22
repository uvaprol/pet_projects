towns = {
    'a':{'b':5, 'c':6, 'd':7},
    'b':{'a':5},
    'c':{'a':6},
    'd':{'a':7},
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
        parent_ways = towns[parent_town]
    except:
        parent_ways = {}
    while True:
        child_town = str(input(f'{parent_town} -> '))
        try:
            child_ways = towns[child_town]
        except:
            child_ways = {}
        if child_town == '':
            towns[parent_town] = parent_ways
            if child_ways != {}:
                towns[child_town] = child_ways
                return towns
            return towns
        if parent_town == child_town:
            print('chek town name')
            continue
        if parent_ways.get(child_town) != None:
            agree = str(input(f'Do you want change way to {child_town} y/n: '))
            if agree == 'y':
                way = int(input(f'way {child_town}: '))
                parent_ways[child_town] = way
                child_ways = towns[child_town]
                child_ways[parent_town] = way
        else:
            way = int(input(f'way {child_town}: '))
            parent_ways[child_town] = way
            child_ways[parent_town] = way
            
def show_town(towns):
    for key, value in towns.items():
        print(key, value)
    return

comands = {
    'create':create_town,
    'way':create_ways,
    'rename': rename_town,
    'show':show_town
}

while True:
    try:
        comand = comands.get(str(input('select comand:\nway\nrename\nshow\ncreate\n\n:')))
        comand(towns)
        print('___\n___')
    except:
        print('___\n___')
