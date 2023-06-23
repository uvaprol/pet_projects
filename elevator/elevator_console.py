class Elevator(object):
    
    def __init__(self, name = ''):
        self.elevator = {}
        self.name = name
        
    def create(self, n = 1):
        if self.elevator != {}:
            start = max(self.elevator) + 1
        else:
            start = 1
        stop = start + n
        for i in range(start, stop):
            self.elevator[i] = {'move' : False, 'floor': 1}
        return self.elevator
        
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
    
    def show(self):
        if self.elevator != {}:
            print(f'Elevators group {self.name}:')
            for key, value in (self.elevator).items():
                print(f'elevator {key}: status{value}')
        else:
            print('No elevators')
        
    def get_value(self):
        return self.elevator
        
    def rename(self, name = ''):
        if name != '':
            self.name = name
            
    def move(self, floor):
        if self.elevator != {}:
            number = 1
            distance = abs(floor - self.elevator[1]['floor'])
            for key in self.elevator:
                if abs(floor - self.elevator[key]['floor']) < distance:
                    distance = abs(floor - self.elevator[key]['floor'])
                    number = key
            self.elevator[number]['floor'] = floor
        else:
            print('No elevators')
    
    
'''--------------------------------------------Test space--------------------------------------------'''
if __name__ == "__main__":
    a = Elevator('a')
    b = Elevator('b')
    
    
    a.create(2)
    a.rename('')
    a.show()
    a.move(4)
    a.show()
    a.move(2)
    a.show()
    a.move(1)
    a.show()
