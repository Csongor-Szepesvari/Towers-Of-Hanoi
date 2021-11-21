from TowersVisualizer import *
# Towers of Hanoi fun implementation
a = [] #the towers
b = []
c = []
# The variable that designates how big the tower is
SIZE = 5
for i in range(SIZE):
    a.append(SIZE-i)
#how many moves made
moves = 0

def solver(size, fromTower, toTower, spare):
    global moves
    #too hard to solve
    #we solve smaller problem
    if size==1:
        toTower.append(fromTower.pop())
        moves+=1
        printTowers(SIZE, a, b, c)
    else:
        solver(size-1, fromTower, spare, toTower)
        toTower.append(fromTower.pop())
        moves+=1
        printTowers(SIZE, a, b, c)
        solver(size-1, spare, toTower, fromTower)

