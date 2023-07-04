from random import randint as rd
pass_list = {}
padlock = 'password'


# i=0
# while True:
#     password = (''.join([chr(rd(65,123)) for _ in range(8)]))
#     if pass_list.get(password) == None:
#         i+=1
#         pass_list[password] = i
#         if password == padlock:
#             print(i, password, padlock)
#             break
    


i = 0
rep = 1
from itertools import product
alph = (''.join([chr(i) for i in range(65,123)]))
while True:
    password = product(alph, repeat=rep)
    for p in password:
        i+=1
        print(i,(''.join(p)))
        if (''.join(p)) == padlock:
            print(i, padlock, (''.join(p)))
            exit()
    rep += 1
