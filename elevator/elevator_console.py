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
        return self.elevator
        
    def delete(self, n = 1):
        if self.elevator != {}:
            elevator_count = len(self.elevator)
            if elevator_count <= n:
                if str(input('Do you want delete all elevators? y/n: ')) == 'y':
                    n = elevator_count
                else:
                    return self.elevator
            start = elevator_count
            stop = start - n
            for i in range(start, stop, -1):
                del self.elevator[i]
            return self.elevator
        else:
            print('No elevators')
    
    def show(self):
        return self.elevator
    
    
'''--------------------------------------------Test space--------------------------------------------'''
a = Elevator()
b = Elevator()


a.create(2)
a.delete(3)
a.create(3)
a.delete(5)

b.create(4)
b.delete()

print(a.show())
print(b.show())
