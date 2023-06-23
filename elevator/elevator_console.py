class Elevator:
    
    def __init__(self):
        self.elevator = {}
        
    def create(self, n = 1):
        if self.elevator != {}:
            start = max(self.elevator) + 1
        else:
            start = 1
        stop = start + n
        for i in range(start, stop):
            self.elevator[i] = {'move' : False, 'floor': 1}
        
    def delete(self, n = 1):
        if self.elevator != {}:
            elevator_count = len(self.elevator)
            if elevator_count <= n:
                if str(input('Do you want delete all elevators? y/n: ')) == 'y':
                    n = elevator_count
                else:
                    return
            start = elevator_count
            stop = start - n
            for i in range(start, stop, -1):
                del self.elevator[i]
        else:
            print('No elevators')
    
    def show(self, name = ''):
        print(f'Elevators group {name}:')
        for key, value in (self.elevator).items():
            print(f'elevator {key}: status{value}')

    def get_value(self):
        return self.elevator
    
    
'''--------------------------------------------Test space--------------------------------------------'''
a = Elevator()
b = Elevator()


a.create(2)
b.create(4)
b.delete()

a.show()
b.show('b')
# print(a.get_value())
