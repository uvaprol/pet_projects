from random import randint as rd
from time import sleep

def move(el, move_map, pos):
    # code start
        # repeat check
        for i in range(len(move_map)-1):
            if move_map[i] == move_map[-1]:
                del move_map[-1]
                break
        move_map.sort()
        
        # task check
        if move_map != []:
            if move_map[0] == pos:
                del move_map[0]
                el['move'] = False
                el['direction'] = 'stop'
            elif move_map[-1] == pos:
                del move_map[-1]
                el['move'] = False
                el['direction'] = 'stop'
            print(el)
            
            # moving
            if move_map != []:
                if pos < move_map[-1] and (el['direction'] == 'stop' or el['direction'] == 'up'):
                    el['floor'] = el['floor'] + 1
                    el['move'] = True
                    el['direction'] = 'up'
                if pos > move_map[0] and (el['direction'] == 'stop' or el['direction'] == 'down'):
                    el['floor'] = el['floor'] - 1
                    el['move'] = True
                    el['direction'] = 'down'
        else:
            print(el)


def controler(el, move_map, control):
    
    if control == 'auto':
        # auto control
        for _ in range(int(input('number of repetitions: '))):  
            pos = el['floor']
            sleep(1)
            pk = True
            if rd(1,10) > 7:
                    move_map.append(rd(1,10))
                    print(f':{move_map[-1]}')
                    pk = False
            if pk:
                print(':')
            move(el, move_map, pos)
            

    elif control == 'hand':  
        # hand control
        while True:
            pos = el['floor']
            try:
                move_map.append(int(input(':')))
            except:
                pass
            move(el, move_map, pos)
        
        
el = {
    1: {'move': False, 'floor': 1, 'task': [], 'direction': 'stop'},
    2: {'move': False, 'floor': 1, 'task': [], 'direction': 'stop'},
    3: {'move': False, 'floor': 1, 'task': [], 'direction': 'stop'}
    
}
control = str(input('hand/auto: '))
controler(el[1], [], control)
print('stop')
