def move(el, move_list):
    # floor = move_list[-1]

    # for key in el:
    #     if el[key]['ready_move']:
    #         number = key
    #         distance = abs(floor - el[key]['floor'])
    #         direction = int(floor - el[key]['floor'] >= 0) 
    #         break
    # try:
    #     for key in el:
    #         if abs(floor - el[key]['floor']) < distance and el[key]['ready_move']:
    #             distance = abs(floor - el[key]['floor'])
    #             number = key
    # except:
    #     pass
    # print(number)
    
    while True:
        pos = el['floor']
        try:
            move_list.append(int(input(':')))
        except:
            pass
        if pos<move_list[-1]:
            el['floor'] = el['floor'] + 1
            el['move'] = False
        elif pos>move_list[-1]:
            el['floor'] = el['floor'] - 1
            el['move'] = False
        if len(move_list)>1 and move_list[-1]==pos:
            del move_list[-1]
        print(el)
        el['move'] = True
el = {
    1: {'move': False, 'floor': 1, 'task': [], 'derection': 'stop'},
    2: {'move': False, 'floor': 1, 'task': [], 'derection': 'stop'},
    3: {'move': False, 'floor': 1, 'task': [], 'derection': 'stop'}
    
}

move(el[1], [9])
print('stop')
