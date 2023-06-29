el = {
    1: {'move': False, 'floor': 1, 'task': 0, 'status': 'stop'},
    2: {'move': False, 'floor': 1, 'task': 0, 'status': 'stop'},
    3: {'move': False, 'floor': 1, 'task': 0, 'status': 'stop'}
}
task_list = {
    
}
while True:
    task = (input(':'))
    if task != '':
        task = int(task)
        task_list[task] = True
    

        for n in el:
            if el[n]['task'] == 0:
                el[n]['task'] = task
                break
    for n in el:
        if el[n]['floor'] < el[n]['task'] and el[n]['task'] != 0:
            el[n]['floor'] = el[n]['floor'] + 1
        elif el[n]['floor'] > el[n]['task'] and el[n]['task'] != 0:
            el[n]['floor'] = el[n]['floor'] - 1
        else:
            el[n]['task'] = 0
    for key, value in el.items():
        print(key, value)
