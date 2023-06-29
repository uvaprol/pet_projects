from random import randint as rd
from time import sleep

def show(el):
    for key in el:
        print(key, el[key])
        

def move(el):
    show(el)
    pass


el = {
    1: {'move': False, 'floor': 1, 'task': {}, 'status': 'stop'},
    2: {'move': False, 'floor': 1, 'task': {}, 'status': 'stop'},
    3: {'move': False, 'floor': 1, 'task': {}, 'status': 'stop'}
}

task_list = []

while True:
    try:
        task = int(input(':'))
    except:
        pass
    
    for key in el:
        try:
            logic_gate = (task < max([t for t in el[key]['task']]))
        except:
            logic_gate = True
            
        print(logic_gate)
        if (el[key]['status'] == 'stop' or el[key]['status'] == 'down') and logic_gate:
            el[key]['task'][task] = True
            break
        pass
    
        
        
    move(el)
    
print('stop')
