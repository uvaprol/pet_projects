from random import randint as rd
from time import sleep

def show(el):
    for key in el:
        print(key, el[key])
    pass

def move(elevator, pos):
    # code start
    el = elevator[1]
     
    # repeat check
    for i in range(len(el['task'])-1):
        if el['task'][i] == el['task'][-1]:
            del el['task'][-1]
            break
    el['task'].sort()
    
    # task check
    if el['task'] != []:
        if el['task'][0] == pos:
            del el['task'][0]
            el['move'] = False
            el['status'] = 'pause'
        elif el['task'][-1] == pos:
            del el['task'][-1]
            el['move'] = False
            el['status'] = 'pause'
        show(elevator)
        
        # moving
        if el['task'] != []:
            if pos < el['task'][-1] and (el['status'] == 'stop' or el['status'] == 'up'):
                el['floor'] = el['floor'] + 1
                el['move'] = True
                el['status'] = 'up'
            elif pos > el['task'][0] and (el['status'] == 'stop' or el['status'] == 'down'):
                el['floor'] = el['floor'] - 1
                el['move'] = True
                el['status'] = 'down'
            elif el['status'] == 'pause':
                el['status'] = 'stop'
    else:
        el['status'] = 'stop'
        show(elevator)


def controler(elevator, control):
    el = elevator[1]
    if control == 'auto':
        # auto control
        for _ in range(int(input('number of repetitions: '))):  
            pos = el['floor']
            sleep(1)
            pk = True
            if rd(1,10) > 7:
                    el['task'].append(rd(1,10))
                    print(f":{el['task'][-1]}")
                    pk = False
            if pk:
                print(':')
            move(elevator, pos)
            

    elif control == 'hand':  
        # hand control
        while True:
            pos = el['floor']
            try:
                el['task'].append(int(input(':')))
            except:
                pass
            move(elevator, pos)
        
        
el = {
    1: {'move': False, 'floor': 1, 'task': [], 'status': 'stop'},
    2: {'move': False, 'floor': 1, 'task': [], 'status': 'stop'},
    3: {'move': False, 'floor': 1, 'task': [], 'status': 'stop'}
    
}
control = str(input('hand/auto: '))
controler(el, control)
print('stop')
