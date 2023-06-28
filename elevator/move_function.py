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
            floor = int(input(':'))
        except:
            floor = move_list[-1] 
        if pos<move_list[-1]:
            if floor > pos and floor < move_list[-1]:
                move_list.append(floor)
            el['floor'] = el['floor'] + 1
        elif pos>move_list[-1]:
            if floor < pos and floor > move_list[-1]:
                move_list.append(floor)
            el['floor'] = el['floor'] - 1
        print(pos)
        if len(move_list)>1 and move_list[-1]==pos:
            print('stop')
            del move_list[-1]
            
el = {
    1: {'ready_move': True, 'floor': 1, 'task': [], 'derection': 'stop'},
    2: {'ready_move': True, 'floor': 1, 'task': [], 'derection': 'stop'},
    3: {'ready_move': True, 'floor': 1, 'task': [], 'derection': 'stop'}
    
}

move(el[1], [9])
print('stop')
