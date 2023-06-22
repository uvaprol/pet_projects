class Elevator():
    def __init__(self):
        print(elevator)
    def create(n):
        if elevator != {}:
            elevator_list = [key for key in elevator]
            elevator_list.sort()
            last_number = elevator_list[-1] + 1
        else:
            last_number = 1
        for i in range(last_number, last_number + n):
            elevator[i] = {'move' : False, 'floor': 1}
        return elevator
    def delete(n = 1):
        if elevator != {}:
            elevator_list = [key for key in elevator]
            elevator_list.sort()
            start = len(elevator_list)
            stop = start - n
            for i in range(start, stop, -1):
                del elevator[i]
            return elevator
        else:
            print('No elevators')
    
    
    

a = Elevator.create(5)
print(a)
a = Elevator.delete()
print(a)
