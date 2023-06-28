def move(pos, move):
    while pos!=move[-1]:
        try:
            floor = int(input(':'))
        except:
            floor = move[-1] 
        if pos<move[-1]:
            if floor > pos and floor < move[-1]:
                move.append(floor)
            pos+=1
        else:
            if floor < pos and floor > move[-1]:
                move.append(floor)
            pos-=1
        print(pos)
        if len(move)>1 and move[-1]==pos:
            print('stop')
            del move[-1]
move(1,[9])
print('stop')
